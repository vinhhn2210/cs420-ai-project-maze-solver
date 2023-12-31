import os
from colorama import Fore
import copy
CUR_PATH = os.path.dirname(os.path.abspath(__file__))

class MapState:
    def __init__(self, name, nRow, mCol, nLayer = 1, mazer = []):
        self.name = name
        self.nRow = nRow
        self.mCol = mCol
        self.nLayer = nLayer
        self.mazer = copy.deepcopy(mazer)

    def display(self):
        print(self.name)
        print(self.nRow, self.mCol, self.nLayer)
        # print beautiful map with floor
        for i in range(self.nLayer):
            print('[floor' + str(i + 1) + ']')
            for j in range(self.nRow):
                for k in range(self.mCol):
                    print(self.mazer[i][j][k], end = '\t')
                print('|')
            print()
    
    def visualize(self, path):
        # visualize the path
        # path = [(x1, y1, layer1), (x2, y2, layer2), ...]
        traceMaze = self.mazer.copy()
        for i in range(1, len(path)):
            xCor, yCor, layer, key = path[i]
            traceMaze[layer][xCor][yCor] = i
        for i in range(self.nLayer):
            print('[floor' + str(i + 1) + ']')
            for j in range(self.nRow):
                for k in range(self.mCol):
                    s = str(traceMaze[i][j][k])
                    if (len(s) == 1):
                        s = '  ' + s
                    elif (len(s) == 2):
                        s = ' ' + s
                    if (traceMaze[i][j][k] == '-1'):
                        print(Fore.RED + s, end = ' ')
                    elif (traceMaze[i][j][k] == '0'):
                        print(Fore.GREEN + s, end = ' ')
                    elif (traceMaze[i][j][k] == 'A1'):
                        print(Fore.YELLOW + s, end = ' ')
                    else:
                        print(Fore.WHITE + s, end = ' ')
                print()
            print()
    def getKeysPosition(self):
        keyList = []
        for i in range(self.nLayer):
            for j in range(self.nRow):
                for k in range(self.mCol):
                    if len(self.mazer[i][j][k]) > 1 and self.mazer[i][j][k][0] == 'K':
                        keyList.append([int(self.mazer[i][j][k][1:]), j, k, i])
        sorted(keyList, key = lambda x: x[0])

        return keyList
def loadMap(folderPath, mapName):
    MAP_PATH = os.path.join(CUR_PATH, folderPath, mapName + '.txt')

    with open(MAP_PATH, 'r') as data:
        # read lines in data without \n
        lines = [line.rstrip('\n') for line in data]
        nRow, mCol = list(map(int, lines[0].split(',')))
        nLayer = 1
        mazer = []
        for i in range(1, len(lines)):
            if lines[i].startswith('[') and lines[i].endswith(']'):
                nLayer = int(lines[i][6:-1])
                mazer.append([])
            else:
                row_data = lines[i].split(',')
                mazer[nLayer - 1].append(row_data)
        return MapState(mapName, nRow, mCol, nLayer, mazer)

def loadMapOnDirectory(mapDirectory, mapName):
    MAP_PATH = mapDirectory

    with open(MAP_PATH, 'r') as data:
        # read lines in data without \n
        lines = [line.rstrip('\n') for line in data]
        nRow, mCol = list(map(int, lines[0].split(',')))
        nLayer = 1
        mazer = []
        for i in range(1, len(lines)):
            if lines[i].startswith('[') and lines[i].endswith(']'):
                nLayer = int(lines[i][6:-1])
                mazer.append([])
            else:
                row_data = lines[i].split(',')
                mazer[nLayer - 1].append(row_data)
        return MapState(mapName, nRow, mCol, nLayer, mazer)

def listKeys(keyMask):
    keyList = []
    for i in range(32):
        if keyMask & (1 << i) != 0:
            keyList.append(i)
    return keyList
    '''
20,15
[floor1]
A1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0
-1,0,0,0,0,0,0,0,0,0,0,0,0,0,T1
Example of map file
    '''