# TEE RATKAISUSI TÄHÄN:

import pygame
from random import randint

pygame.init()
korkeus = 480
leveys = 640
naytto = pygame.display.set_mode((leveys, korkeus))
robo = pygame.image.load("robo.png")

class Robot():
	def __init__(self):
		self.x = randint(0, leveys)
		self.y = randint(-500, -100)
		self.finished = False
		self.suunta = randint (1,2)
		
	def move_bot(self):
		if self.y < korkeus - robo.get_height():
			self.y += 2
		else:
			if self.x < leveys / 2:
				self.x -= 2
			else:
				self.x += 2
		if self.x < (0 - robo.get_width()) or self.x > leveys:
			self.finished = True

clock = pygame.time.Clock()
robot_amount = 10
robots = []
for i in range(robot_amount):
	i = Robot()
	robots.append(i)
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	naytto.fill((0, 0, 0))
	for i in robots:
		i.move_bot()
		naytto.blit(robo, (i.x, i.y))
		if i.finished:
			robots.remove(i)
			i = Robot()
			robots.append(i)
	pygame.display.flip()
	clock.tick(60)