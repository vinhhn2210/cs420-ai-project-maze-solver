import pygame
import Const
import CellClass

class Portal():
	def __init__(self, curCell):
		self.portalCell = curCell
		self.portalCoord = self.portalCell.cellCoord
		self.portalSize = (self.portalCell.cellSize[0], self.portalCell.cellSize[1])

		self.portalFrame = []
		for frame in Const.PORTAL_FRAME_LIST:
			self.portalFrame.append(pygame.transform.scale(frame, self.portalSize))

		self.curFrame = 0
		self.numFrame = len(self.portalFrame)

	def draw(self, gameScreen):
		gameScreen.blit(self.portalFrame[self.curFrame], (self.portalCell.cellCoord[0] + (self.portalCell.cellSize[0] - self.portalSize[0]) / 2, self.portalCell.cellCoord[1] + (self.portalCell.cellSize[1] - self.portalSize[1]) / 2))
		self.curFrame = (self.curFrame + 1) % self.numFrame
		
