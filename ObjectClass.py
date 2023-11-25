import pygame

class Object:
	def __init__(self, objectSize, objectImage, containerInfo):
		self.size = (objectSize[0], objectSize[1])
		self.image = pygame.transform.scale(objectImage, self.size)
		self.coord = (containerInfo[0] + (containerInfo[2] - self.size[0]) / 2, containerInfo[1] + (containerInfo[3] - self.size[1]) / 2)

	def draw(self, gameScreen):
		gameScreen.blit(self.image, self.coord)