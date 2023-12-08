import pygame

DELL = (1280, 720)

# Color
WHITE = (255, 255, 255)
BROWN = (128,0,0)
BLACK = (0, 0, 0)

# Text Font
AMATICSC_FONT = 'Assets/Fonts/AmaticSC-Bold.ttf'
VCR_OSD_MONO_FONT = 'Assets/Fonts/VCR_OSD_MONO.ttf'

# Menu
MENU_BACKGROUND = pygame.image.load('Assets/Images/Menu/Background.png')
START_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/start.png')
DROPBOX_IMAGE = pygame.image.load('Assets/Images/Menu/Adjust_button.png')
UP_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/up.png')
DOWN_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/down.png')
TICK_IMAGE = [
	pygame.image.load('Assets/Images/Menu/checkbox-unchecked.png'),
	pygame.image.load('Assets/Images/Menu/checkbox-checked.png')
]

# In Game
INGAME_BACKGROUND = pygame.image.load('Assets/Images/InGame/Background.png')
INGAME_BACKGROUND_LEVEL4 = pygame.image.load('Assets/Images/InGame/Background_Level4.png')
CELL_MOVE = ((0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/InGame/Cell/tile-{i}.png') for i in range(1, 6)]
CELL_IMAGE_BLOCK = pygame.image.load(f'Assets/Images/InGame/Cell/Block.png')
CELL_IMAGE_CHEST = [pygame.image.load(f'Assets/Images/InGame/Cell/chest_{i}.png') for i in range(1, 10)]
CELL_IMAGE_KEY = [pygame.image.load(f'Assets/Images/InGame/Cell/Key-{i}.png') for i in range(1, 21)]
CELL_IMAGE_SUPPORTKEY = pygame.image.load(f'Assets/Images/InGame/Cell/Support-Key.png')
CELL_IMAGE_DOOR = [pygame.image.load(f'Assets/Images/InGame/Cell/Door-{i}.png') for i in range(1, 21)]
CELL_IMAGE_STAIR_UP = pygame.image.load(f'Assets/Images/InGame/Cell/Stair-up.png')
CELL_IMAGE_STAIR_DOWN = pygame.image.load(f'Assets/Images/InGame/Cell/Stair-down.png')

COLOR_AGENT = (
	(0, 0, 0),
	(182, 213, 60),
	(35, 205, 224),
	(244, 127, 20),
	(253, 123, 151),
	(228, 185, 36),
	(208, 221, 239),
	(54, 69, 120),
	(127, 112, 111),
	(111, 57, 123)
)
AGENT_FRAME_LIST = [
	[
		[pygame.image.load(f'Assets/Images/InGame/Agent/agent{i}-left-{j}.png') for j in range(3)],
		[pygame.image.load(f'Assets/Images/InGame/Agent/agent{i}-right-{j}.png') for j in range(3)]
	]
	for i in range(1, 10)
]
AGENT_AVA_LIST = [
	pygame.image.load(f'Assets/Images/InGame/Agent/agent{i}-left-0.png')
for i in range(1, 10)]

PAUSE_BUTTON = [
	pygame.image.load('Assets/Images/InGame/Pause_button.png'),
	pygame.image.load('Assets/Images/InGame/Continue_button.png')
]
MENU_BUTTON = pygame.image.load('Assets/Images/InGame/Menu_button.png')


# Leaderboard
LEADERBOARD_BACKGROUND = pygame.image.load('Assets/Images/Leaderboard/Background.png')
BACK_BUTTON_IMAGE = pygame.image.load('Assets/Images/Leaderboard/back.png')