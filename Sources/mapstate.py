import os
PARENT_PATH = os.path.dirname(os.getcwd())
MAP_PATH = os.path.join(PARENT_PATH, 'Map')
SOL_PATH = os.path.join(PARENT_PATH, 'Solution')


class MapState:
    def __init__(self, name, nRow, mCol, nLayer = 1, mazer = []):
        self.name = name
        self.nRow = nRow
        self.mCol = mCol
        self.nLayer = nLayer
        self.mazer = mazer

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
                    print(traceMaze[i][j][k], end = '\t')
                print()
            print()
    def getKeysPosition(self):
        keyList = []
        for i in range(self.nLayer):
            for j in range(self.nRow):
                for k in range(self.mCol):
                    if len(self.mazer[i][j][k]) > 1 and self.mazer[i][j][k][0] == 'K':
                        keyList.append([j, k, i])
        return keyList
def loadMap(mapName):
    new_path = os.path.join(MAP_PATH, f'{mapName}.txt')

    with open(new_path, 'r') as data:
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