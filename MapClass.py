import pygame
import CellClass
import Const

# Map Cell
'''
	0: empty
	-1: obstacle
	A1...91..2: agent color
	T1...9: chest 1...9
	K1...9: Key
	UP: up
	DO: down
'''
class Map:
	def __init__(self, mapLen, mapData, mapSize, containerInfo):
		self.mapSize = mapSize
		self.mapCoord = (containerInfo[0] + (containerInfo[2] - self.mapSize[0]) / 2, containerInfo[1] + (containerInfo[3] - self.mapSize[1]) / 2)
		
		self.M, self.N = (mapLen[0], mapLen[1])
		print(self.M, self.N)
		self.mapData = mapData

		cellSize = (self.mapSize[0] / self.N, self.mapSize[1] / self.M)

		# self.mapData = mapData

		# Create Image for Map
		self.mapImage = []
		for i in range(self.M):
			mapImageRow = []
			for j in range(self.N):
				if self.mapData[i][j] == "-1": 
					mapImageRow.append(CellClass.ObstacleCell(cellSize, (j * cellSize[0] + self.mapCoord[0], i * cellSize[1] + self.mapCoord[1]), (i, j)))
				else:
					mapImageRow.append(CellClass.EmptyCell(cellSize, (j * cellSize[0] + self.mapCoord[0], i * cellSize[1] + self.mapCoord[1]), (i, j)))

					if self.isChestCell(self.mapData[i][j]):
						mapImageRow[j].updateChest(int(self.mapData[i][j][1:]) - 1)

					if self.isDoorCell(self.mapData[i][j]):
						curDoor = self.mapData[i][j][1:]
						mapImageRow[j].updateDoor(int(curDoor) - 1)

			self.mapImage.append(mapImageRow)

		# Create graph for Map
		# for i in range(self.M):
		# 	for j in range(self.N):
		# 		for k in range(8):
		# 			u = i + Const.CELL_MOVE[k][0]
		# 			v = j + Const.CELL_MOVE[k][1]
		# 			if u < 0 or u >= self.M or v < 0 or v >= self.N:
		# 				continue

		# 			curCell = self.getCell(i, j)
		# 			nextCell = self.getCell(u, v)
		# 			curCell.addAdj(nextCell, k)

	def getCell(self, i, j):
		return self.mapImage[i % self.M][j % self.N]

	def draw(self, gameScreen):
		for mapImageRow in self.mapImage:
			for cell in mapImageRow:
				cell.draw(gameScreen)

	def isChestCell(self, ID):
		return ID[0:1] == 'T'

	def isDoorCell(self, ID):
		return ID[0:1] == 'D'

