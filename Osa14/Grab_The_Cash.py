# TEE PELI TÄHÄN

import pygame
from random import *

pygame.display.set_caption("Grab The Ca$h")
pygame.init()

def detect_collision(robo_x, robo_y, robo_h, robo_w, muu_x, muu_y, muu_h, muu_w):
	if robo_x < muu_x + muu_w and muu_x < robo_x + robo_w and \
		robo_y < muu_y + muu_h and muu_y < robo_y + robo_h:
		return True
	else:
		return False

class Hirvio:
	def __init__(self):
		self.x = randint(0, 640 - 50)
		self.y = randint(-1500, -200)
		self.velocity = 2
		self.finished = False

	def tiputa_hirvio(self, counter :int):
		if (counter >= 10):
			self.velocity += counter / 1000
		if (counter >= 90):
			self.velocity += 1
		if self.y < 700:
			self.y += self.velocity
		if self.y > (480 - 70) or self.y > 480:
			self.finished = True

class Coins:
	def __init__(self):
		self.x = randint(0, 640 - 50)
		self.y = randint(-1500, -300)
		self.finished = False
		self.velocity = 3
		

	def tiputa_kolikko(self, counter :int):
		if counter >= 10:
			self.velocity += counter / 10000
		if self.y < 700:
			self.y += self.velocity
		if self.y > 480 - 50 or self.y > 480:
			self.finished = True

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
coin = pygame.image.load("kolikko.png")
hirvio = pygame.image.load("hirvio.png")

robo_health = 5
counter = 0

fontti = pygame.font.SysFont("Arial", 36)

x = 320-robo.get_width()
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
ylos = False
alas = False

kello = pygame.time.Clock()

kolikoita = 12
kolikot = []
for i in range(kolikoita):
	i = Coins()
	kolikot.append(i)

monsters = 5
mon_list = []
for mon in range(monsters):
	mon = Hirvio()
	mon_list.append(mon)

def endScreen(counter :int, robo_health :int):
	run = True
	while run:
		pygame.time.delay(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					run = False
					counter = 0
					robo_health = 5
					return 
					
		largeFont = pygame.font.SysFont('comicsans', 80) 
		currentScore = largeFont.render(f"Final Score: {counter}", True, (0, 0, 0))
		restart = fontti.render(f"Press R to restart:", True, (0,0,0))
		win = largeFont.render(f"YOU WON!", True, (0, 0, 0))
		if counter < 100:
			naytto.blit(currentScore, (50, 170))
		if counter == 100:
			naytto.blit(win, (50, 170))
		naytto.blit(restart, (0,0))

		pygame.display.update()
		

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
		x += 3.5
	if vasemmalle and x >= 0:
		x -= 3.5
	if ylos and y >= 0:
		y -= 3.5
	if alas and y + robo.get_height() <= 480:
		y += 3.5


	naytto.fill((255, 0, 255))

	for kolikko in kolikot:
		kolikko.tiputa_kolikko(counter)
		naytto.blit(coin, (kolikko.x, kolikko.y))
		collision = detect_collision(x, y, robo.get_height(), robo.get_width(), kolikko.x, kolikko.y, coin.get_height(), coin.get_width())
		if collision:
			kolikot.remove(kolikko)
			kolikko = Coins()
			kolikot.append(kolikko)
			counter += 1
		if kolikko.finished:
			kolikot.remove(kolikko)
			kolikko = Coins()
			kolikot.append(kolikko)

	for monster in mon_list:
		monster.tiputa_hirvio(counter)
		naytto.blit(hirvio, (monster.x, monster.y))
		collision = detect_collision(x, y, robo.get_height(), robo.get_width(), monster.x, monster.y, hirvio.get_height(), hirvio.get_width())
		if collision:
			mon_list.remove(monster)
			monster = Hirvio()
			mon_list.append(monster)
			robo_health -= 1
		if monster.finished:
			mon_list.remove(monster)
			monster = Hirvio()
			mon_list.append(monster)

	teksti = fontti.render(f"Counter: {counter}", True, (0, 0, 0))
	health = fontti.render(f"Health: {robo_health}", True, (0, 0, 0))

	naytto.blit(robo, (x, y))
	naytto.blit(teksti, (450,430))
	naytto.blit(health, (15,430))

	if robo_health == 0:
		endScreen(counter, robo_health)
	if counter == 100:
		endScreen(counter, robo_health)

	pygame.display.flip()

	kello.tick(60)