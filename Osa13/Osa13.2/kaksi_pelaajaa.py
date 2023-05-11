# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
x = 0
y = 480-robo.get_height()

robo2 = pygame.image.load("robo.png")
x2 = 640-robo2.get_width()
y2 = 0

oikealle = False
vasemmalle = False
ylos = False
alas = False

oikealle2 = False
vasemmalle2 = False
ylos2 = False
alas2 = False

kello = pygame.time.Clock()

while True:
	for tapahtuma in pygame.event.get():
		if tapahtuma.type == pygame.KEYDOWN:
			if tapahtuma.key == pygame.K_LEFT:
				vasemmalle = True
			if tapahtuma.key == pygame.K_RIGHT:
				oikealle = True
			if tapahtuma.key == pygame.K_UP:
				ylos = True
			if tapahtuma.key == pygame.K_DOWN:
				alas = True

			if tapahtuma.key == pygame.K_a:
				vasemmalle2 = True
			if tapahtuma.key == pygame.K_d:
				oikealle2 = True
			if tapahtuma.key == pygame.K_w:
				ylos2 = True
			if tapahtuma.key == pygame.K_s:
				alas2 = True

		if tapahtuma.type == pygame.KEYUP:
			if tapahtuma.key == pygame.K_LEFT:
				vasemmalle = False
			if tapahtuma.key == pygame.K_RIGHT:
				oikealle = False
			if tapahtuma.key == pygame.K_UP:
				ylos = False
			if tapahtuma.key == pygame.K_DOWN:
				alas = False

			if tapahtuma.key == pygame.K_a:
				vasemmalle2 = False
			if tapahtuma.key == pygame.K_d:
				oikealle2 = False
			if tapahtuma.key == pygame.K_w:
				ylos2 = False
			if tapahtuma.key == pygame.K_s:
				alas2 = False

		if tapahtuma.type == pygame.QUIT:
			exit()

	if oikealle and x + robo.get_width() <= 640:
		x += 2
	if vasemmalle and x >= 0:
		x -= 2
	if ylos and y >= 0:
		y -= 2
	if alas and y + robo.get_height() <= 480:
		y += 2

	if oikealle2 and x2+robo2.get_width() < 640:
		x2 += 2
	if vasemmalle2 and x2 > 0:
		x2 -= 2
	if ylos2 and y2 > 0:
		y2 -= 2
	if alas2 and y2+robo2.get_height() < 480:
		y2 += 2

	naytto.fill((0, 0, 0))
	naytto.blit(robo, (x, y))
	naytto.blit(robo2, (x2, y2))
	pygame.display.flip()

	kello.tick(60)