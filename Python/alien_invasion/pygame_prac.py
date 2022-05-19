import pygame

screen = pygame.display.set_mode((800,1200))
image = pygame.image.load('images/dancing-dave-minion-510835_640.jpg')

screen.blit(image)

pygame.display.update()