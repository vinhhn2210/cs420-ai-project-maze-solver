#import algorithms in level1 folder
from level1.algorithms import *
from level1.algorithms_level2 import *
from mapstate import *
import os 
import json
import re
import sys

# back to the parent folder
CUR_PATH = os.path.dirname(os.path.abspath(__file__))

def repl_func(match: re.Match):
    return " ".join(match.group().split())


# This is the main program for the project to navigate between frontend, backend and other class
class SystemController:
    def __init__(self):
        self.mapLists = {}

    def readUserImportMap(self, mapPath, levelID):
        mapName = f'input0-level{levelID}'
        print(mapName)
        self.mapLists[mapName] = loadMapOnDirectory(mapPath, mapName)

    def readFolderMap(self, folderName): 
        files = os.listdir(CUR_PATH + '/' + folderName)
        for file in files:
            fileName = file[:-4]
            self.mapLists[fileName] = loadMap(folderName, fileName)

    def readAllFolderMap(self, folderName):
        for level in range(1, 4):
            mapFolderName = folderName + f'/level{level}'
            self.readFolderMap(mapFolderName)

    
    def displayMap(self, mapName):
        self.mapLists[mapName].display()
    
    def displayMapList(self):
        for key in self.mapLists:
            self.mapLists[key].display()

    def writeSolutionJsonFile(self, mapName, agentPath, algorithm):
        # path = [(x1, y1, layer1), (x2, y2, layer2), ...]
        MapJson = self.mapLists[mapName]
        # write to json file
        jsonData = {
            "0": {
                "numFloor": MapJson.nLayer,
                "numAgent": len(agentPath),
                "floor": [],
                "mapSize": [MapJson.nRow, MapJson.mCol],
                "key": MapJson.getKeysPosition(),
                "map": MapJson.mazer,
                "agents": {
                   
                }
            }
        }
        floorList = []
        for i in range(0, len(agentPath)):
            xCor, yCor, layer, key = agentPath[i][0]
            if (layer not in floorList):
                floorList.append(layer)
            jsonData['0']['agents'][str(i + 1)] = {
                "position": [xCor, yCor, layer],
                "key": listKeys(key)
            }
        jsonData['0']['floor'] = floorList
        numStep = len(agentPath[0])
        #print(agentPath)
        for i in range(1, numStep):
            floorList = []
            for j in range(0, len(agentPath)):
                xCor, yCor, layer, key = agentPath[j][i]
                if (layer not in floorList):
                    floorList.append(layer)

            jsonData[str(i)] = {
                "isWin": (i == numStep - 1),
                "floor": floorList,
                "step": i,
                "agents": {
                }
            }
            for j in range(0, len(agentPath)):
                xCor, yCor, layer, key = agentPath[j][i]
                jsonData[str(i)]['agents'][str(j + 1)] = {
                    "position": [xCor, yCor, layer],
                    "key": listKeys(key)
                }
        SOL_PATH = CUR_PATH + '/Solution/' + mapName + '_' + algorithm + '.json'
        with open(SOL_PATH, "w") as outfile:
            # write to json file with endline
            json_str = json.dumps(jsonData, indent=4)
            json_str = re.sub(r"(?<=\[)[^\[\]]+(?=])", repl_func, json_str)
            outfile.write(json_str)
        print('Write to file ' + mapName + '_' + algorithm + '.json successfully')

    def getMapLevel(self, mapName):
        mapInfo = mapName.split('-')
        if len(mapInfo) != 2:
            return 1
        mapLevel = mapInfo[1][5:]
        return int(mapLevel)

    def solving(self, mapName, algorithm):
        mapLevel = self.getMapLevel(mapName)

        MazeSolver = None

        if mapLevel == 2:
            MazeSolver = MazerSolverLevel2(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol, self.mapLists[mapName].nLayer)
        else:
            MazeSolver = MazerSolverLevel3(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol, self.mapLists[mapName].nLayer)
        
        start = MazeSolver.agentPosition('A1')
        goal = MazeSolver.goalPosition('T1')
        #self.mapLists[mapName].display()
        solution = []
        if algorithm == 'dfs':
            solution = MazeSolver.dfs(start, goal)
        elif algorithm == 'bfs':
            solution = MazeSolver.bfs(start, goal)
        elif algorithm == 'astar':
            solution = MazeSolver.astar(start, goal)

        if solution:
            self.writeSolutionJsonFile(mapName, [solution], algorithm)
        else:
            print('No solution for ' + mapName + ' with ' + algorithm + ' algorithm')
        return solution

    def solvingAllMap(self, algorithm):
        for mapName in self.mapLists:
            self.solving(mapName, algorithm)

    def solveAStarMap(self):
        for mapName in self.mapLists:
            mapLevel = self.getMapLevel(mapName)

            if mapLevel == 2:
                self.solving(mapName, 'astar')


# system.displayMap('input1-level2')

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Please enter the correct command')
        print('Example: python3 system.py Map_folder')
        exit()
    system = SystemController()
    system.readAllFolderMap(sys.argv[1])
    # system.readFolderMap(sys.argv[1])
    system.solvingAllMap('dfs')
    system.solvingAllMap('bfs')
    system.solvingAllMap('astar')
    # system.solveAStarMap()
    
    