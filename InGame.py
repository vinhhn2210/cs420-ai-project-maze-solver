import pygame
import Const
import MapClass
import AgentClass
import TextClass
import LeaderboardClass
import ButtonClass
import MenuClass
import AgentPropertyClass
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
		algoName = menuData[2]
		if algoName == 'A*':
			algoName = "astar"
		jsonFilePath = 'Sources/Solution/input' + str(menuData[0]) + '-level' + str(menuData[1]) + '_' + algoName.lower() + '.json'
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
		# self.gameBackground = pygame.transform.scale(Const.INGAME_BACKGROUND, (self.screenWidth, self.screenHeight))
		# if menuData[1] == 4:
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
			20,
			"Time: 10s",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 35 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 5 / 100)
		)
		# Time Text
		self.memoryText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			"Memory: 10MB",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 50 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 5 / 100)
		)
		# Score Text
		self.scoreText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			"Step: 0",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 65 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 5 / 100)
		)
		# Score Text
		self.floorText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			"Floor: 1",
			(self.gamePropertiesContent[0] + textPadding, self.gamePropertiesContent[1] + self.gamePropertiesContent[3] * 80 / 100, self.gamePropertiesContent[2] - 2 * textPadding, self.gamePropertiesContent[3] * 5 / 100)
		)

		# Agent Property
		agentPropertyCoord = (763 / 1000 * self.screenWidth, 259 / 562.71 * self.screenHeight)
		agentPropertySize = (64 / 1000 * self.screenWidth, 73 / 562.71 * self.screenHeight)
		keyProperty = (24 / 1000 * self.screenWidth, 33 / 562.71 * self.screenHeight, 40 / 1000 * self.screenWidth, 40 / 562.71 * self.screenHeight)
		self.agentPropertyList = []
		scoreProperty = (17 / 1000 * self.screenWidth, 7 / 562.71 * self.screenHeight, 48 / 1000 * self.screenWidth, 17 / 562.71 * self.screenHeight)
		cnt = 0
		for i in range(3):
			for j in range(3):
				if cnt < self.totalAgent:
					cnt += 1
					curPropertyCoord = (agentPropertyCoord[0] + j * agentPropertySize[0], agentPropertyCoord[1] + i * agentPropertySize[1])
					curPropertyInfo = (curPropertyCoord[0], curPropertyCoord[1], agentPropertySize[0], agentPropertySize[1])
					self.agentPropertyList.append(AgentPropertyClass.AgentProperty(curPropertyInfo, cnt, keyProperty, [], scoreProperty))

		# Set up Clock
		self.clock = pygame.time.Clock()
		self.isEndGame = False
		self.initTick = pygame.time.get_ticks()
		self.stepTime = 10 / len(self.jsonData) * self.totalFloor
		# print(self.stepTime)

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
		self.gameMap = [MapClass.Map(self.mapSize, self.map[i], (inGameContainer[2], inGameContainer[3]), inGameContainer) for i in range(self.totalFloor)]

		# Initial Agent
		self.totalAgent = data["0"]["numAgent"]
		for i in range(1, self.totalAgent + 1):
			tmpTuple = data["0"]["agents"][str(i)]["position"]
			X, Y, Z = tmpTuple[0], tmpTuple[1], tmpTuple[2]

			self.agentList.append(AgentClass.Agent(i, self.gameMap[Z].getCell(X, Y)))

		# Initial Key
		self.keyList = data["0"]["key"]
		for i in self.keyList:
			self.gameMap[i[3]].getCell(i[1], i[2]).updateKey(i[0] - 1)

		# Json Data
		self.jsonData = data

		jsonFile.close()

	def updateMap(self):
		self.scoreText.changeTextContent(f"Step: {self.step}")
		self.floorText.changeTextContent(f'Floor: {self.curFloor + 1}')

		for i in range(1, self.totalAgent + 1):
			listKey = self.jsonData[str(self.step)]['agents'][str(i)]['key']
			self.agentPropertyList[i - 1].updateListKey(listKey)

		for i in range(1, self.totalAgent + 1):
			tmpTuple = self.jsonData[str(self.step)]["agents"][str(i)]["position"]
			X, Y, Z = tmpTuple[0], tmpTuple[1], tmpTuple[2]

			if self.step >= 1:
				preTuple = self.jsonData[str(self.step - 1)]["agents"][str(i)]["position"]
				A, B, C = preTuple[0], preTuple[1], preTuple[2]
				if Z != C:
					self.curFloor = Z
					# print(Z, X, Y)
					self.gameMap[Z].getCell(X, Y).updateAgent(i, 0)
					self.agentList[i - 1].updateAgentInStair(self.gameMap[Z].getCell(X, Y))
					continue

			if len(self.map[Z][X][Y]) < 3:
				self.map[Z][X][Y] = f'A{i}0'
				self.gameMap[Z].getCell(X, Y).updateAgent(i, 0)
				self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))
			else:
				if self.map[Z][X][Y][1] == str(i):
					deg = int(self.map[Z][X][Y][2:])
					self.map[Z][X][Y] = f'A{i}{deg + 1}'
					self.gameMap[Z].getCell(X, Y).updateAgent(i, deg + 1)
					self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))
				else:
					self.map[Z][X][Y] = f'A{i}0'
					self.gameMap[Z].getCell(X, Y).updateAgent(i, 0)
					self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))

			# if self.map[Z][X][Y][:] == f'A{i}':
			# 	self.map[Z][X][Y] = f'A{i}0'
			# 	self.gameMap[Z].getCell(X, Y).updateAgent(i)
			# 	self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))
			# else:
			# 	self.map[Z][X][Y] = f'A{i}0'
			# 	self.gameMap[Z].getCell(X, Y).updateAgent(i)
			# 	self.agentList[i - 1].updateAgentCell(self.gameMap[Z].getCell(X, Y))

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
				self.running = False
				break		

			self.pauseButton[self.isPause].draw(self.gameScreen)
			pygame.display.update()

		self.initTick = pygame.time.get_ticks()


	def run(self):
		while self.running :
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					exit(0)
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
			# 	else:
			# 		self.isEndGame = True

			# if self.isEndGame:
				# leaderboard = LeaderboardClass.Leaderboard(self.menuData)
				# leaderboard.run()
				# break

			# Draw window
			self.gameScreen.blit(self.gameBackground, (0, 0))
			self.pauseButton[self.isPause].draw(self.gameScreen)
			self.menuButton.draw(self.gameScreen)
			self.timeText.draw(self.gameScreen)
			self.memoryText.draw(self.gameScreen)
			self.scoreText.draw(self.gameScreen)
			self.floorText.draw(self.gameScreen)
			self.gameMap[self.curFloor].draw(self.gameScreen)
			for i in self.agentList:
				i.draw(self.gameScreen)
			for i in self.agentPropertyList:
				i.draw(self.gameScreen)

			pygame.display.update()


