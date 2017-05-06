from __future__ import print_function
import json
from flask import Flask, request, redirect, url_for, send_from_directory
import frame
import classifier
import api
import numpy as np
import sys
import os
import glob
import random
import imageio

# Setup Flask app.
app = Flask(__name__)
app.debug = True
app._static_folder = '../client'


# Setup classifier.
# Creates classification network and node ID --> English string lookup.
# node_lookup = classifier.NodeLookup()
videoFolder = './server/videos'
cacheFolder = './server/cache'
# createdGraph = False

if "cache" not in os.listdir('./server'):
    os.mkdir("./server/cache")

# Routes
@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

@app.route('/cached', methods=['GET'])
def cached_handler():
    resData = []
    for file in glob.glob(cacheFolder + "/*.json"):
        resData.append(file.rsplit('.', 1)[0].rsplit('/', 1)[-1])
    return json.dumps(random.sample(resData, min(len(resData), 14)))

@app.route('/video', methods=['POST'])
def json_handler_api():
    reqData = json.loads(request.data)
    youtube_id = frame.get_youtube_id(reqData['url'])
    filename = cacheFolder + "/" + youtube_id + ".json"
    print (filename)
    try:
        cached = open(filename, 'r')
        print("Found %s in JSON cache" % (filename))
        resJson = cached.read()
        # print (resJson)
        resData = json.loads(resJson)
    except:
        print("Didn't find %s in JSON cache: %s" % (filename, str(sys.exc_info())) )
        print (reqData['url'])
        frame_time_tuple, folder = frame.extract_files(reqData['url'])
        predictions = dict()
        times = [x[1] for x in frame_time_tuple]
        destinations = [x[2] for x in frame_time_tuple]
        resData = {"labels" : {}}

        for i, img in enumerate(destinations):
            if ".jpg" in img:
                prediction = api.classify(img) #  list of names and probs
                for pair in prediction:
                    concept = pair[0]
                    prob = pair[1]
                    if concept not in resData["labels"]:
                        resData["labels"][concept] = dict()
                        resData["labels"][concept]["times"] = list()
                        resData["labels"][concept]["scores"] = list()
                    resData["labels"][concept]["times"].append(times[i])
                    resData["labels"][concept]["scores"].append(prob)
        # Response data should be formatted like this.
        # resData = {
        #     "labels": {
        #         "cat" : {
        #             "times": [40,50,60,70],
        #             "scores" : [0.8, 0.3, 0.4, 0.9]
        #         },
        #         "dog" : {
        #             "times": [120,130,140]
        #             "scores" : [0.8, 0.3, 0.4]
        #         }
        #     }
        # }

        # Remove any consecutive label times
        for label, obj in resData["labels"].items():
            start = 1
            times = obj["times"]
            scores = obj["scores"]
            for i in range(1, len(times), 1):
                if times[i] - times[i-1] > 1:
                    times[start] = times[i]
                    scores[start] = scores[i]
                    start = start + 1
                else:
                    # stick the higher value into the one we're keeping for this label
                    if scores[i] > scores[start-1]:
                        scores[start-1] = scores[i]
            times = times[:start]
            scores = scores[:start]
            if start >= 15:
                indicies = random.sample(range(start), 15)
                obj["times"] = list()
                obj["scores"] = list()
                for i in indicies:
                    obj["times"].append(times[i])
                    obj["scores"].append(scores[i])
            else:
                obj["times"] = times
                obj["scores"] = scores
        print(resData)
        resJson = json.dumps(resData)
        cached = open(filename, 'w')
        cached.write(resJson)
    else:
        # See if this cached file has the labelId attribute
        for label, info in resData["labels"].items():
            good = ("labelId" in info) and isinstance(info["labelId"], str)
            break
        if not good:
            resData["youtubeId"] = youtube_id
            for label, info in resData["labels"].items():
                info["labelId"] = node_lookup.string_to_id(label)
            # Write to cache
            print("Adding nodeIds to cached data")
            print(resData)
            resJson = json.dumps(resData)
            cached = open(filename, 'w')
            cached.write(resJson)
    pruneLabels(resData, 0.55)
    return json.dumps(resData)

# Removes all entries with a score lower than the the given threshold
def pruneLabels(resData, threshold):
    items = resData["labels"].items()
    todelete = list()
    for label, obj in items:
        start = 0
        times = obj["times"]
        scores = obj["scores"]
        for i in range(len(times)):
            if scores[i] >= threshold:
                times[start] = times[i]
                scores[start] = scores[i]
                start = start + 1
        obj["times"] = times[:start]
        obj["scores"] = scores[:start]
        if len(obj["times"]) == 0:
            todelete.append(label)
    for label in todelete:
        del resData["labels"][label]

    resData["sortedLabels"] = sorted(resData["labels"], key=lambda label: max(resData["labels"][label]["scores"]), reverse=True)

if __name__ == '__main__':
  app.run()
