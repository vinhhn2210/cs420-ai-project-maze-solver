import pygame
import Const
import MapClass
import AgentClass

class InGame:
	def __init__(self):
		# Init
		pygame.init()

		# Set up Game Window
		self.gameScreen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption("Move Your Step")
		pygame.display.flip()
		self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

		# Running
		self.running = True

		# Game background
		self.gameBackground = pygame.transform.scale(Const.INGAME_BACKGROUND, (self.screenWidth, self.screenHeight))
		self.gameScreen.blit(self.gameBackground, (0, 0))

		# Set up Map
		self.gameMap = MapClass.Map((self.screenWidth, self.screenHeight), (0, 0, self.screenWidth, self.screenHeight))
		
		# Set up Clock
		self.clock = pygame.time.Clock()
		isEndGame = False
		initTick = pygame.time.get_ticks()
		stepTime = 0.5

		# Agent
		self.agent1 = AgentClass.Agent(1, self.gameMap.getCell(1, 1))

	def run(self):
		while self.running :
			self.clock.tick(10)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.agent1.handleEvent()

			# Draw window
			self.gameScreen.blit(self.gameBackground, (0, 0))
			self.gameMap.draw(self.gameScreen)
			self.agent1.draw(self.gameScreen)

			pygame.display.update()


