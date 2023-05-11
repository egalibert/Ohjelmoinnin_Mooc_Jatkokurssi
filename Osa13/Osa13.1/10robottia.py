# TEE RATKAISUSI TÄHÄN:

import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))

i = 0

leveys = robo.get_width()
korkeus = robo.get_height()
x = 0
print (leveys)

while (i < 10):
	naytto.blit(robo, (570-leveys-x, (480 / 4)))

	x += leveys
	i += 1
	

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()