# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
robo2 = pygame.image.load("robo.png")

x = 0
y = 0
z = 0

nopeus = 1
nopeus2 = 1

kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()

	naytto.fill((0, 0, 0))
	naytto.blit(robo, (x, y))
	naytto.blit(robo2, (z, y+robo2.get_height()))
	pygame.display.flip()
	
	x += nopeus
	z += nopeus2 * 2

	if nopeus > 0 and x+robo.get_width() >= 640:
		nopeus = -nopeus
	if nopeus < 0 and x <= 0:
		nopeus = -nopeus

	if nopeus2 > 0 and z+robo2.get_width() >= 640:
		nopeus2 = -1

	if nopeus2 < 0 and z <= 0:
		nopeus2 = 1


	kello.tick(60)