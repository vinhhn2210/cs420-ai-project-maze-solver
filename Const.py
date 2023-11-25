import pygame

DELL = (1280, 720)

# Color
WHITE = (255, 255, 255)

# Text Font
AMATICSC_FONT = 'Assets/Fonts/AmaticSC-Bold.ttf'
VCR_OSD_MONO_FONT = 'Assets/Fonts/VCR_OSD_MONO.ttf'

# Menu
MENU_BACKGROUND = pygame.image.load('Assets/Images/Menu/Background.png')
LOGO_IMAGE = pygame.image.load('Assets/Images/Menu/Logo.png')
START_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/start-button.png')
DROPBOX_IMAGE = pygame.image.load('Assets/Images/Menu/dropdown.png')
UP_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/up.png')
DOWN_BUTTON_IMAGE = pygame.image.load('Assets/Images/Menu/down.png')
TICK_IMAGE = [
	pygame.image.load('Assets/Images/Menu/checkbox-unchecked.png'),
	pygame.image.load('Assets/Images/Menu/checkbox-checked.png')
]

# In Game
INGAME_BACKGROUND = pygame.image.load('Assets/Images/InGame/Background.png')
CELL_MOVE = ((0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))
CELL_IMAGE_LIST = [pygame.image.load(f'Assets/Images/InGame/Cell/tile_{i}.png') for i in range(12)]

AGENT_FRAME_LIST = [
	[pygame.image.load(f'Assets/Images/InGame/Agent/player{i}-left-{j}.png') for i in range(1, 5) for j in range(12)],
	[pygame.image.load(f'Assets/Images/InGame/Agent/player{i}-right-{j}.png') for i in range(1, 5) for j in range(12)],
]

PORTAL_FRAME_LIST = [pygame.image.load(f'Assets/Images/InGame/Portal/portal-{i}.png') for i in range(9)]

