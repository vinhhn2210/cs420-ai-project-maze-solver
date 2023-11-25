#import algorithms in level1 folder
from level1.algorithms import *
from map import *
import os 
import json

# This is the main program for the project to navigate between frontend, backend and other class
class SystemController:
    def __init__(self):
        self.mapLists = {}

    def readFolderMap(self, folderName): 
        # list all txt files in the folder using os
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\' + folderName, cur_path)
        files = os.listdir(new_path)
        for file in files:
            fileName = file[:-4]
            self.mapLists[fileName] = loadMap(fileName)
    
    def displayMap(self, mapName):
        self.mapLists[mapName].display()
    
    def displayMapList(self):
        for key in self.mapLists:
            self.mapLists[key].display()

    def solutionJsonFile(self, mapName, path, algorithm):
        # path = [(x1, y1, layer1), (x2, y2, layer2), ...]
        traceMaze = self.mapLists[mapName].mazer.copy()
        for i in range(1, len(path)):
            xCor, yCor, layer, key = path[i]
            traceMaze[layer][xCor][yCor] = i
        # write to json file
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\Solution\\' + mapName + '_' + algorithm + '.json', cur_path)
        jsonData = {

        }
        
        with open(new_path, "w") as outfile:
            json.dump(jsonData, outfile)

    def solving(self, mapName, algorithm):
        MazeSolver = MazerSolverLevel1(self.mapLists[mapName].mazer, self.mapLists[mapName].nRow, self.mapLists[mapName].mCol, self.mapLists[mapName].nLayer)
        start = MazeSolver.agentPosition('A1')
        goal = MazeSolver.agentPosition('T1')
        #self.mapLists[mapName].display()
        solution = []
        if algorithm == 'dfs':
            solution = MazeSolver.dfs(start, goal)
        elif algorithm == 'bfs':
            solution = MazeSolver.bfs(start, goal)
        if solution:
            self.mapLists[mapName].visualize(solution)
        else:
            print('No solution')
            print(goal)
system = SystemController()
system.readFolderMap('Map')
system.solving('input1-level1', 'bfs')
#system.displayMap('input1-level2')