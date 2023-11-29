import MenuClass
import pygame

# Init
pygame.init()
infoObject = pygame.display.Info()
screenProportion = 3 / 4

menuGame = MenuClass.Menu((infoObject.current_w * screenProportion, infoObject.current_h * screenProportion))

menuGame.run()