import pygame
import Const
import random

class Cell:
	def __init__(self, cellSize, cellCoord, cellID):
		self.cellSize = cellSize
		self.cellCoord = cellCoord
		self.cellID = cellID

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

		# Properties
		self.itemPadding = cellSize[1] * 15 / 100

		self.chestSize = (cellSize[0] * 90 / 100, cellSize[1] * 120 / 100)
		self.chestCoord = self.getItemCoord(self.chestSize)

		self.doorSize = (cellSize[0] * 90 / 100, cellSize[1] * 120 / 100)
		self.doorCoord = self.getItemCoord(self.doorSize)

		self.keySize = (self.cellSize[0] * 4 / 10, self.cellSize[1] * 8 / 10)
		self.keyCoord = self.getItemCoord(self.keySize)

		self.fillColorPadding = (cellSize[0] * 10 / 100, cellSize[1] * 10 / 100)

		# Image
		self.image = [
			pygame.transform.scale(Const.CELL_IMAGE_LIST[i], cellSize) 
		for i in range(5)]

		self.chestImage = [
			pygame.transform.scale(Const.CELL_IMAGE_CHEST[i], self.chestSize) 
		for i in range(9)]

		self.keyImage = [
			pygame.transform.scale(Const.CELL_IMAGE_KEY[i], self.keySize) 
		for i in range(20)
		]

		self.doorImage = [
			pygame.transform.scale(Const.CELL_IMAGE_DOOR[i], self.doorSize) 
		for i in range(20)
		]

		self.stairUpImage = pygame.transform.scale(Const.CELL_IMAGE_STAIR_UP, self.cellSize) 
		self.stairDownImage = pygame.transform.scale(Const.CELL_IMAGE_STAIR_DOWN, self.cellSize) 

		self.supportKeyImage = pygame.transform.scale(Const.CELL_IMAGE_SUPPORTKEY, cellSize) 

		# Cell Type
		self.emptyID = random.randint(0, len(self.image) - 1)
		self.agentID = -1
		self.keyID = -1
		self.doorID = -1
		self.chestID = -1
		self.isStairUp = False
		self.isStairDown = False

	def getItemCoord(self, itemSize):
		itemCoord = (self.cellCoord[0] + (self.cellSize[0] - itemSize[0]) / 2, self.cellCoord[1] + self.cellSize[1] * 60 / 100 - itemSize[1])
		return itemCoord

	def updateAgent(self, agentID):
		self.agentID = agentID

	def updateChest(self, chestID):
		self.chestID = chestID

	def updateKey(self, keyID):
		self.keyID = keyID

	def updateDoor(self, doorID):
		self.doorID = doorID

	def updateStairUp(self):
		self.isStairUp = True

	def updateStairDown(self):
		self.isStairDown = True

	def draw(self, gameScreen):	
		gameScreen.blit(self.image[self.emptyID], self.cellCoord)

		if self.keyID != -1:
			gameScreen.blit(self.supportKeyImage, self.cellCoord)

		if self.agentID != -1:
			pygame.draw.rect(gameScreen, Const.COLOR_AGENT[self.agentID], pygame.Rect(self.cellCoord[0] + self.fillColorPadding[0], self.cellCoord[1] + self.fillColorPadding[1], self.cellSize[0] - 2 * self.fillColorPadding[0], self.cellSize[1] - 2 * self.fillColorPadding[1]))

		if self.keyID != -1:
			gameScreen.blit(self.keyImage[self.keyID], self.keyCoord)

		if self.doorID != -1:
			gameScreen.blit(self.doorImage[self.doorID], self.doorCoord)

		if self.chestID != -1:
			gameScreen.blit(self.chestImage[self.chestID], self.chestCoord)

		if self.isStairUp == True:
			gameScreen.blit(self.stairUpImage, self.cellCoord)

		if self.isStairDown == True:
			gameScreen.blit(self.stairDownImage, self.cellCoord)

class ObstacleCell(Cell):
	def __init__(self, cellSize, cellCoord, cellID):
		Cell.__init__(self, cellSize, cellCoord, cellID)

		self.image = pygame.transform.scale(Const.CELL_IMAGE_BLOCK, cellSize) 

	def draw(self, gameScreen):
		gameScreen.blit(self.image, self.cellCoord)

