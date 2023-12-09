import math
from queue import PriorityQueue

class MazerSolverLevel1:
    def __init__(self, mazer, nRow, mCol, n0 = 1):
        self.mazer = mazer # 3D array (floor, row, col)
        self.nRow = nRow 
        self.mCol = mCol
        self.n0 = n0 # number of floor
        self.dx = [-1, 0, 1, 0, -1, -1, 1, 1] # x direction
        self.dy = [0, 1, 0, -1, -1, 1, -1, 1] # y direction
        for xCor in range(self.nRow):
            for yCor in range(self.mCol):
                if self.mazer[0][xCor][yCor][0] == 'A':
                    self.agentPos = (xCor, yCor, 0)
                elif self.mazer[0][xCor][yCor][0] == 'T':
                    self.goalPos = (xCor, yCor, 0)

    def agentPosition(self, agentName):
        ''' return agent's position'''
        return self.agentPos
    def goalPosition(self, goalName):
        ''' return goal's position'''
        return self.goalPos
    def keyPosition(self, keyName):
        ''' return key's position'''
        return self.keyPos[keyName]
    def doorPosition(self, doorName):
        ''' return door's position'''
        return self.doorPos[doorName]
    
    def inside(self, xCor, yCor):
        ''' check if position is inside the maze'''
        return (xCor >= 0 and xCor < self.nRow and yCor >= 0 
            and yCor < self.mCol)
    
    def isValid(self, xCor, yCor):
        ''' check if cell is blocked'''
        if self.mazer[0][xCor][yCor]== '-1':
            return False
        return True
    
    def goalTest(self, state, goal):
        ''' check if agent reach the goal'''
        return state == goal
    
    # can move
    def canMove(self, xCor, yCor):
        ''' check if agent can travel to the cell'''
        if not self.inside(xCor, yCor) or not self.isValid(xCor, yCor):
            return False
        return True

    # successor function
    def succesor(self, xCor, yCor):
        ''' return a list of successor'''
        succ = []
        for i in range(8):
            xNext = xCor + self.dx[i]
            yNext = yCor + self.dy[i]
            # move to cell
            if self.canMove(xNext, yNext) and self.isValid(xCor, yNext) and self.isValid(xNext, yCor):
                succ.append((xNext, yNext, 0))
        return succ

    # dfs algorithm to solve mazer 
    def dfs(self, start, goal):
        visited = dict()
        stack = [start]
        visited[start] = None
        solution = False
        while stack:
            xCor, yCor, layer = stack.pop()
            if self.goalTest((xCor, yCor, 0), goal):
                solution = True
                break
            for xNext, yNext, layer in self.succesor(xCor, yCor):
                if (xNext, yNext, 0) not in visited:
                    visited[(xNext, yNext, 0)] = (xCor, yCor, 0)
                    stack.append((xNext, yNext, 0))
        
        if solution:
            path = []
            current = goal
            while current:
                path.append(current + (0, ))
                current = visited[current]
            path.reverse()
            return [path]
        else:
            return None
        
    def bfs(self, start, goal, key = 0):
        visited = dict()
        queue = [start]
        visited[start] = None
        solution = False
        while queue:
            xCor, yCor, layer = queue.pop(0)
            if self.goalTest((xCor, yCor, 0), goal):
                solution = True
                break
            for xNext, yNext, layer in self.succesor(xCor, yCor):
                if (xNext, yNext, 0) not in visited:
                    visited[(xNext, yNext, 0)] = (xCor, yCor, 0)
                    queue.append((xNext, yNext, 0))
        
        if solution:
            path = []
            current = goal
            while current:
                path.append(current + (0, ))
                current = visited[current]
            path.reverse()
            return [path]
        else:
            return None
        
    def getHeuristicFunction(self, state, goal):
        xCor, yCor, layer = state
        goalX, goalY, layer = goal 
        return max(abs(xCor - goalX), abs(yCor - goalY))

    
    def astar(self, start, goal):
        visited = {}
        visited[start] = None

        g = {}
        g[start] = 0

        f = {}
        f[start] = self.getHeuristicFunction(start, goal)

        solution = False
        q = PriorityQueue()
        q.put((f[start], start))

        while q.empty() == False:
            curF, curState = q.get()
            xCor, yCor, layer = curState

            if curF != f[curState]:
                continue

            curG = g[curState]

            if self.goalTest((xCor, yCor, 0), goal):
                solution = True
                break

            for xNext, yNext, layer in self.succesor(xCor, yCor):
                if (xNext, yNext, 0) not in g or g[(xNext, yNext, 0)] > curG + 1:
                    visited[(xNext, yNext, 0)] = (xCor, yCor, 0)
                    g[(xNext, yNext, 0)] = curG + 1
                    f[(xNext, yNext, 0)] = curG + 1 + self.getHeuristicFunction((xNext, yNext, 0), goal)
                    q.put((f[(xNext, yNext, 0)], (xNext, yNext, 0)))

        if solution:
            path = []
            current = goal
            while current:
                path.append(current + (0, ))
                current = visited[current]
            path.reverse()
            return [path]
        else:
            return None

    def ucs(self, start, goal):
        visited = {}
        visited[start] = None
        
        g = {}
        g[start] = 0
        
        solution = False
        q = PriorityQueue()
        q.put((g[start], start))

        while q.empty() == False:
            curF, curState = q.get()
            xCor, yCor, layer = curState

            if curF != g[curState]:
                continue

            curG = g[curState]

            if self.goalTest((xCor, yCor, 0), goal):
                solution = True
                break

            for xNext, yNext, layer in self.succesor(xCor, yCor):
                if (xNext, yNext, 0) not in g or g[(xNext, yNext, 0)] > curG + 1:
                    visited[(xNext, yNext, 0)] = (xCor, yCor, 0)
                    g[(xNext, yNext, 0)] = curG + 1
                    q.put((g[(xNext, yNext, 0)], (xNext, yNext, 0)))

        if solution:
            path = []
            current = goal
            while current:
                path.append(current + (0, ))
                current = visited[current]
            path.reverse()
            return [path]
        else:
            return None


    
