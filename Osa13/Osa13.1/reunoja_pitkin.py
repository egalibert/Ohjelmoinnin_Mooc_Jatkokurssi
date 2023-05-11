# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 1
nopeus2 = 0
kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.QUIT:
			exit()

	naytto.fill((0, 0, 0))
	naytto.blit(robo, (x, y))
	pygame.display.flip()
	
	y += nopeus2
	x += nopeus
	if nopeus > 0 and x+robo.get_width() >= 640:
		nopeus2 = 1
		nopeus = 0
	if nopeus2 > 0 and y+robo.get_height() >= 480:
		nopeus2 = 0
		nopeus = -1
	if nopeus < 0 and y+robo.get_height() >= 480 and x <= 0:
		nopeus = 0
		nopeus2 = -1
	if x <= 0 and y <= 0 and nopeus2 < 0:
		nopeus2 = 0
		nopeus = 1

	# if nopeus < 0 and y <= 0:
	#     nopeus = -nopeus
	# if nopeus2 > 0 and x+robo.get_width() >= 640:
	#     nopeus2 = -nopeus2
	# if nopeus2 < 0 and x <= 0:
	#     nopeus2 = -nopeus2

	kello.tick(60)