
# load model first - it takes some time
# download the Word2Vec Model from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit and put it in the same folder as this file

def loadModel():
    from gensim.models.keyedvectors import KeyedVectors
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  
    return model

def getCategory (labels, word_input, model = None):
    from gensim.models.keyedvectors import KeyedVectors
    if model == None:
        model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)  
    for label in labels: 
        for word in model.most_similar_cosmul(positive=[label], topn=100):
            if word[0] == word_input:
                return label
    return word_input
