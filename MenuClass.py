import pygame
import Const
import ObjectClass
import TextClass
import ButtonClass
import InGame
import sys
sys.path.append('Sources')
import system

from tkinter import filedialog

def openFileDialog():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        return file_path
    return None

class Menu:
	def __init__(self, screenSize):
		pygame.init()

		### Prepare data
		self.levelID = 1
		self.algorithmID = -1
		self.mapID = 1

		# Menu Screen
		self.gameScreen = pygame.display.set_mode(screenSize)
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		pygame.display.flip()
		pygame.display.set_caption("Move Your Step")

		# print(self.screenWidth, self.screenHeight)

		# Run
		self.running = True
		self.clock = pygame.time.Clock()

		# Menu Background
		self.backgroundImage = pygame.transform.scale(Const.MENU_BACKGROUND, (self.screenWidth, self.screenHeight))
		self.importMapBackGround = ObjectClass.Object(
			(self.screenWidth * 3.5 / 10, self.screenHeight * 6 / 10),
			Const.IMPORT_MAP_BACKGROUND,
			(0, 0, self.screenWidth, self.screenHeight)
		)

		# Content Box Container
		containerBoxContainer = (self.screenWidth * 614 / 1000, self.screenHeight * 58 / 563, self.screenWidth * 332 / 1000, self.screenHeight * 332 / 563)

		# Level Text
		self.levelText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			45,
			"LEVEL",
			(containerBoxContainer[0], containerBoxContainer[1], containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Level Dropbox
		self.levelDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 14 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Level ID
		self.levelIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
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
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 39 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0] + containerBoxContainer[2] - containerBoxContainer[2] * 35 / 100, containerBoxContainer[1] + containerBoxContainer[3] * 39 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 52 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
			(containerBoxContainer[0] + containerBoxContainer[2] - containerBoxContainer[2] * 35 / 100, containerBoxContainer[1] + containerBoxContainer[3] * 52 / 100, containerBoxContainer[2] * 20 / 100, containerBoxContainer[1] * 15 / 100),
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
			Const.BROWN,
			25,
			self.algoTuple[i],
			(self.algoTickButtonList[i][0].coord[0] + self.screenWidth * 1 / 100 + self.algoTickButtonList[i][0].size[0], self.algoTickButtonList[i][0].coord[1], 0, self.algoTickButtonList[i][0].size[1])
		) for i in range(4)]

		# Map Text
		self.mapText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			45,
			"MAP",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 53 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Map Dropbox
		self.mapDropbox = ObjectClass.Object(
			(self.screenWidth * 25 / 100, self.screenHeight * 10 / 100),
			Const.DROPBOX_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 66 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100)
		)

		# Map ID
		self.mapIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
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

		# Import Map Button
		self.importMapButton = ButtonClass.Button(
			(self.screenWidth * 15 / 100, self.screenHeight * 6 / 100),
			Const.IMPORT_BUTTON_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 83 / 100, containerBoxContainer[2], containerBoxContainer[3] * 20 / 100),
		)
		self.importMapText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			25,
			'Import Map',
			(self.importMapButton.coord[0], self.importMapButton.coord[1], self.importMapButton.size[0], self.importMapButton.size[1])
		)

		# Start Button
		self.startButton = ButtonClass.Button(
			(self.screenWidth * 15 / 100, self.screenHeight * 15 / 100),
			Const.START_BUTTON_IMAGE,
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] + self.screenHeight * 3 / 100, containerBoxContainer[2], self.screenHeight - (containerBoxContainer[1] + containerBoxContainer[3]))
		)

	def importMapScreen(self):
		importCoord = self.importMapBackGround.coord
		importSize = self.importMapBackGround.size

		levelID = 1

		# Import Map Text
		importText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			35,
			"Import Map",
			(importCoord[0], importCoord[1] + importSize[1] * 12 / 100, importSize[0], importSize[1] * 15 / 100)
		)

		# FileDiagog Button
		fileDialogButton = ButtonClass.Button(
			(importSize[0] * 30 / 100, importSize[1] * 12 / 100),
			Const.DROPBOX_IMAGE,
			(importCoord[0], importCoord[1] + importSize[1] * 27 / 100, importSize[0], importSize[1] * 15 / 100)
		)
		fileDialogText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			'File Dialog',
			(fileDialogButton.coord[0], fileDialogButton.coord[1], fileDialogButton.size[0], fileDialogButton.size[1])
		)

		# Level Dropbox
		levelDropbox = ObjectClass.Object(
			(importSize[0] * 40 / 100, importSize[1] * 12 / 100),
			Const.DROPBOX_IMAGE,
			(importCoord[0], importCoord[1] + importSize[1] * 40 / 100, importSize[0], importSize[1] * 20 / 100)
		)

		# Level ID
		levelIDText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			'Level ' + str(levelID),
			(levelDropbox.coord[0], levelDropbox.coord[1], levelDropbox.size[0], levelDropbox.size[1])
		)

		# Up Level Button
		upLevelButton = ButtonClass.Button(
			(levelDropbox.size[0] * 7.5 / 100, levelDropbox.size[1] * 25 / 100),
			Const.UP_BUTTON_IMAGE,
			(levelDropbox.coord[0] + levelDropbox.size[0] * 80 / 100, levelDropbox.coord[1], levelDropbox.size[0] * 20 / 100, levelDropbox.size[1] / 2)
		)

		# Down Level Button
		downLevelButton = ButtonClass.Button(
			(levelDropbox.size[0] * 7.5 / 100, levelDropbox.size[1] * 25 / 100),
			Const.DOWN_BUTTON_IMAGE,
			(levelDropbox.coord[0] + levelDropbox.size[0] * 80 / 100, levelDropbox.coord[1] + levelDropbox.size[1] / 2, levelDropbox.size[0] * 20 / 100, levelDropbox.size[1] / 2)
		)

		algoList = ['BFS', 'DFS', 'UCS', 'A*']
		algoID = -1
		algoCoord = (importCoord[0] + importSize[0] * 10 / 100, importCoord[1] + importSize[1] * 60 / 100)
		algoSize = ((importSize[0] - importSize[0] * 20 / 100) / 4, importSize[1] * 8 / 100)
		algoButton = []
		algoText = []
		for i in range(4):	
			tmpAlgo = ButtonClass.Button(
				(algoSize[0] * 70 / 100, algoSize[1]),
				Const.DROPBOX_IMAGE,
				(algoCoord[0] + i * algoSize[0], algoCoord[1], algoSize[0], algoSize[1])
			)
			# Level ID
			tmpAlgoText = TextClass.Text(
				Const.AMATICSC_FONT,
				Const.BROWN,
				15,
				algoList[i],
				(tmpAlgo.coord[0], tmpAlgo.coord[1], tmpAlgo.size[0], tmpAlgo.size[1])
			)
			algoButton.append(tmpAlgo)
			algoText.append(tmpAlgoText)

		# Start Button
		startButton = ButtonClass.Button(
			(importSize[0] * 15 / 100, importSize[1] * 9 / 100),
			Const.START_BUTTON_IMAGE,
			(importCoord[0], importCoord[1] + importSize[1] * 7 / 10, importSize[0], importSize[1] * 12 / 100)
		)

		# Close Button
		closeButton = ButtonClass.Button(
			(importSize[0] * 10 / 100, importSize[0] * 10 / 100),
			Const.CLOSE_BUTTON,
			(importCoord[0] + importSize[0] * 81 / 100, importCoord[1] + importSize[1] * 9 / 100, importSize[0] * 10 / 100, importSize[0] * 10 / 100)
		)

		# Process Text
		processText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.BROWN,
			20,
			'',
			(importCoord[0], importCoord[1] + importSize[1] * 8 / 10, importSize[0], importSize[1] * 12 / 100)
		)

		curFileTxt = None

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					exit(0)

			# Up, Down Level Process
			upLevelState = upLevelButton.isClicked(self.gameScreen)
			if upLevelState == True:
				if levelID < 4:
					levelID += 1
				levelIDText.changeTextContent('Level ' + str(levelID))

			downLevelState = downLevelButton.isClicked(self.gameScreen)
			if downLevelState == True:
				if levelID > 1:
					levelID -= 1
				levelIDText.changeTextContent('Level ' + str(levelID))

			for i in range(4):
				if algoButton[i].isClicked(self.gameScreen) == True:
					algoID = i

			if closeButton.isClicked(self.gameScreen):
				return False

			if startButton.isClicked(self.gameScreen):
				if curFileTxt == None:
					processText.changeTextContent('Not Valid File')
				elif algoID == -1:
					processText.changeTextContent('Please Choose Algorithm')
				else:
					processText.changeTextContent('Loading...')
					menuSystem = system.SystemController()
					menuSystem.readUserImportMap(curFileTxt, levelID)

					curAlgo = algoList[algoID]
					curAlgo = curAlgo.lower()
					if curAlgo == 'a*':
						curAlgo = 'astar'
					menuSystem.solvingAllMap(curAlgo)

					ingame = InGame.InGame((0, levelID, curAlgo))
					ingame.run()

					return True

			if fileDialogButton.isClicked(self.gameScreen):
				curFileTxt = openFileDialog()
				if curFileTxt != None:
					processText.changeTextContent('Loading File')

			self.importMapBackGround.draw(self.gameScreen)
			startButton.draw(self.gameScreen)
			closeButton.draw(self.gameScreen)
			fileDialogButton.draw(self.gameScreen)
			fileDialogText.draw(self.gameScreen)
			importText.draw(self.gameScreen)
			levelDropbox.draw(self.gameScreen)
			levelIDText.draw(self.gameScreen)
			upLevelButton.draw(self.gameScreen)
			downLevelButton.draw(self.gameScreen)
			processText.draw(self.gameScreen)
			for i in range(len(algoButton)):
				if i == algoID:
					algoButton[i].fillColor(self.gameScreen)
				else:
					algoButton[i].draw(self.gameScreen)
			for i in algoText:
				i.draw(self.gameScreen)

			pygame.display.update()	


	def run(self):
		while self.running:
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					exit(0)
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_presses = pygame.mouse.get_pressed()

			# Up, Down Level Process
			upLevelState = self.upLevelButton.isClicked(self.gameScreen)
			if upLevelState == True:
				if self.levelID < 4:
					self.levelID += 1
				self.levelIDText.changeTextContent('Level ' + str(self.levelID))

			downLevelState = self.downLevelButton.isClicked(self.gameScreen)
			if downLevelState == True:
				if self.levelID > 1:
					self.levelID -= 1
				self.levelIDText.changeTextContent('Level ' + str(self.levelID))

			# Up, Down Map Process
			upMapState = self.upMapButton.isClicked(self.gameScreen)
			if upMapState == True:
				if self.mapID < 5:
					self.mapID += 1
				self.mapIDText.changeTextContent('Map ' + str(self.mapID))

			downMapState = self.downMapButton.isClicked(self.gameScreen)
			if downMapState == True:
				if self.mapID > 1:
					self.mapID -= 1
				self.mapIDText.changeTextContent('Map ' + str(self.mapID))

			# Algorithm Process
			for i in range(4):
				algoState = self.algoTickButtonList[i][0].isClicked(self.gameScreen)
				if algoState == True:
					self.algorithmID = i

			# Import Map Process
			importmapButtonState = self.importMapButton.isClicked(self.gameScreen)
			importMap = None

			if importmapButtonState == True:
				importMap = self.importMapScreen()
				if importMap == True:
					# ingame.run()
					break

			# Start Button Process
			startButtonState = self.startButton.isClicked(self.gameScreen)

			if startButtonState == True:
				if self.algorithmID != -1:
					ingame = InGame.InGame((self.mapID, self.levelID, self.algoTuple[self.algorithmID]))
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
			self.importMapButton.draw(self.gameScreen)
			self.importMapText.draw(self.gameScreen)
			self.startButton.draw(self.gameScreen)
			# self.importMapBackGround.draw(self.gameScreen)

			pygame.display.update()
		