import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
max = pygame.image.load("max.png")

naytto.fill((0, 0, 0))

leveys = robo.get_width()
korkeus = robo.get_height()
naytto.blit(robo, (0, 0))
naytto.blit(robo, (640-leveys, 480-korkeus))
naytto.blit(robo, (640-leveys, 0))
naytto.blit(robo, (0, 480-korkeus))

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()