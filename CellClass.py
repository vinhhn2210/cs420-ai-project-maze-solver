import pygame
import Const

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
		for i in range(10)]

	def draw(self, gameScreen):
		gameScreen.blit(self.image[0], self.cellCoord)

class ObstacleCell(Cell):
	def __init__(self, cellSize, cellCoord, cellID):
		Cell.__init__(self, cellSize, cellCoord, cellID)

		self.image = [
			pygame.transform.scale(Const.CELL_IMAGE_LIST[i], cellSize) 
		for i in range(10, 11)]

	def draw(self, gameScreen):
		gameScreen.blit(self.image[0], self.cellCoord)

