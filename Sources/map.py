import os

class Map:
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

def loadMap(mapName):
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('..\\Map\\' + mapName +'.txt', cur_path)

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
        return Map(mapName, nRow, mCol, nLayer, mazer)

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