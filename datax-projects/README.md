# Introduction
This is the project that I completed during Spring 2017 Data-X class, taught at Berkeley under Professor Ikhlaq Sidhu.

I developed a real time image classification and video labeling app.

## Downloads ##
To download this project, click [here](http://tugan0329.bitbucket.io/downloads/datax/datax-projects.zip)

# Running the Code
You need an API key from [Clarifai](https://www.clarifai.com). 

After obtaining them, save the Client Key and Client Secret in the 'key.py' file under 'server' folder.

Make sure you have all corresponding pacakges mentioned in Software section below installed.

To run the video classification, run the following code under Python 3 environment.
```
$ chmod +x run.sh
$ ./run.sh
```

To run the real time classification, run the following code under Python 2 environment with OpenCV installed.
```
$ python server/livestream.py
```
Click on screen to close the camera app when you are finished. The predictions will be shown in the termial.

# Academic Honesty
If you are a student from UC Berkeley taking Data-X, please DO NOT read my code before you write your own.
Please submit your own code for grading.

The EECS Department Policy on Academic Dishonesty says, **"Copying all or part of another person's work, or using reference materials not specifically allowed, are forms of cheating and will not be tolerated."** 
The policy statement goes on to explain the penalties for cheating, which range from a zero grade for the test up to dismissal from the University, for a second offense.

Rather than copying my work, please ask your GSIs, TAs, lab assistants, and instructor for help. If you invest the time to learn the material and complete the projects, you won't need to copy any answers.

I will **not** be responsible for any consequence that resulted from any act of yours that may be deemed as cheating.

# Software
To view and test out the projects, you need Python 2 and 3 or above. You can get python [here](https://www.python.org/downloads/release/python-343/). 

You also need OpenCV, PyTube, Clarifai, Flask, Numpy, and ImageIo.