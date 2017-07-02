import nltk
from nltk import ngrams
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer

def getWords(text):

    tokenizer = RegexpTokenizer(r'\w+')

    words = tokenizer.tokenize(text)

    for i in range(0,len(words)):
		words[i] = (words[i].lower()).encode('utf-8')

    return words

def getFreqUnigram(words):

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

def getBigram(words):

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

def getMLE(word):

    text = gutenberg.raw()

    words = getWords(text)

    unigramFreq = getFreqUnigram(words)

    bigramFreq = getFreqBigram(getBigram(words))

    tempDict = {}

    for key in bigramFreq:
        if key[0] == word:
            tempDict[key] = bigramFreq[key]

    mle = {}

    if bool(tempDict):
        sortedList = sorted(tempDict, key=tempDict.get, reverse=True)    

        for i in range(0, 3):
            count = tempDict[sortedList[i]]

            prob = count/float(unigramFreq[word])

            mle[sortedList[i][1]] = prob

    return mle

if __name__ == "__main__":

    print "Maximum Likelihood Estimation"

    word = raw_input("Enter a word: ")

    nextWord = getMLE(word.lower())

    if bool(nextWord):
        print "Next word may be:"

        print nextWord

    else:
        print "Cannot determine next word"    
