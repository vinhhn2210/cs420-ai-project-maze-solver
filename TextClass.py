import pygame
import Const

class Text:
	def __init__(self, textFont, textColor, textSize, textContent, containerInfo):
		self.textFont = pygame.font.Font(textFont, textSize)
		self.textColor = textColor
		self.text = self.textFont.render(textContent, True, textColor)
		textHeight = self.textFont.size(textContent)[1]
		textWidth = self.textFont.size(textContent)[0]
		self.textCoord = (containerInfo[0] + (containerInfo[2] - textWidth) / 2, containerInfo[1] + (containerInfo[3] - textHeight) / 2)
		self.leftToRightTextCoord = (containerInfo[0], containerInfo[1] + (containerInfo[3] - textHeight) / 2)

	def changeTextContent(self, newContent):
		self.text = self.textFont.render(newContent, True, self.textColor)

	def draw(self, gameScreen):
		gameScreen.blit(self.text, self.textCoord)

	def drawLeftToRight(self, gameScreen):
		gameScreen.blit(self.text, self.leftToRightTextCoord)
