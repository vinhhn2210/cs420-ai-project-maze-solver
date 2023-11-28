import pygame
import Const
import ObjectClass
import TextClass
import ButtonClass
import InGame

class Leaderboard:
	def __init__(self):
		pygame.init()

		### Prepare data
		self.levelID = 1
		self.algorithmID = -1
		self.mapID = 1

		# Menu Screen
		infoObject = pygame.display.Info()
		screenProportion = 1
		self.gameScreen = pygame.display.set_mode((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()
		pygame.display.flip()
		pygame.display.set_caption("Move Your Step")


		# Run
		self.running = True
		self.clock = pygame.time.Clock()

		# Menu Background
		self.backgroundImage = pygame.transform.scale(Const.LEADERBOARD_BACKGROUND, (self.screenWidth, self.screenHeight))

		# Content Box Container
		containerBoxContainer = (self.screenWidth * 334 / 1000, self.screenHeight * 115 / 563, self.screenWidth * 332 / 1000, self.screenHeight * 332 / 563)

		# Leaderboard Text
		self.leaderboardText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			60,
			"Leaderboard",
			(containerBoxContainer[0], containerBoxContainer[1], containerBoxContainer[2], containerBoxContainer[3] * 30 / 100)
		)

		# Algorithm Text
		self.levelText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			"Level: 1",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 25 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Algorithm Text
		self.algorithmText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			"Algorithm: BFS",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 40 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Time Text
		self.timeText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			"Time: 10s",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 55 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Memory Text
		self.memoryText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			"Memory: 10MB",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 70 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Score Text
		self.scoreText = TextClass.Text(
			Const.AMATICSC_FONT,
			Const.WHITE,
			35,
			"Score: 100",
			(containerBoxContainer[0], containerBoxContainer[1] + containerBoxContainer[3] * 85 / 100, containerBoxContainer[2], containerBoxContainer[3] * 15 / 100)
		)

		# Start Button
		self.backButton = ButtonClass.Button(
			(self.screenWidth * 10 / 100, self.screenHeight * 10 / 100),
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

			# Start Button Process
			backButtonState = self.backButton.isClicked(self.gameScreen)

			if backButtonState == True:
				break

			# Draw Window
			self.gameScreen.blit(self.backgroundImage, (0, 0))
			self.leaderboardText.draw(self.gameScreen)
			self.algorithmText.draw(self.gameScreen)
			self.levelText.draw(self.gameScreen)
			self.timeText.draw(self.gameScreen)
			self.memoryText.draw(self.gameScreen)
			self.scoreText.draw(self.gameScreen)
			self.backButton.draw(self.gameScreen)

			pygame.display.update()
		