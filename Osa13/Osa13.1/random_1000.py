# TEE RATKAISUSI TÄHÄN:

from random import *
import pygame
 
pygame.init()
naytto = pygame.display.set_mode((640, 480))
 
robo = pygame.image.load("robo.png")
index = 0
x = 0
y = 0
 
naytto.fill((0, 0, 0))
while index < 1000:
	x = randint(0, 640)
	y = randint(0, 480)
	print (x, y)
	naytto.blit(robo, (x, y))
	index += 1
pygame.display.flip()
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()