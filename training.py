import pickle
import ssfAPI

def getWords():

    inputPath = '/home/aishwary/Desktop/ltrc/training'

    fileList = ssfAPI.folderWalk(inputPath)

    newFileList = []

    for fileName in fileList:
        xFileName = fileName.split('/')[-1]
        if xFileName == 'err.txt' or xFileName.split('.')[-1] in ['comments', 'bak'] or xFileName[:4] == 'task':
            continue
        else:
            newFileList.append(fileName)

    words = []

    for fileName in newFileList:
        d = ssfAPI.Document(fileName)
        for tree in d.nodeList:
            for chunkNode in tree.nodeList:
                for node in chunkNode.nodeList:
                    words.append(node.type.encode('utf-8'))

    return words

if __name__ == '__main__':

    words = getWords()

    #Below code is used to write list into a text file

    with open('training.txt', 'w') as file:
        pickle.dump(words, file)

    file.close()

    '''
    This code can be used to read list from text file

    
    with open("training.txt", "rb") as file:
        words = pickle.load(file)

    '''