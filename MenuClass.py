import pygame
import Const
import ObjectClass
import TextClass
import ButtonClass
import InGame

class Menu:
	def __init__(self):
		pygame.init()

		### Prepare data
		self.levelID = 1
		self.algorithmID = -1
		self.mapID = 1

		# Menu Screen
		infoObject = pygame.display.Info()
		screenProportion = 3 / 4
		self.gameScreen = pygame.display.set_mode((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		pygame.display.flip()
		pygame.display.set_caption("Move Your Step")

		print(self.screenWidth, self.screenHeight)

		# Run
		self.running = True
		self.clock = pygame.time.Clock()

		# Menu Background
		self.backgroundImage = pygame.transform.scale(Const.MENU_BACKGROUND, (self.screenWidth, self.screenHeight))

		# Content Box Container
		containerBoxContainer = (self.screenWidth * 614 / 1000, self.screenHeight * 58 / 563, self.screenWidth * 332 / 1000, self.screenHeight * 332 / 563)

		# Level Text
		self.levelText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			50,
			"LEVEL",
			(containerBoxContainer[0], containerBoxContainer[1], containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Level Dropbox
		self.levelDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 18 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Level ID
		self.levelIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			'Level ' + str(self.levelID),
			(self.levelDropbox.coord[0], self.levelDropbox.coord[1], self.levelDropbox.size[0], self.levelDropbox.size[1])
		)

		# Up Level Button
		self.upLevelButton = ButtonClass.Button(
			(self.levelDropbox.size[0] * 7.5 / 100, self.levelDropbox.size[1] * 25 / 100),
			Const.UP_BUTTON_IMAGE,
			(self.levelDropbox.coord[0] + self.levelDropbox.size[0] * 80 / 100, self.levelDropbox.coord[1], self.levelDropbox.size[0] * 20 / 100, self.levelDropbox.size[1] / 2)
		)

		# Down Level Button
		self.downLevelButton = ButtonClass.Button(
			(self.levelDropbox.size[0] * 7.5 / 100, self.levelDropbox.size[1] * 25 / 100),
			Const.DOWN_BUTTON_IMAGE,
			(self.levelDropbox.coord[0] + self.levelDropbox.size[0] * 80 / 100, self.levelDropbox.coord[1] + self.levelDropbox.size[1] / 2, self.levelDropbox.size[0] * 20 / 100, self.levelDropbox.size[1] / 2)
		)

		# Choose Algorithm
		algoTickCoord = (
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 45 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0] + containerBoxContainer[2] - containerBoxContainer[2] * 35 / 100, containerBoxContainer[1] + containerBoxContainer[3] * 45 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 58 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0] + containerBoxContainer[2] - containerBoxContainer[2] * 35 / 100, containerBoxContainer[1] + containerBoxContainer[3] * 58 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
		)
		self.algoTickButtonList = [[ButtonClass.Button(
			(self.screenWidth * 3 / 100, self.screenWidth * 3 / 100),
			Const.TICK_IMAGE[j],
			algoTickCoord[i]
		) for j in range(2)] for i in range(4)]

		# Algorithm Text
		self.algoTuple = ('BFS', 'DFS', 'UCS', 'A*')

		self.algoText = [TextClass.Text(
			Const.VCR_OSD_MONO_FONT,
			Const.WHITE,
			25,
			self.algoTuple[i],
			(self.algoTickButtonList[i][0].coord[0] + self.screenWidth * 1 / 100 + self.algoTickButtonList[i][0].size[0], self.algoTickButtonList[i][0].coord[1], 0, self.algoTickButtonList[i][0].size[1])
		) for i in range(4)]

		# Map Text
		self.mapText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			50,
			"MAP",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 60 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Map Dropbox
		self.mapDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 78 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Map ID
		self.mapIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			40,
			'Map ' + str(self.mapID),
			(self.mapDropbox.coord[0], self.mapDropbox.coord[1], self.mapDropbox.size[0], self.mapDropbox.size[1])
		)

		# Up Map Button
		self.upMapButton = ButtonClass.Button(
			(self.mapDropbox.size[0] * 7.5 / 100, self.mapDropbox.size[1] * 25 / 100),
			Const.UP_BUTTON_IMAGE,
			(self.mapDropbox.coord[0] + self.mapDropbox.size[0] * 80 / 100, self.mapDropbox.coord[1], self.mapDropbox.size[0] * 20 / 100, self.mapDropbox.size[1] / 2)
		)

		# Down Map Button
		self.downMapButton = ButtonClass.Button(
			(self.mapDropbox.size[0] * 7.5 / 100, self.mapDropbox.size[1] * 25 / 100),
			Const.DOWN_BUTTON_IMAGE,
			(self.mapDropbox.coord[0] + self.mapDropbox.size[0] * 80 / 100, self.mapDropbox.coord[1] + self.mapDropbox.size[1] / 2, self.mapDropbox.size[0] * 20 / 100, self.mapDropbox.size[1] / 2)
		)

		# Start Button
		self.startButton = ButtonClass.Button(
			(self.screenWidth * 15 / 100, self.screenHeight * 15 / 100),
			Const.START_BUTTON_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] + self.screenHeight * 3 / 100, containerBoxContainer[2], self.screenHeight - (containerBoxContainer[1] + containerBoxContainer[3]))
		)

	def run(self):
		while self.running:
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_presses = pygame.mouse.get_pressed()

			# Up, Down Level Process
			upLevelState = self.upLevelButton.isClicked(self.gameScreen)
			if upLevelState == True:
				self.levelID += 1
				self.levelIDText.changeTextContent('Level ' + str(self.levelID))

			downLevelState = self.downLevelButton.isClicked(self.gameScreen)
			if downLevelState == True:
				self.levelID -= 1
				self.levelIDText.changeTextContent('Level ' + str(self.levelID))

			# Up, Down Map Process
			upMapState = self.upMapButton.isClicked(self.gameScreen)
			if upMapState == True:
				self.mapID += 1
				self.mapIDText.changeTextContent('Map ' + str(self.mapID))

			downMapState = self.downMapButton.isClicked(self.gameScreen)
			if downMapState == True:
				self.mapID -= 1
				self.mapIDText.changeTextContent('Map ' + str(self.mapID))

			# Algorithm Process
			for i in range(4):
				algoState = self.algoTickButtonList[i][0].isClicked(self.gameScreen)
				if algoState == True:
					self.algorithmID = i

			# Start Button Process
			startButtonState = self.startButton.isClicked(self.gameScreen)

			if startButtonState == True:
				if self.algorithmID != -1:
					jsonFilePath = 'Solution/input' + str(self.mapID) + '-level' + str(self.levelID) + '_' + self.algoTuple[self.algorithmID].lower() + '.json'
					ingame = InGame.InGame(jsonFilePath)
					ingame.run()
					break

			# Draw Window
			self.gameScreen.blit(self.backgroundImage, (0, 0))
			self.levelText.draw(self.gameScreen)
			self.levelDropbox.draw(self.gameScreen)
			self.levelIDText.draw(self.gameScreen)
			self.upLevelButton.draw(self.gameScreen)
			self.downLevelButton.draw(self.gameScreen)
			for i in range(4):
				if self.algorithmID == i:
					self.algoTickButtonList[i][1].draw(self.gameScreen)
				else:
					self.algoTickButtonList[i][0].draw(self.gameScreen)
				self.algoText[i].drawLeftToRight(self.gameScreen)
			self.mapText.draw(self.gameScreen)
			self.mapDropbox.draw(self.gameScreen)
			self.mapIDText.draw(self.gameScreen)
			self.upMapButton.draw(self.gameScreen)
			self.downMapButton.draw(self.gameScreen)
			self.startButton.draw(self.gameScreen)

			pygame.display.update()
		