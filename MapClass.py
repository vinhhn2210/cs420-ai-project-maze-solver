import pygame
import CellClass
import Const

class Map:
	def __init__(self, mapSize, containerInfo):
		self.mapSize = mapSize
		self.mapCoord = (containerInfo[0] + (containerInfo[2] - self.mapSize[0]) / 2, containerInfo[1] + (containerInfo[3] - self.mapSize[1]) / 2)
		
		self.M, self.N = 10, 10
		self.mapList = [[0 for j in range(self.M)] for i in range(self.N)]

		cellSize = (self.mapSize[0] / self.N, self.mapSize[1] / self.M)

		# Create Image for Map
		self.mapImage = []
		for i in range(self.M):
			mapImageRow = []
			for j in range(self.N):
				mapImageRow.append(CellClass.EmptyCell(cellSize, (j * cellSize[0] + self.mapCoord[0], i * cellSize[1] + self.mapCoord[1]), (i, j)))
			self.mapImage.append(mapImageRow)

		# Create graph for Map
		for i in range(self.M):
			for j in range(self.N):
				for k in range(8):
					u = i + Const.CELL_MOVE[k][0]
					v = j + Const.CELL_MOVE[k][1]
					if u < 0 or u >= self.M or v < 0 or v >= self.N:
						continue

					curCell = self.getCell(i, j)
					nextCell = self.getCell(u, v)
					curCell.addAdj(nextCell, k)

	def getCell(self, i, j):
		return self.mapImage[i % self.M][j % self.N]

	def draw(self, gameScreen):
		for mapImageRow in self.mapImage:
			for cell in mapImageRow:
				cell.draw(gameScreen)
