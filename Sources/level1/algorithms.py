    
class MazerSolverLevel1:
    def __init__(self, mazer, nRow, mCol, nLayer = 1):
        self.mazer = mazer # 3D array (floor, row, col)
        self.nRow = nRow 
        self.mCol = mCol
        self.nLayer = nLayer # number of floor
        self.key = 0 # agent's key
        self.dx = [-1, 0, 1, 0, -1, -1, 1, 1] # x direction
        self.dy = [0, 1, 0, -1, -1, 1, -1, 1] # y direction
        self.agentPos = {} # agent's position
        self.goalPos = {} # goal's position
        self.keyPos = {} # key's position
        self.doorPos = {} # door's position
        self.upFloor = {} # up floor's position
        self.downFloor = {} # down floor's position
        for layer in range(self.nLayer):
            for xCor in range(self.nRow):
                for yCor in range(self.mCol):
                    value = self.mazer[layer][xCor][yCor]
                    if self.mazer[layer][xCor][yCor][0] == 'A':
                        self.agentPos[value] = (xCor, yCor, layer)
                    elif self.mazer[layer][xCor][yCor][0] == 'T':
                        self.goalPos[value] = (xCor, yCor, layer)
                    elif len(self.mazer[layer][xCor][yCor]) > 1 and self.mazer[layer][xCor][yCor][0] == 'K':
                        self.keyPos[value] = (xCor, yCor, layer)
                    elif len(self.mazer[layer][xCor][yCor]) > 1 and self.mazer[layer][xCor][yCor][0] == 'D' and self.mazer[layer][xCor][yCor][1] != 'O':
                        self.doorPos[value] = (xCor, yCor, layer)
                    elif self.mazer[layer][xCor][yCor][0] == 'U':
                        self.upFloor[layer] = (xCor, yCor, layer)
                    elif self.mazer[layer][xCor][yCor] == 'DO':
                        self.downFloor[layer] = (xCor, yCor, layer)

    def agentPosition(self, agentName):
        ''' return agent's position'''
        return self.agentPos[agentName]
    def goalPosition(self, goalName):
        ''' return goal's position'''
        return self.goalPos[goalName]
    def keyPosition(self, keyName):
        ''' return key's position'''
        return self.keyPos[keyName]
    def doorPosition(self, doorName):
        ''' return door's position'''
        return self.doorPos[doorName]
    def upFloorPosition(self, floor):
        ''' return up floor's position'''
        return self.upFloor[floor]
    def downFloorPosition(self, floor):
        ''' return down floor's position'''
        return self.downFloor[floor]
    
    def inside(self, xCor, yCor, layer):
        ''' check if position is inside the maze'''
        return (xCor >= 0 and xCor < self.nRow and yCor >= 0 
            and yCor < self.mCol and layer >= 0 and layer < self.nLayer)
    
    def canUnlock(self, door, key):
        ''' check if agent can unlock the door'''
        return key & (1 << door) != 0

    def isValid(self, xCor, yCor, layer, key):
        ''' check if cell is blocked or locked door'''
        if self.mazer[layer][xCor][yCor]== '-1':
            return False
        if len(self.mazer[layer][xCor][yCor]) > 1 and self.mazer[layer][xCor][yCor][0] == 'D' and self.mazer[layer][xCor][yCor][1] != 'O':
            door = int(self.mazer[layer][xCor][yCor][1:])
            return self.canUnlock(door, key)
        return True
    
    def goalTest(self, state, goal):
        ''' check if agent reach the goal'''
        return state == goal
    
    # can move
    def canMove(self, xCor, yCor, layer, key):
        ''' check if agent can travel to the cell'''
        if not self.inside(xCor, yCor, layer) or not self.isValid(xCor, yCor, layer, key):
            return False
        return True

    # successor function
    def succesor(self, xCor, yCor, layer, key):
        ''' return a list of successor and their key'''
        succ = []
        for i in range(8):
            xNext = xCor + self.dx[i]
            yNext = yCor + self.dy[i]
            layerNext = layer
            keyNext = key
            if self.inside(xNext, yNext, layer) and self.mazer[layerNext][xNext][yNext] == 'UP':
                layerNext += 1
                xNext, yNext, layerNext = self.downFloorPosition(layerNext)
                succ.append((xNext, yNext, layerNext, keyNext))
            elif self.inside(xNext, yNext, layer) and self.mazer[layerNext][xNext][yNext] == 'DO':
                layerNext -= 1
                xNext, yNext, layerNext = self.upFloorPosition(layerNext)
                succ.append((xNext, yNext, layerNext, keyNext))
    
            elif self.canMove(xNext, yNext, layerNext, keyNext) and self.isValid(xCor, yNext, layer, key) and self.isValid(xNext, yCor, layer, key):
                succ.append((xNext, yNext, layerNext, keyNext))
        return succ

    # dfs algorithm to solve mazer 
    def dfs(self, start, goal, key = 0):
        visited = dict()
        stack = [start + (key, )]
        visited[start + (key, )] = None
        solution = False
        while stack:
            xCor, yCor, layer, key = stack.pop()
            if self.goalTest((xCor, yCor, layer), goal):
                solution = True
                break
            for xNext, yNext, layerNext, keyNext in self.succesor(xCor, yCor, layer, key):
                if (xNext, yNext, layerNext, keyNext) not in visited:
                    visited[(xNext, yNext, layerNext, keyNext)] = (xCor, yCor, layer, key)
                    stack.append((xNext, yNext, layerNext, keyNext))
        
        if solution:
            path = []
            current = goal + (key, )
            while current:
                path.append(current)
                current = visited[current]
            path.reverse()
            return path
        else:
            return None
        
    def bfs(self, start, goal, key = 0):
        visited = dict()
        queue = [start + (key, )]
        visited[start + (key, )] = None
        solution = False
        while queue:
            xCor, yCor, layer, key = queue.pop(0)
            if self.goalTest((xCor, yCor, layer), goal):
                solution = True
                break
            for xNext, yNext, layerNext, keyNext in self.succesor(xCor, yCor, layer, key):
                if (xNext, yNext, layerNext, keyNext) not in visited:
                    visited[(xNext, yNext, layerNext, keyNext)] = (xCor, yCor, layer, key)
                    queue.append((xNext, yNext, layerNext, keyNext))
        
        if solution:
            path = []
            current = goal + (key, )
            while current:
                path.append(current)
                current = visited[current]
            path.reverse()
            return path
        else:
            return None
    
    