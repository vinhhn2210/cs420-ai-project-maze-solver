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


# Find number of surrounding cells
def surroundingCells(rand_wall, maze):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == CELL):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == CELL):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == CELL):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == CELL):
		s_cells += 1

	return s_cells


def create_map_lv1(width, height, maze):

    # Randomize starting point and set it a cell
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height-1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width-1):
        starting_width -= 1

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = CELL
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height-1][starting_width] = WALL
    maze[starting_height][starting_width - 1] = WALL
    maze[starting_height][starting_width + 1] = WALL
    maze[starting_height + 1][starting_width] = WALL

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == CELL):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall, maze)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])


                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == CELL):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == CELL):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL

                    # Mark the new walls
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]-1] = WALL
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == CELL):

                s_cells = surroundingCells(rand_wall, maze)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = CELL

                    # Mark the new walls
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != CELL):
                            maze[rand_wall[0]][rand_wall[1]+1] = WALL
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]+1][rand_wall[1]] = WALL
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != CELL):
                            maze[rand_wall[0]-1][rand_wall[1]] = WALL
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
        


    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = WALL

    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == CELL):
            maze[0][i] = CELL
            break

    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == CELL):
            maze[height-1][i] = CELL
            break
        
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
        current = stack.pop()
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

maze = generate_map(20, 20, 1)
visualize(maze)

# export_maze(maze, 'Map/input4-level1.txt')