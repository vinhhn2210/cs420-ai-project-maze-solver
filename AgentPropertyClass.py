import Const
import pygame
import TextClass

class AgentProperty:
	def __init__(self, containerInfo, agentID, keyInfo, listKey, scorePropertyInfo):
		self.size = (containerInfo[2], containerInfo[3])
		self.agentSize = (self.size[0] * 3 / 10, self.size[1] * 3 / 10)
		self.agentImage = pygame.transform.scale(Const.AGENT_AVA_LIST[agentID - 1], self.agentSize)
		self.agentCoord = (containerInfo[0] + (containerInfo[2] * 4 / 10 - self.agentSize[0]) / 2, containerInfo[1] + (containerInfo[3] - self.agentSize[1]) / 2 + containerInfo[3] / 10)
		self.keyInfo = (keyInfo[0] + containerInfo[0], keyInfo[1] + containerInfo[1], keyInfo[2], keyInfo[3])
		self.keySize = (self.keyInfo[2] / 5, self.keyInfo[3] / 4)
		self.scoreProperty = (scorePropertyInfo[0] + containerInfo[0], scorePropertyInfo[1] + containerInfo[1], scorePropertyInfo[2], scorePropertyInfo[3])
		self.scorePropertyText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			15,
			f"Agent: {agentID}",
			self.scoreProperty
		)
		self.keyImage = [pygame.transform.scale(Const.CELL_IMAGE_KEY[i], (self.keySize[0] * 6 / 10, self.keySize[1] * 8 / 10)) for i in range(0, 20)]
		self.listKey = listKey

	def updateListKey(self, listKey):
		self.listKey = listKey

	def updateScore(self, score):
		self.scorePropertyText.changeTextContent(score)

	def draw(self, gameScreen):
		gameScreen.blit(self.agentImage, self.agentCoord)
		self.scorePropertyText.drawLeftToRight(gameScreen)

		cnt = 0
		for i in range(4):
			for j in range(5):
				if cnt < len(self.listKey):
					gameScreen.blit(self.keyImage[self.listKey[cnt] - 1], (self.keyInfo[0] + self.keySize[0] * j, self.keyInfo[1] + self.keySize[1] * i))
					cnt += 1
				else:
					break