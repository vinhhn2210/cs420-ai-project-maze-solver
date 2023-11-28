import pygame
import Const
import MapClass
import AgentClass
import json

class InGame:
	def __init__(self, jsonFile):
		# Init
		pygame.init()

		# Data for ingame
		self.totalFloor = 0
		self.curFloor = 0
		self.map = []
		self.mapSize = ()
		self.step = 0
		self.jsonData = []
		self.totalAgent = 0

		self.loadJsonFile(jsonFile)

		# Set up Game Window
		infoObject = pygame.display.Info()
		screenProportion = 1
		self.gameScreen = pygame.display.set_mode((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))
		pygame.display.set_caption("Move Your Step")
		pygame.display.flip()
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

		# Running
		self.running = True

		# Game background
		self.gameBackground = pygame.transform.scale(Const.INGAME_BACKGROUND, (self.screenWidth, self.screenHeight))
		self.gameScreen.blit(self.gameBackground, (0, 0))

		# Set up Map
		inGameContainer = (159 / 1000 * self.screenWidth, 51 / 562.71 * self.screenHeight, 542 / 1000 * self.screenWidth, 447 / 562.71 * self.screenHeight)

		self.gameMap = [MapClass.Map(self.mapSize, self.map[self.curFloor], (inGameContainer[2], inGameContainer[3]), inGameContainer) for i in range(self.totalFloor)]

		# Set up Clock
		self.clock = pygame.time.Clock()
		self.isEndGame = False
		self.initTick = pygame.time.get_ticks()
		self.stepTime = 0.5

		# Agent
		# self.agent1 = AgentClass.Agent(1, self.gameMap.getCell(1, 1))

		self.updateMap()

	def loadJsonFile(self, jsonFilePath):
		jsonFile = open(jsonFilePath)

		data = json.load(jsonFile)

		self.totalFloor = data["0"]["numFloor"]
		self.curFloor = data["0"]["floor"][0]
		self.mapSize = tuple(data["0"]["mapSize"])
		self.map = data["0"]["map"]
		self.totalAgent = data["0"]["numAgent"]

		self.jsonData = data

		jsonFile.close()

	def updateMap(self):
		for i in range(1, self.totalAgent + 1):
			tmpTuple = self.jsonData[str(self.step)]["agents"][str(i)]["position"]
			X, Y, Z = tmpTuple[0], tmpTuple[1], tmpTuple[2]

			if self.map[Z][X][Y] == f'A{i}':
				self.map[Z][X][Y] = f'A{i}0'
				self.gameMap[Z].getCell(X, Y).updateAgent(i)
			else:
				self.map[Z][X][Y] = f'A{i}'
				self.gameMap[Z].getCell(X, Y).updateAgent(i)


	def run(self):
		while self.running :
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			tick = pygame.time.get_ticks()
			if tick >= self.initTick + self.stepTime * 1000:
				self.step += 1
				self.initTick += self.stepTime * 1000

				if str(self.step) in self.jsonData:
					self.updateMap()
				else:
					self.isEndGame = True

			if self.isEndGame:
				print("End here")
				break

			# self.agent1.handleEvent()

			# Draw window
			self.gameScreen.blit(self.gameBackground, (0, 0))
			self.gameMap[self.curFloor].draw(self.gameScreen)

			pygame.display.update()


