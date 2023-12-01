import pygame
import Const
import MapClass
import AgentClass
import TextClass
import LeaderboardClass
import ButtonClass
import MenuClass
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
		if menuData[1] == 4:
			self.gameBackground = pygame.transform.scale(Const.INGAME_BACKGROUND_LEVEL4, (self.screenWidth, self.screenHeight))
		self.gameScreen.blit(self.gameBackground, (0, 0))

		# Game Properties
		self.isPause = 0
		self.gamePropertiesContent = (762.51 / 1000 * self.screenWidth, 51 / 562.71 * self.screenHeight, 196 / 1000 * self.screenWidth, 152 / 562.71 * self.screenHeight)
		self.pauseButton = [
			ButtonClass.Button(
				(self.gamePropertiesContent[2] * 20 / 100, self.gamePropertiesContent[2] * 20 / 100),
				Const.PAUSE_BUTTON[i],
				(self.gamePropertiesContent[0], self.gamePropertiesContent[1], self.gamePropertiesContent[2] / 2, self.gamePropertiesContent[3] * 30 / 100)
			)
			for i in range(2)
		]
		self.menuButton = ButtonClass.Button(
			(self.gamePropertiesContent[2] * 20 / 100, self.gamePropertiesContent[2] * 20 / 100),
			Const.MENU_BUTTON,
			(self.gamePropertiesContent[0] + self.gamePropertiesContent[2] / 2, self.gamePropertiesContent[1], self.gamePropertiesContent[2] / 2, self.gamePropertiesContent[3] * 30 / 100)
		)

		textPadding = self.gamePropertiesContent[2] * 5 / 100 
		# Time Text
		self.timeText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			25,
			"Time: 10s",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 35 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 10 / 100)
		)
		# Time Text
		self.memoryText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			25,
			"Memory: 10MB",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 55 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 10 / 100)
		)
		# Time Text
		self.scoreText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			25,
			"Score: 10",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 75 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 10 / 100)
		)

		# Set up Clock
		self.clock = pygame.time.Clock()
		self.isEndGame = False
		self.initTick = pygame.time.get_ticks()
		self.stepTime = 0.3

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

	def pauseGame(self):
		while self.isPause == 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					exit(0)

			pauseState = self.pauseButton[0].isClicked(self.gameScreen)
			if pauseState == True:
				self.isPause = 1 - self.isPause	

			menuState = self.menuButton.isClicked(self.gameScreen)
			if menuState == True:
				menu = MenuClass.Menu((self.screenWidth, self.screenHeight))
				menu.run()
				self.run = False
				break		

		self.initTick = pygame.time.get_ticks()


	def run(self):
		while self.running :
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					break

			pauseState = self.pauseButton[0].isClicked(self.gameScreen)

			if pauseState == True:
				self.isPause = 1 - self.isPause
				self.pauseGame()

			menuState = self.menuButton.isClicked(self.gameScreen)
			if menuState == True:
				menu = MenuClass.Menu((self.screenWidth, self.screenHeight))
				menu.run()
				break

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
			self.pauseButton[0].draw(self.gameScreen)
			self.menuButton.draw(self.gameScreen)
			self.timeText.draw(self.gameScreen)
			self.memoryText.draw(self.gameScreen)
			self.scoreText.draw(self.gameScreen)
			self.gameMap[self.curFloor].draw(self.gameScreen)
			for i in self.agentList:
				i.draw(self.gameScreen)

			pygame.display.update()


