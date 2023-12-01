import pygame
import Const
import PortalClass

class Agent:
	def __init__(self, agentID, curCell):
		self.agentID = agentID
		self.agentCell = curCell
		self.agentSize = (curCell.cellSize[0] * 4 / 7, curCell.cellSize[1] * 7 / 7)
		self.agentPadding = curCell.cellSize[1] * 30 / 100
		self.agentCoord = self.getAgentCoord()

		# Agent moving
		self.moveDirection = -1
		self.agentSpeed = 15

		# Agent Animation
		self.agentFrame = [[
			pygame.transform.scale(Const.AGENT_FRAME_LIST[self.agentID - 1][i][j], self.agentSize)
				for j in range(len(Const.AGENT_FRAME_LIST[self.agentID - 1][i]))] 
			for i in range(len(Const.AGENT_FRAME_LIST[self.agentID - 1]))]

		for i in range(len(self.agentFrame)):
			for j in range(len(self.agentFrame[i])):
				self.agentFrame[i][j] = pygame.transform.scale(self.agentFrame[i][j], self.agentSize) 

		# Agent frame
		self.animationDirection = 1
		self.curFrame = 0
		self.totalFrame = len(self.agentFrame[self.animationDirection])

	def getAgentCoord(self):
		agentCoord = [self.agentCell.cellCoord[0] + (self.agentCell.cellSize[0] - self.agentSize[0]) / 2, self.agentCell.cellCoord[1] + self.agentCell.cellSize[1] * 60 / 100 - self.agentSize[1]]
		return agentCoord

	def getAgentCoordInCell(self, newCell):
		agentCoord = [self.agentCell.cellCoord[0] + (self.agentCell.cellSize[0] - self.agentSize[0]) / 2, self.agentCell.cellCoord[1] + self.agentCell.cellSize[1] * 60 / 100 - self.agentSize[1]]
		return agentCoord

	def moveAgent(self):
		targetPos = self.getAgentCoordInCell(self.agentCell)

		if self.agentCoord == targetPos:
			return

		for i in range(2):
			moveDistance = min(self.agentSpeed, abs(targetPos[i] - self.agentCoord[i]))
			if self.agentCoord[i] < targetPos[i]:
				self.agentCoord[i] += moveDistance
			elif self.agentCoord[i] > targetPos[i]:
				self.agentCoord[i] -= moveDistance

	def updateAgentCell(self, newCell):
		if newCell.cellID[0] > self.agentCell.cellID[0]:
			self.animationDirection = 1
		elif newCell.cellID[0] < self.agentCell.cellID[0]:
			self.animationDirection = 0

		self.agentCell = newCell

	def updateAgentInStair(self, newCell):
		self.agentCell = newCell
		# print(self.agentCell.cellID)
		self.agentCoord = self.getAgentCoord()
		# print(self.agentCoord)

	def changeCell(self, direction):
		if self.agentCell.listAdj[direction] is not None:
			self.agentCell = self.agentCell.listAdj[direction]

	def handleEvent(self):
		key = pygame.key.get_pressed()

		if key[pygame.K_UP]:
			self.changeCell(1)
		if key[pygame.K_DOWN]:
			self.changeCell(3)
		if key[pygame.K_LEFT]:
			self.changeCell(0)
		if key[pygame.K_RIGHT]:
			self.changeCell(2)

	def moveFrame(self):
		self.moveAgent()

		self.curFrame = (self.curFrame + 1) % self.totalFrame

	def draw(self, gameScreen):
		gameScreen.blit(self.agentFrame[self.animationDirection][self.curFrame], tuple(self.agentCoord))

		self.moveFrame()