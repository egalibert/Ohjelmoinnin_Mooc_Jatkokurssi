# TEE PELI TÄHÄN

import pygame
from random import *

class Hirvio:
	def __init__(self):
		self.x = randint(0, 640)
		self.y = randint(-300, -300)
		self.finished = False

	def tiputa_hirvio(self):
		if self.y < 600 - hirvio.get_height():
			self.y += 2
		if self.y > (480 - hirvio.get_height()) or self.y > 480:
			self.finished = True

class Coins:
	def __init__(self):
		self.x = randint(0, 640)
		self.y = randint(-500, -200)
		self.finished = False
		

	def tiputa_kolikko(self):
		if self.y < 600:
			self.y += 2
		if self.y > 480 - 50 or self.y > 480:
			self.finished = True

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
coin = pygame.image.load("kolikko.png")
hirvio = pygame.image.load("hirvio.png")

x = 320-robo.get_width()
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
ylos = False
alas = False

kello = pygame.time.Clock()

kolikoita = 10
kolikot = []
for i in range(kolikoita):
	i = Coins()
	kolikot.append(i)

monsters = 10
mon_list = []
for mon in range(monsters):
	mon = Hirvio()
	mon_list.append(mon)

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

		if tapahtuma.type == pygame.KEYUP:
			if tapahtuma.key == pygame.K_LEFT:
				vasemmalle = False
			if tapahtuma.key == pygame.K_RIGHT:
				oikealle = False
			if tapahtuma.key == pygame.K_UP:
				ylos = False
			if tapahtuma.key == pygame.K_DOWN:
				alas = False

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

	naytto.fill((255, 0, 255))

	for kolikko in kolikot:
		kolikko.tiputa_kolikko()
		naytto.blit(coin, (kolikko.x, kolikko.y))
		if kolikko.finished:
			kolikot.remove(kolikko)
			kolikko = Coins()
			kolikot.append(kolikko)

	for monster in mon_list:
		monster.tiputa_hirvio()
		naytto.blit(hirvio, (monster.x, monster.y))
		if monster.finished:
			mon_list.remove(monster)
			monster = Hirvio()
			mon_list.append(kolikko)
	
	naytto.blit(robo, (x, y))
	pygame.display.flip()

	kello.tick(60)