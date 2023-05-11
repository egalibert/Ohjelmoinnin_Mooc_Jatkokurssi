# TEE RATKAISUSI TÄHÄN:

import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

kulma = 0
keski_x = 0
keski_y = 0
kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()

	keski_x = 640 / 2
	keski_y = 480 / 2

	# x = keski_x+math.cos(kulma)*100-robo.get_width()/2
	# y = keski_y+math.sin(kulma)*100-robo.get_height()/2

	naytto.fill((0, 0, 0))

	for index in range(10):
		x = keski_x + math.cos(kulma + (2 * math.pi) * (index / 10)) * 150 - robo.get_width() / 2
		y = keski_y + math.sin(kulma + (2 * math.pi) * (index / 10)) * 150 - robo.get_height() / 2
		naytto.blit(robo, (x, y))
	
	pygame.display.flip()

	kulma += 0.01
	kello.tick(60)