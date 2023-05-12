import pygame
from random import *

# class Robot:
# 	def __init__(self):
# 		self.x = 320
# 		self.y = 400
		

class Kolikko:
	def __init__(self):
		self.x = randint(0, 640)
		self.y = randint(-200, -100)
		self.finished = False

class CashGrab:
	def __init__ (self):
		pygame.init()

		self.fontti = pygame.font.SysFont("Times New Roman", 26)
		pygame.display.set_caption("Grab The Ca$h")
		self.naytto = pygame.display.set_mode((640, 480))
		
		self.kello = pygame.time.Clock()

		self.x = 0
		self.y = 0

		self.vasemmalle = False
		self.oikealle = False
		self.ylos = False
		self.alas = False


		self.lataa_kuvat()
		self.uusi_peli()
		self.tapahtumat()



	def lataa_kuvat(self):
		self.robo = pygame.image.load("robo.png")
		self.kolikko = pygame.image.load("kolikko.png")
		self.hirvio = pygame.image.load("hirvio.png")


	def uusi_peli(self):
		self.collected = 0
		self.lives = 3
	
		# self.pelaa()
		# self.uusi_taso()

	# def aloitusnaytto(self):
	# 	# print("Menee aloitusnayttoon")
	# 	aloitusteksti = self.fontti.render("Grab The Ca$h", True, (100, 255, 100))
	# 	start = self.fontti.render("Press S to start", True, (255, 0, 0))

	# 	self.naytto.fill((0, 0, 0))

	# 	self.naytto.blit(aloitusteksti, (320 - (aloitusteksti.get_width() / 2), 50))
	# 	self.naytto.blit(start, (320, 360))

	# 	# self.y += 2

	# 	self.drop_coins()
	# 	pygame.display.flip()

	def tapahtumat(self):
		self.naytto.fill((0, 0, 0))
		while True:
			for tapahtuma in pygame.event.get():
				if tapahtuma.type == pygame.KEYDOWN:
					if tapahtuma.key == pygame.K_LEFT:
						self.vasemmalle = True
					if tapahtuma.key == pygame.K_RIGHT:
						self.oikealle = True
					if tapahtuma.key == pygame.K_UP:
						self.ylos = True
					if tapahtuma.key == pygame.K_DOWN:
						self.alas = True

				if tapahtuma.type == pygame.KEYUP:
					if tapahtuma.key == pygame.K_LEFT:
						self.vasemmalle = False
					if tapahtuma.key == pygame.K_RIGHT:
						self.oikealle = False
					if tapahtuma.key == pygame.K_UP:
						self.ylos = False
					if tapahtuma.key == pygame.K_DOWN:
						self.alas = False
					
				if tapahtuma.type == pygame.QUIT:
					exit()
			self.start_game()



	def start_game(self):
		aloitusteksti = self.fontti.render("Grab The Ca$h", True, (100, 255, 100))

		x = 320 - self.robo.get_width()
		y = 480 - self.robo.get_height()

		while (True):
			self.naytto.fill((0, 0, 0))
			self.naytto.blit(aloitusteksti, (320 - (aloitusteksti.get_width() / 2), 30))
			# self.naytto.blit(self.robo, (x,y))


			if self.oikealle: #and x + self.robo.get_width() <= 640:
				x += 2
			if self.vasemmalle: #and self.x >= 0:
				x -= 2
			if self.ylos and self.y >= 0:
				y -= 2
			if self.alas and self.y + self.robo.get_height() <= 480:
				y += 2

			self.naytto.blit(self.robo, (x,y))
			# pygame.display.flip()
			# self.kello.tick(60)

			# self.robot()
			# # self.drop_coins()

			pygame.display.flip()
			self.kello.tick(60)

	# def drop_coins(self):
	# 	coin_count = 10
	# 	coins = []
	# 	for i in range(coin_count):
	# 		i = Kolikko()
	# 		coins.append(i)

	# 	for i in coins:
	# 		i.y += 2
	# 		self.naytto.blit(self.kolikko, (i.x, i.y))

	# 		if i.y >= 480:
	# 			coins.remove(i)
	# 			i = Kolikko()
	# 			coins.append(i)

	def robot(self):
		robo = pygame.image.load("robo.png")
		x = 320 - self.robo.get_width()
		y = 480 - self.robo.get_height()

		if self.oikealle: #and x + self.robo.get_width() <= 640:
			x += 2
		if self.vasemmalle: #and self.x >= 0:
			x -= 2
		if self.ylos and self.y >= 0:
			y -= 2
		if self.alas and self.y + self.robo.get_height() <= 480:
			y += 2

		self.naytto.blit(robo, (x,y))
		pygame.display.flip()
		self.kello.tick(60)

# x = 0
# y = 480-robo.get_height()

# fontti = pygame.font.SysFont("Arial", 24)
# teksti = fontti.render("Level 1", True, (255, 0, 0))

# oikealle = False
# vasemmalle = False
# ylos = False
# alas = False

# kello = pygame.time.Clock()

# while True:
# 	for tapahtuma in pygame.event.get():
# 		if tapahtuma.type == pygame.KEYDOWN:
# 			if tapahtuma.key == pygame.K_LEFT:
# 				vasemmalle = True
# 			if tapahtuma.key == pygame.K_RIGHT:
# 				oikealle = True
# 			if tapahtuma.key == pygame.K_UP:
# 				ylos = True
# 			if tapahtuma.key == pygame.K_DOWN:
# 				alas = True

# 		if tapahtuma.type == pygame.KEYUP:
# 			if tapahtuma.key == pygame.K_LEFT:
# 				vasemmalle = False
# 			if tapahtuma.key == pygame.K_RIGHT:
# 				oikealle = False
# 			if tapahtuma.key == pygame.K_UP:
# 				ylos = False
# 			if tapahtuma.key == pygame.K_DOWN:
# 				alas = False

# 		if tapahtuma.type == pygame.QUIT:
# 			exit()

# 	if oikealle and x + robo.get_width() <= 640:
# 		x += 2
# 	if vasemmalle and x >= 0:
# 		x -= 2
# 	if ylos and y >= 0:
# 		y -= 2
# 	if alas and y + robo.get_height() <= 480:
# 		y += 2

# 	naytto.fill((0, 0, 0))
# 	naytto.blit(teksti, (320 - (teksti.get_width() / 2), 50))
# 	naytto.blit(robo, (x, y))
# 	pygame.display.flip()

# 	kello.tick(60)

def main():
	CashGrab()


main()