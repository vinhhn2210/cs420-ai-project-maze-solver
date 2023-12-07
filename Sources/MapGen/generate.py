# generate a map given width and height, with:
# 0: cell
# -1: wall
# A1: agent 1
# T1: target 1
# level 1: 1 floor, no key
# level 2: 1 floor, key Ki and Door Di
# level 3: n floor, key Ki and Door Di
import random

CELL = '0'
WALL = '-1'
AGENT = 'A1'
TARGET = 'T1'

# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore

## Functions

MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# Find number of surrounding cells
def surroundingCells(coord, width, height, maze):
    '''return the list of valid surrounding cells'''
    scells = []
    for i in MOVE:
        if (coord[0] + i[0] < 0 or coord[0] + i[0] >= height or coord[1] + i[1] < 0 or coord[1] + i[1] >= width):
            continue
        if (maze[coord[0] + i[0]][coord[1] + i[1]] != 'u'):
            continue
        scells.append([coord[0] + i[0], coord[1] + i[1]])
    return scells


def initialize(width, height, maze, value):
    '''initialize the maze with only value'''
    for i in range(height):
        maze[i] = [value] * width
    return maze


def create_map_lv1(width, height, maze):

    # initialize the maze with only 'u'
    maze = initialize(width, height, maze, 'u')
    
    # set a variable visited with all false
    consider = []
    
    # randomize starting point and set it a cell
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    
    consider.append([starting_height, starting_width])
    
    # pop cell from consider
    while (consider):
        # random between 1 and 2
        # num = 1
        # if num = 1 -> pop one cell from consider
        # if (num == 1):
            # pop until we find a cell that has not been visited
        current = consider.pop()
        # print(current)
        # if consider is empty, break
        maze[current[0]][current[1]] = CELL
        for i in surroundingCells(current, width, height, maze):
            if (maze[i[0]][i[1]] != 'u'):
                continue
            # randomize between 0 and 1
            if (random.random() <= 0.3):
                maze[i[0]][i[1]] = WALL
            else:
                consider.append(i)
    # assign the rest of walls
    for i in range(height):
        for j in range(width):
            if (maze[i][j] == 'u'):
                maze[i][j] = CELL
    return maze
    
        


def generate_map(width, height, level):
    # Check the map size
    if (width < 5 or height < 5):
        print("Width and height must be greater than 5")
        return

    # Check the level
    if (level < 1 or level > 3):
        print("Level must be in range [1, 3]")
        return

    # The maze
    maze = []

    # Create the default maze
    for i in range(height):
        maze.append([])
        for j in range(width):
            # randomize between cell and wall
            # if (random.random() <= 0.3):
            #     maze[i].append(WALL)
            # else:
            #     maze[i].append(CELL)
            maze[i].append('u')

    # # The list of walls
    # walls = []


    maze = create_map_lv1(width, height, maze)
    
    
    # randomize starting point and set it a cell
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    
    maze[starting_height][starting_width] = AGENT
    
    # find all cells that can be reached from starting point and the number of steps to reach them
    # use DFS to find all reachable cells
    reachable_cells = {}
    stack = []
    stack.append([starting_height, starting_width, 0])
    while (stack):
        # pop the min step cell
        index = stack.index(min(stack, key = lambda x: x[2]))
        current = stack.pop(index)
        # if current is visited, skip
        if ((current[0], current[1]) in reachable_cells):
            continue
        reachable_cells[(current[0], current[1])] = current[2]
        # add neighbors to stack
        if (current[0] > 0 and maze[current[0] - 1][current[1]] == CELL and (current[0] - 1, current[1]) not in reachable_cells):
            stack.append([current[0] - 1, current[1], current[2] + 1])
        if (current[0] < height - 1 and maze[current[0] + 1][current[1]] == CELL and (current[0] + 1, current[1]) not in reachable_cells):
            stack.append([current[0] + 1, current[1], current[2] + 1])
        if (current[1] > 0 and maze[current[0]][current[1] - 1] == CELL and (current[0], current[1] - 1) not in reachable_cells):
            stack.append([current[0], current[1] - 1, current[2] + 1])
        if (current[1] < width - 1 and maze[current[0]][current[1] + 1] == CELL and (current[0], current[1] + 1) not in reachable_cells):
            stack.append([current[0], current[1] + 1, current[2] + 1])
    
    # create target in a reachable cell with the longest path
    target_height = starting_height
    target_width = starting_width
    max_step = 0
    for key in reachable_cells:
        if (reachable_cells[key] > max_step):
            max_step = reachable_cells[key]
            target_height = key[0]
            target_width = key[1]
    
    # # make sure starting point and target point are not the same
    # while (target_height == starting_height and target_width == starting_width):
    #     target_height = int(random.random() * height)
    #     target_width = int(random.random() * width)
    # maze[starting_height][starting_width] = AGENT
    # maze[target_height][target_width] = TARGET
    maze[target_height][target_width] = TARGET
    if (level == 1):
        return maze

from colorama import Fore

def visualize(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            s = str(maze[i][j])
            if (len(s) == 1):
                s = ' ' + s
            if (maze[i][j] == WALL):
                print(Fore.RED + s, end=" ")
            elif (maze[i][j] == CELL):
                print(Fore.GREEN + s, end=" ")
            elif (maze[i][j] == AGENT):
                print(Fore.YELLOW + s, end=" ")
            elif (maze[i][j].startswith('K') or maze[i][j].startswith('D')):
                # base on the number of keys and doors
                print(Fore.BLUE + s, end=" ")                
            else:
                print(Fore.WHITE + s, end=" ")
        print('\n')


def export_maze(maze, path, level = 1):
    with open(path, 'w') as outfile:
        outfile.write(str(len(maze)) + ',' + str(len(maze[0])) + '\n')
        if (level == 1):
            outfile.write('[floor1]\n')
            for i in range(len(maze)):
                for j in range(len(maze[0])):
                    outfile.write(maze[i][j])
                    if (j < len(maze[0]) - 1):
                        outfile.write(',')
                outfile.write('\n')
        else: 
            raise Exception('Level not supported yet')

def load_maze(path):
    with open(path, 'r') as infile:
        line = infile.readline()
        line = line.strip().split(',')
        height = int(line[0])
        width = int(line[1])
        print(Fore.WHITE + '\nHeight: ' + str(height) + ' Width: ' + str(width) + '\n')
        # while the line is not empty
        while (True):
            readline = infile.readline()
            if (readline == ''):
                break
            if (readline != None):
                print(Fore.YELLOW + readline, end=" ")
            maze = []
            for i in range(height):
                line = infile.readline()
                line = line.strip().split(',')
                maze.append(line)
            visualize(maze)
        return maze
# export_maze(maze, 'Map/level1-tmp.txt')

# maze = load_maze('Map/level3/input1-level3.txt')
# visualize(maze)

import sys

if __name__ == '__main__':
    op = sys.argv[1]
    if (op == '-f'):
        folder = sys.argv[2]
        # list all files in folder
        import os
        files = os.listdir(folder)
        files.sort()
        for i in files: 
            if(i.endswith('.txt')):
                print(Fore.YELLOW + i)
                maze = load_maze(folder + '/' + i)
    elif (op == '-s'):
        file = sys.argv[2]
        print(Fore.YELLOW + file)
        maze = load_maze(file)