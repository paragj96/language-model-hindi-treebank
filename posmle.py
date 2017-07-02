import nltk
import json
import pickle
import ssfAPI
from nltk import ngrams
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer

def getPOS():

    pos = {}

    with open('pos.txt') as file:
        pos = json.load(file)

    file.close()    

    return pos

def getWords():

    words = []

    with open("training.txt", "rb") as file:
        words = pickle.load(file)

    file.close()

    return words

def getFreqUnigram(words):

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

def getBigrams(words):

    bigrams = []

    for i in range(0, len(words)-1):
        tempList = []
        tempList.insert(i, words[i])
        tempList.insert(i+1, words[i+1])
        bigrams.append(tuple(tempList))

    return bigrams

def getFreqBigram(bigrams):

    freq = {}

    for grams in bigrams:
        freq[grams] = freq.get(grams, 0) + 1

    return freq

def getMLE():

    words = getWords()

    unigramFreq = getFreqUnigram(words)

    bigramFreq = getFreqBigram(getBigrams(words))

    pos = getPOS()

    mleAll = {}

    for key in pos:
        word = pos[key]

        tempDict = {}

        for key in bigramFreq:
            if key[0] == word:
                tempDict[key] = bigramFreq[key]

        mle = {}

        if bool(tempDict):
            sortedList = sorted(tempDict, key=tempDict.get, reverse=True)

            i = 0

            while i < len(sortedList):
                temp = sortedList[i]

                count = tempDict[temp]

                prob = count/float(unigramFreq[word])

                mle[sortedList[i][1]] = prob

                i = i + 1

        mleAll[word.encode('utf-8')] = mle

    maxmle = {}

    for key in mleAll:
        mle = mleAll[key]

        maxval = 0

        for k in mle:
            v = mle[k]

            if v >= maxval:
                maxval = v
                maxkey = k

        '''

        print str(key) + ":" + str(mleAll[key]) + "\n\tmax:" + str(maxval)

        tempmax = {}

        tempmax[maxkey] = maxval

        maxmle[key] = tempmax

        '''

        maxmle[key] = maxkey

    return maxmle

def calcProb(maxmle):

    words = []      #inference words
    
    with open("inference.txt", "rb") as file:
        words = pickle.load(file)

    file.close()

    calc = {}

    total = {}

    for i in range(0, len(words)-1):
        word = words[i]
        nextWord = words[i+1]

        if maxmle[word] == nextWord:
            calc[word] = calc.get(word, 0) + 1

        total[word] = total.get(word, 0) + 1

    accall = []

    for key in total:
        c = calc.get(key, 0)
        t = total[key]

        acc = c/float(t)

        accall.append(acc*100)

    sum = 0

    for i in range(0, len(accall)):
        sum = sum + accall[i]

    print "Accuracy: " + str((sum/float(len(accall))))


if __name__ == "__main__":

    calcProb(getMLE())
