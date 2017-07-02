import json
import ssfAPI

def getPOS():

    inputPath = '/home/aishwary/Desktop/ltrc/treebank'

    fileList = ssfAPI.folderWalk(inputPath)

    newFileList = []

    for fileName in fileList:
        xFileName = fileName.split('/')[-1]
        if xFileName == 'err.txt' or xFileName.split('.')[-1] in ['comments', 'bak'] or xFileName[:4] == 'task':
            continue
        else:
            newFileList.append(fileName)

    pos = {}

    for fileName in newFileList:
        d = ssfAPI.Document(fileName)
        for tree in d.nodeList:
            for chunkNode in tree.nodeList:
                for node in chunkNode.nodeList:
                    pos[node.type.encode('utf-8')] = node.type.encode('utf-8')

    return pos

if __name__ == '__main__':

    pos = getPOS()

    #Below code writes the dictionary to a text file using JSON
    with open('pos.txt', 'w') as file:
        json.dump(pos, file)

    file.close()

    '''
    This code can be used to read dictionary from text file

    pos = {}

    with open('pos.txt') as file:
        pos = json.load(file)
    '''