import pygame
import Const
import random

class Cell:
	def __init__(self, cellSize, cellCoord, cellID):
		self.cellSize = cellSize
		self.cellCoord = cellCoord
		self.cellID = cellID
		self.listAdj = [None for i in range(8)]
		# self.playerSet = set()

	# def AddPlayer(self, playerId):
	# 	self.playerSet.add(playerId)

	# def RemovePlayer(self, playerId):
	# 	if playerId in self.playerSet:
	# 		self.playerSet.discard(playerId)

	def addAdj(self, adjCell, direction):
		if direction < 0 or direction > 7:
			return
		self.listAdj[direction] = adjCell

	def getAdj(self, direction):
		if direction < 0 or direction > 3:
			return None
		return self.listAdj[direction]

class EmptyCell(Cell):
	def __init__(self, cellSize, cellCoord, cellID):
		Cell.__init__(self, cellSize, cellCoord, cellID)

		self.image = [
			pygame.transform.scale(Const.CELL_IMAGE_LIST[i], cellSize) 
		for i in range(5)]

		self.chestID = -1

		self.chestImage = [
			pygame.transform.scale(Const.CELL_IMAGE_CHEST[i], cellSize) 
		for i in range(9)]

		self.agentID = -1
		self.emptyID = random.randint(0, 4)
		self.padding = (cellSize[0] * 10 / 100, cellSize[1] * 10 / 100)

	def updateAgent(self, agentID):
		self.agentID = agentID

	def updateChest(self, chestID):
		self.chestID = chestID

	def draw(self, gameScreen):	
		gameScreen.blit(self.image[self.emptyID], self.cellCoord)

		if self.agentID != -1:
			pygame.draw.rect(gameScreen, Const.COLOR_AGENT[self.agentID], pygame.Rect(self.cellCoord[0] + self.padding[0], self.cellCoord[1] + self.padding[1], self.cellSize[0] - 2 * self.padding[0], self.cellSize[1] - 2 * self.padding[1]))

		if self.chestID != -1:
			gameScreen.blit(self.chestImage[self.chestID], self.cellCoord)

class ObstacleCell(Cell):
	def __init__(self, cellSize, cellCoord, cellID):
		Cell.__init__(self, cellSize, cellCoord, cellID)

		self.image = pygame.transform.scale(Const.CELL_IMAGE_BLOCK, cellSize) 

	def draw(self, gameScreen):
		gameScreen.blit(self.image, self.cellCoord)

