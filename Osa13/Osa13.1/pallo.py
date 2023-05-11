# TEE RATKAISUSI TÄHÄN:

import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))
pallo = pygame.image.load("pallo.png")
kello = pygame.time.Clock()

x = 0
y = 0

x_nopeus = 3
y_nopeus = 3

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()

	naytto.fill((0, 0, 0))
	naytto.blit(pallo, (x, y))

	x += x_nopeus
	y += y_nopeus
	if x + pallo.get_width() >= naytto.get_width():
		x_nopeus *= -1
	if y + pallo.get_height() >= naytto.get_height():
		y_nopeus *= -1

	if x_nopeus < 0 and x <= 0:
		x_nopeus *= -1
	if y <= 0 and y_nopeus < 0:
		y_nopeus *= -1


	pygame.display.flip()




	kello.tick(60)