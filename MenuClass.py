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
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		pygame.display.flip()
		pygame.display.set_caption("Move Your Step")

		print(self.screenWidth, self.screenHeight)

		# Run
		self.running = True
		self.clock = pygame.time.Clock()

		# Menu Background
		self.backgroundImage = pygame.transform.scale(Const.MENU_BACKGROUND, (self.screenWidth, self.screenHeight))

		# Logo Image
		self.logoObject = ObjectClass.Object(
			(self.screenWidth * 30 / 100, self.screenHeight * 40 / 100),
			Const.LOGO_IMAGE,
			(0, 0, self.screenWidth / 2, self.screenHeight)
		)

		# Level Text
		self.levelText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			70,
			"LEVEL",
			(self.screenWidth / 2, self.screenHeight * 7 / 100, self.screenWidth / 2, self.screenHeight * 10 / 100)
		)

		# Level Dropbox
		self.levelDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(self.screenWidth / 2, self.screenHeight * 20 / 100, self.screenWidth / 2, self.screenHeight * 10 / 100)
		)

		# Level ID
		self.levelIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			40,
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
			(self.screenWidth / 2, self.screenHeight * 35 / 100, self.screenWidth / 4, self.screenHeight * 10 / 100),
			(self.screenWidth * 3 / 4, self.screenHeight * 35 / 100, self.screenWidth / 4, self.screenHeight * 10 / 100),
			(self.screenWidth / 2, self.screenHeight * 45 / 100, self.screenWidth / 4, self.screenHeight * 10 / 100),
			(self.screenWidth * 3 / 4, self.screenHeight * 45 / 100, self.screenWidth / 4, self.screenHeight * 10 / 100),
		)
		self.algoTickButtonList = [[ButtonClass.Button(
			(self.screenWidth * 4 / 100, self.screenWidth * 4 / 100),
			Const.TICK_IMAGE[j],
			algoTickCoord[i]
		) for j in range(2)] for i in range(4)]

		# Algorithm Text
		algoTuple = ('BFS', 'DFS', 'UCS', 'A*')

		self.algoText = [TextClass.Text(
			Const.VCR_OSD_MONO_FONT,
			Const.WHITE,
			30,
			algoTuple[i],
			(self.algoTickButtonList[i][0].coord[0] + self.screenWidth * 1 / 100 + self.algoTickButtonList[i][0].size[0], self.algoTickButtonList[i][0].coord[1], 0, self.algoTickButtonList[i][0].size[1])
		) for i in range(4)]

		# Map Text
		self.mapText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			70,
			"MAP",
			(self.screenWidth / 2, self.screenHeight * 55 / 100, self.screenWidth / 2, self.screenHeight * 10 / 100)
		)

		# Map Dropbox
		self.mapDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(self.screenWidth / 2, self.screenHeight * 67 / 100, self.screenWidth / 2, self.screenHeight * 10 / 100)
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
			(self.screenWidth * 15 / 100, self.screenHeight * 12 / 100),
			Const.START_BUTTON_IMAGE,
			(self.screenWidth / 2, self.screenHeight * 85 / 100, self.screenWidth / 2, self.screenHeight * 10 / 100)
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
					ingame = InGame.InGame()
					ingame.run()
					break

			# Draw Window
			self.gameScreen.blit(self.backgroundImage, (0, 0))
			self.logoObject.draw(self.gameScreen)
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
		