import pygame
import Const
import PortalClass

class Agent:
	def __init__(self, agentID, curCell):
		self.agentID = agentID
		self.agentCell = curCell
		self.agentSize = (curCell.cellSize[0] * 4 / 7, curCell.cellSize[1] * 6 / 7)
		self.agentPadding = curCell.cellSize[1] * 10 / 100
		self.agentCoord = [curCell.cellCoord[0] + (curCell.cellSize[0] - self.agentSize[0]) / 2, curCell.cellCoord[1] + curCell.cellSize[1] / 2 + self.agentPadding - self.agentSize[1]]
		# self.agentCell.addPlayer(self.agentID)

		# Agent moving
		self.isMoving = False
		self.moveDirection = -1
		self.agentSpeed = 15

		# Agent Animation
		self.agentFrame = []
		for listFrame in Const.AGENT_FRAME_LIST:
			agentFrameList = []
			step = len(listFrame) // 4
			for i in range(self.agentID * step, self.agentID * step + step):
				frame = listFrame[i]
				agentFrameList.append(pygame.transform.scale(frame, self.agentSize))
			self.agentFrame.append(agentFrameList)

		# Agent frame
		self.animationDirection = 0
		self.curFrame = 0
		self.totalFrame = len(self.agentFrame[self.animationDirection])

		# Portal
		self.agentPortal = PortalClass.Portal(curCell)
		self.portalFrame = 10

	def getAgentCoordInCell(self, newCell):
		return (newCell.cellCoord[0] + (newCell.cellSize[0] - self.agentSize[0]) / 2, newCell.cellCoord[1] + newCell.cellSize[1] / 2 + self.agentPadding - self.agentSize[1])

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
		if(self.portalFrame > 0):
			self.agentPortal.draw(gameScreen)
			self.portalFrame -= 1
			return

		gameScreen.blit(self.agentFrame[0][self.curFrame], tuple(self.agentCoord))

		self.moveFrame()