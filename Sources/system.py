#import algorithms in level1 folder
from level1.algorithms import *
from level1.algorithms_level2 import *
from level1.algorithms_level1 import *
from mapstate import *
from lists_of_algorithms import *
import os 
import json
import re
import sys
import time
import psutil
import tracemalloc
import PIL.Image as Image
from matplotlib import pyplot as plt
# back to the parent folder
CUR_PATH = os.path.dirname(os.path.abspath(__file__))

def repl_func(match: re.Match):
    return " ".join(match.group().split())


# This is the main program for the project to navigate between frontend, backend and other class
class SystemController:
    def __init__(self):
        self.mapLists = {}
        self.timeCount = 0
        self.memoryCount = 0
        
    def readUserImportMap(self, mapPath, levelID):
        mapName = f'input0-level{levelID}'
        self.mapLists[mapName] = loadMapOnDirectory(mapPath, mapName)

    def readFolderMap(self, folderName): 
        files = os.listdir(CUR_PATH + '/' + folderName)
        for file in files:
            fileName = file[:-4]
            self.mapLists[fileName] = loadMap(folderName, fileName)

    def readAllFolderMap(self, folderName, levelID = None):
        if levelID != None:
            mapFolderName = folderName + f'/level{levelID}'
            self.readFolderMap(mapFolderName)
            return
        for level in range(1, 4):
            mapFolderName = folderName + f'/level{level}'
            self.readFolderMap(mapFolderName)

    def printMapList(self):
        for i, key in enumerate(self.mapLists):
            print(f'{i + 1}. {key}')

    def displayMap(self, mapName):
        self.mapLists[mapName].display()
    
    def displayMapList(self):
        for key in self.mapLists:
            self.mapLists[key].display()

    def measureStart(self):
        tracemalloc.clear_traces()
        self.timeCount = time.time()
        self.memoryCount = psutil.Process()
    def measureEnd(self):
        self.timeCount = time.time() - self.timeCount
        self.memoryCount = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
        #self.memoryCount = self.memoryCount.memory_info().rss / (1024 ** 2)
        # print time, mem with 4 digits after comma
        self.timeCount = round(self.timeCount * 1000, 4)
        self.memoryCount = round(self.memoryCount, 4)
        print('\t+ Time: \t{} ms'.format(self.timeCount))
        print('\t+ Memory:\t{} Mib'.format(self.memoryCount))
        return self.timeCount, self.memoryCount

    def createFloorImage(self, FLOOR_PATH, grid):
        heatmap = grid.copy()
        #print(heatmap)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1: # obstacle cell
                    heatmap[i][j] = 0
                elif grid[i][j] == 0: # empty cell, color white
                    heatmap[i][j] = 1
                elif grid[i][j] >= 600: # stair down cell
                    heatmap[i][j] = 0.15
                elif grid[i][j] >= 500: # stair up cell
                    heatmap[i][j] = 0.2
                elif grid[i][j] >= 400: # door cell
                    heatmap[i][j] = 0.1
                elif grid[i][j] >= 300: # agent cell
                    heatmap[i][j] = 0.3
                elif grid[i][j] >= 200: # key cell
                    heatmap[i][j] = 0.4
                elif grid[i][j] >= 100: # goal cell
                    heatmap[i][j] = 0.6
                else: # agent cell (can be multiple times)
                    heatmap[i][j] = 1 - float(grid[i][j]) / 15
        # create a floor image
        plt.figure(figsize=(10, 10))
        plt.imshow(heatmap, cmap='hot', interpolation='nearest')
        plt.savefig(FLOOR_PATH)
        plt.close()


    def createHeatMapImage(self, HEATMAP_PATH, MapJson, agentPath):
        # create a heatmap image with floor image for each agentPath
        grid = []
        for layer in range(MapJson.nLayer):
            grid.append([[0 for i in range(MapJson.mCol)] for j in range(MapJson.nRow)])
            for xCor in range(MapJson.nRow):
                for yCor in range(MapJson.mCol):
                    if MapJson.mazer[layer][xCor][yCor] == '-1':
                        grid[layer][xCor][yCor] = -1
                    elif MapJson.mazer[layer][xCor][yCor] == 'UP':
                        grid[layer][xCor][yCor] = 500
                    elif MapJson.mazer[layer][xCor][yCor] == 'DO':
                        grid[layer][xCor][yCor] = 600
                    elif MapJson.mazer[layer][xCor][yCor][0] == 'T':
                        grid[layer][xCor][yCor] = 100
                    elif MapJson.mazer[layer][xCor][yCor][0] == 'K':
                        grid[layer][xCor][yCor] = 200
                    elif MapJson.mazer[layer][xCor][yCor][0] == 'A':
                        grid[layer][xCor][yCor] = 300
                    elif MapJson.mazer[layer][xCor][yCor][0] == 'D':
                        grid[layer][xCor][yCor] = 400
                    
        
        # create a heatmap image folder for each map, then for each agentPath, create a heatmap image
        if not os.path.exists(HEATMAP_PATH):
            os.makedirs(HEATMAP_PATH)
        
        for i in range(0, len(agentPath)):
            xCor, yCor, layer, key = agentPath[i]
            grid[layer][xCor][yCor] += 1
        # create a heatmap image for each floor

        for floor in range(MapJson.nLayer):
            # create a floor image
            FLOOR_PATH = HEATMAP_PATH + '/floor' + str(floor + 1) + '.png'
            # create a heatmap image
            self.createFloorImage(FLOOR_PATH, grid[floor])


    def writeHeatMapFile(self, mapName, agentPath, algorithm):
        # create a heatmap image folder for each map, then for each agentPath, create a heatmap image
        # path = [(x1, y1, layer1), (x2, y2, layer2), ...]
        MapJson = self.mapLists[mapName]
        # create folder
        HEATMAP_FOLDER = CUR_PATH + '/Heatmap/' + mapName + '_' + algorithm
        if not os.path.exists(HEATMAP_FOLDER):
            os.makedirs(HEATMAP_FOLDER)
        # create heatmap image for each agentPath
        for i in range(0, len(agentPath)):
            # create a heatmap image for each agentPath
            HEATMAP_PATH = HEATMAP_FOLDER + '/agent' + str(i + 1)
            # create a heatmap image
            self.createHeatMapImage(HEATMAP_PATH, MapJson, agentPath[i])

        print("\t+ Output to heatmap " + mapName + '_' + algorithm + ' successfully...')        

    def writeSolutionJsonFile(self, mapName, agentPath, algorithm):
        # path = [(x1, y1, layer1), (x2, y2, layer2), ...]
        MapJson = self.mapLists[mapName]
        # write to json file
        jsonData = {
            "0": {
                "time": self.timeCount,
                "memory": self.memoryCount,
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
        print('\t+ Output to ' + mapName + '_' + algorithm + '.json successfully...')

    def getMapLevel(self, mapName):
        mapInfo = mapName.split('-')
        if len(mapInfo) != 2:
            return 1
        mapLevel = mapInfo[1][5:]
        return int(mapLevel)

    def solving(self, mapName, algorithm):
        print('-' * 50)
        print('Solving ' + mapName + ' with ' + algorithm + ' algorithm...')
        mapLevel = self.getMapLevel(mapName)

        MazeSolver = None

        if mapLevel == 1:
            MazeSolver = MazerSolverLevel1(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol)
        elif mapLevel == 2:
            MazeSolver = MazerSolverLevel2(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol, self.mapLists[mapName].nLayer)
        else:
            MazeSolver = MazerSolverLevel3(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol, self.mapLists[mapName].nLayer)
        
        start = MazeSolver.agentPosition('A1')
        goal = MazeSolver.goalPosition('T1')

        # run algorithm and measure time and memory
        self.measureStart()
        
        #self.mapLists[mapName].display()
        if not hasattr(MazeSolver, algorithm):
            # extract the sub string after the word level
            level = mapName.split('-')[1]
            print(f'No {algorithm} for ' + level)
            return
        solution = []
        if algorithm == 'dfs':
            solution = MazeSolver.dfs(start, goal)
        elif algorithm == 'bfs':
            solution = MazeSolver.bfs(start, goal)
        elif algorithm == 'astar':
            solution = MazeSolver.astar(start, goal)
        elif algorithm == 'ucs':
            solution = MazeSolver.ucs(start, goal)
        
        self.measureEnd()
        
        if solution:
            print('\t+ Steps:\t' + str(len(solution[0])))
            print('\t+ Score:\t' + str(100 - len(solution[0])))
            print('Logs: ')
            self.writeSolutionJsonFile(mapName, solution, algorithm)
            self.writeHeatMapFile(mapName, solution, algorithm)
        else:
            print('No solution for ' + mapName + ' with ' + algorithm + ' algorithm')
        return solution

    def solvingUserImportMap(self, algorithm):
        for mapName in self.mapLists:
            solution = self.solving(mapName, algorithm)
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
    if len(sys.argv) != 3 or (sys.argv[2] != 'auto' and sys.argv[2] != 'guide'):
        print('Please enter the correct command')
        print('1. To automaticly solving all map with all current algorithms:\n\t python3 Sources/system.py Map auto')
        print('2. to solve with specify map-algorithm:\n\t python3 Sources/system.py Map guide')
        exit()
     
    system = SystemController()
        # Reading map from folder
    print('Folder ' + sys.argv[1] + ' is being processed...')
    system.readAllFolderMap(sys.argv[1])
    print('Load folder: ' + sys.argv[1] + ' is done!')
    print("List of map: ")
    system.printMapList()
    # solving map
    print('-' * 50)
    tracemalloc.start()
    if sys.argv[2] == 'auto':
        print('Solving all map with all current algorithms...')
        system.solvingAllMap('dfs')
        system.solvingAllMap('bfs')
        system.solvingAllMap('ucs')
        system.solvingAllMap('astar')
    elif sys.argv[2] == 'guide':
        print('Please choose the map you want to solve, for example: input1-level1')
        mapName = input('Enter the map name: ')
        if mapName not in system.mapLists:
            print('Map name is not exist!')
            exit()
        print('Please choose the algorithm you want to solve, for example: dfs ')
        for i, algo in enumerate(algo_lists[f'level{system.getMapLevel(mapName)}']):
            print(f'{i + 1}. {algo}')
        algorithm = input('Enter the algorithm name: ')
        if algorithm == 'dfs':
            system.solving(mapName, 'dfs')
        elif algorithm == 'bfs':
            system.solving(mapName, 'bfs')
        elif algorithm == 'ucs':
            system.solving(mapName, 'ucs')
        elif algorithm == 'astar':
            system.solving(mapName, 'astar')
        else:
            print('Algorithm is not exist!')
            exit()
        print('Solving ' + mapName + ' with ' + algorithm + ' algorithm is done!')
    tracemalloc.stop()
    # done and visualize the solution
    print('-' * 50)
    print('Program is done!')
    print('To visualize the solution, please run the main.py file')
    print('\t python3 main.py')
    print('Thank you for using our program!')