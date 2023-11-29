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
		self.itemPadding = cellSize[1] * 15 / 100

		self.chestSize = (cellSize[0] * 80 / 100, cellSize[1] * 100 / 100)
		self.chestImage = [
			pygame.transform.scale(Const.CELL_IMAGE_CHEST[i], self.chestSize) 
		for i in range(9)]
		self.chestCoord = [self.cellCoord[0] + (self.cellSize[0] - self.chestSize[0]) / 2, self.cellCoord[1] + self.cellSize[1] / 2 + self.itemPadding - self.chestSize[1]]

		self.keyImage = [
			pygame.transform.scale(Const.CELL_IMAGE_KEY[i], cellSize) 
		for i in range(20)
		]

		self.supportKeyImage = pygame.transform.scale(Const.CELL_IMAGE_SUPPORTKEY, cellSize) 

		self.doorImage = [
			pygame.transform.scale(Const.CELL_IMAGE_DOOR[i], cellSize) 
		for i in range(20)
		]

		# Cell Type
		self.agentID = -1
		self.keyID = -1
		self.doorID = -1

		self.emptyID = random.randint(0, 4)
		self.padding = (cellSize[0] * 10 / 100, cellSize[1] * 10 / 100)

	def updateAgent(self, agentID):
		self.agentID = agentID

	def updateChest(self, chestID):
		self.chestID = chestID

	def updateKey(self, keyID):
		self.keyID = keyID

	def updateDoor(self, doorID):
		self.doorID = doorID

	def draw(self, gameScreen):	
		gameScreen.blit(self.image[self.emptyID], self.cellCoord)

		if self.keyID != -1:
			gameScreen.blit(self.supportKeyImage, self.cellCoord)
			gameScreen.blit(self.keyImage[self.keyID], (self.cellCoord[0] , self.cellCoord[1]))

		if self.agentID != -1:
			pygame.draw.rect(gameScreen, Const.COLOR_AGENT[self.agentID], pygame.Rect(self.cellCoord[0] + self.padding[0], self.cellCoord[1] + self.padding[1], self.cellSize[0] - 2 * self.padding[0], self.cellSize[1] - 2 * self.padding[1]))

		if self.keyID != -1:
			gameScreen.blit(self.keyImage[self.keyID], (self.cellCoord[0] , self.cellCoord[1]))

		if self.doorID != -1:
			gameScreen.blit(self.doorImage[self.doorID], (self.cellCoord[0] , self.cellCoord[1] - self.itemPadding))

		if self.chestID != -1:
			gameScreen.blit(self.chestImage[self.chestID], self.chestCoord)

class ObstacleCell(Cell):
	def __init__(self, cellSize, cellCoord, cellID):
		Cell.__init__(self, cellSize, cellCoord, cellID)

		self.image = pygame.transform.scale(Const.CELL_IMAGE_BLOCK, cellSize) 

	def draw(self, gameScreen):
		gameScreen.blit(self.image, self.cellCoord)

