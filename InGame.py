import pygame
import Const
import MapClass
import AgentClass
import LeaderboardClass
import json

class InGame:
	def __init__(self, menuData):
		# Init
		pygame.init()

		# Set up Game Window
		infoObject = pygame.display.Info()
		screenProportion = 1
		self.gameScreen = pygame.display.set_mode((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))
		pygame.display.set_caption("Move Your Step")
		pygame.display.flip()
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

		# Running
		self.running = True

		# Menu data
		jsonFilePath = 'Solution/input' + str(menuData[0]) + '-level' + str(menuData[1]) + '_' + menuData[2].lower() + '.json'
		self.menuData = menuData

		# Set up Map
		self.gameMap = []

		# Set up Agent
		self.agentList = []

		# Data for ingame
		self.totalFloor = 0
		self.curFloor = 0
		self.map = []
		self.mapSize = ()
		self.step = 0
		self.jsonData = []
		self.totalAgent = 0

		self.keyList = []

		self.loadJsonFile(jsonFilePath)

		# Game background
		self.gameBackground = pygame.transform.scale(Const.INGAME_BACKGROUND, (self.screenWidth, self.screenHeight))
		self.gameScreen.blit(self.gameBackground, (0, 0))

		# Set up Clock
		self.clock = pygame.time.Clock()
		self.isEndGame = False
		self.initTick = pygame.time.get_ticks()
		self.stepTime = 0.5

		self.updateMap()

	def loadJsonFile(self, jsonFilePath):
		jsonFile = open(jsonFilePath)

		data = json.load(jsonFile)

		# Initial Map
		self.totalFloor = data["0"]["numFloor"]
		self.curFloor = data["0"]["floor"][0]
		self.mapSize = tuple(data["0"]["mapSize"])
		self.map = data["0"]["map"]

		# Game Map
		inGameContainer = (159 / 1000 * self.screenWidth, 51 / 562.71 * self.screenHeight, 542 / 1000 * self.screenWidth, 447 / 562.71 * self.screenHeight)
		self.gameMap = [MapClass.Map(self.mapSize, self.map[self.curFloor], (inGameContainer[2], inGameContainer[3]), inGameContainer) for i in range(self.totalFloor)]

		# Initial Agent
		self.totalAgent = data["0"]["numAgent"]
		for i in range(1, self.totalAgent + 1):
			tmpTuple = data["0"]["agents"][str(i)]["position"]
			X, Y, Z = tmpTuple[0], tmpTuple[1], tmpTuple[2]

			self.agentList.append(AgentClass.Agent(i, self.gameMap[Z].getCell(X, Y)))

		# Initial Key
		self.keyList = data["0"]["key"]
		cnt = 0
		for i in self.keyList:
			self.gameMap[i[2]].getCell(i[0], i[1]).updateKey(cnt)
			cnt += 1

		# Json Data
		self.jsonData = data

		jsonFile.close()

	def updateMap(self):
		for i in range(1, self.totalAgent + 1):
			tmpTuple = self.jsonData[str(self.step)]["agents"][str(i)]["position"]
			X, Y, Z = tmpTuple[0], tmpTuple[1], tmpTuple[2]

			if self.map[Z][X][Y] == f'A{i}':
				self.map[Z][X][Y] = f'A{i}0'
				self.gameMap[Z].getCell(X, Y).updateAgent(i)
				self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))
			else:
				self.map[Z][X][Y] = f'A{i}'
				self.gameMap[Z].getCell(X, Y).updateAgent(i)
				self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))



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
				leaderboard = LeaderboardClass.Leaderboard(self.menuData)
				leaderboard.run()
				break

			# Draw window
			self.gameScreen.blit(self.gameBackground, (0, 0))
			self.gameMap[self.curFloor].draw(self.gameScreen)
			for i in self.agentList:
				i.draw(self.gameScreen)

			pygame.display.update()


