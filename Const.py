import pygame

DELL = (1280, 720)

# Color
WHITE = (255, 255, 255)
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
CELL_MOVE = ((0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/InGame/Cell/tile-{i}.png') for i in range(1, 6)]
CELL_IMAGE_BLOCK = pygame.image.load(f'Assets/Images/InGame/Cell/Block.png')
CELL_IMAGE_CHEST = [pygame.image.load(f'Assets/Images/InGame/Cell/chest_{i}.png') for i in range(1, 10)]

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
# AGENT_FRAME_LIST = [
# 	[pygame.image.load(f'Assets/Images/InGame/Agent/player{i}-left-{j}.png') for i in range(1, 5) for j in range(12)],
# 	[pygame.image.load(f'Assets/Images/InGame/Agent/player{i}-right-{j}.png') for i in range(1, 5) for j in range(12)],
# ]


# Leaderboard
LEADERBOARD_BACKGROUND = pygame.image.load('Assets/Images/Leaderboard/Background.png')
BACK_BUTTON = pygame.image.load('Assets/Images/Leaderboard/back.png')