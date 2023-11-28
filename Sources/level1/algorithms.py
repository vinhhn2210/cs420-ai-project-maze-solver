    
class MazerSolverLevel1:
    def __init__(self, mazer, nRow, mCol, nLayer = 1):
        self.mazer = mazer
        self.nRow = nRow
        self.mCol = mCol
        self.nLayer = nLayer
        self.key = 0
        self.dx = [-1, 0, 1, 0, -1, -1, 1, 1]
        self.dy = [0, 1, 0, -1, -1, 1, -1, 1]
    # check if the current position is inside the mazer

    def agentPosition(self, agentName):
        for layer in range(self.nLayer):
            for xCor in range(self.nRow):
                for yCor in range(self.mCol):
                    if self.mazer[layer][xCor][yCor] == agentName:
                        return (xCor, yCor, layer)

    def inside(self, xCor, yCor, layer):
        return (xCor >= 0 and xCor < self.nRow and yCor >= 0 
            and yCor < self.mCol and layer >= 0 and layer < self.nLayer)
    
    def canUnlock(self, door, key):
        return key & (1 << door) != 0

    def isValid(self, xCor, yCor, layer, key):
        if self.mazer[layer][xCor][yCor]== '-1':
            return False
        if len(self.mazer[layer][xCor][yCor]) > 1 and self.mazer[layer][xCor][yCor][0] == 'D':
            door = int(self.mazer[layer][xCor][yCor][1:])
            return self.canUnlock(door, key)
        return True
    
    # goal test
    def goalTest(self, state, goal):
        return state == goal
    
    # can move
    def canMove(self, xCor, yCor, layer, key):
        if not self.inside(xCor, yCor, layer) or not self.isValid(xCor, yCor, layer, key):
            return False
        return True
    # successor function
    def succesor(self, xCor, yCor, layer, key):
        succ = []
        for i in range(8):
            xNext = xCor + self.dx[i]
            yNext = yCor + self.dy[i]
            layerNext = layer
            keyNext = key
            if self.mazer[layer][xCor][yCor] == 'U':
                layerNext += 1
            elif self.mazer[layer][xCor][yCor] == 'D':
                layerNext -= 1
            if self.mazer[layer][xCor][yCor][0] == 'K':
                keyNext |= (1 << int(self.mazer[layer][xCor][yCor][1:]))
                
            if self.canMove(xNext, yNext, layerNext, keyNext) and self.isValid(xCor, yNext, layer, key) and self.isValid(xNext, yCor, layer, key):
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
    
    