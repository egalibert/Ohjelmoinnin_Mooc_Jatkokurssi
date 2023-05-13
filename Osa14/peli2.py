import pygame
import random
import sys
class Kolikko:
    osui = True
    osuneet=0
    paras_tulos=0
 
    def __init__(self):
        self.kolikko = pygame.image.load("kolikko.png")
        self.x = random.randrange(20, 780)
        self.y = -(random.randrange(20, 350))
        self.v = random.randrange(1,3)
    def game_over(self):
        if Kolikko.osui == True:
            self.y += self.v
    def osuma(self,robo_x,robo_y):
        if self.y > 550:
            if robo_x+50  < self.x or robo_x  > self.x+40:
                Kolikko.osui=False
 
    def nollaa(self):
        self.x = random.randrange(20, 780)
        self.y = -(random.randrange(20, 350))
        self.v = random.randrange(1, 5)
 
 
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.display.set_caption('Kolikkopeli - F1 Ohje')
font = pygame.font.Font('freesansbold.ttf', 24)
naytto = pygame.display.set_mode((800, 600))
suunta = 0
robo_x = 0
robo_y = 500
game_over = False
help = False
text = font.render("", True, green, blue)
textRect = text.get_rect()
textRect.center = (600,40)
textRect2 = text.get_rect()
textRect2.center = (600,80)
kello = pygame.time.Clock()
naytto.fill((0,0,0))
robo = pygame.image.load("robo.png")
naytto.blit(robo, (robo_x, robo_y))
pygame.display.flip()
kolikkolista = []
for i in range(1,random.randrange(3,5)):
    kolikkolista.append(Kolikko())
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                suunta = 1
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = 2
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                suunta = 0
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = 0
            if tapahtuma.key == pygame.K_SPACE:
                suunta = 0
                robo_x = 0 
                robo_y = 500
                for k in kolikkolista:
                    kolikkolista = []
                    for i in range(1,random.randrange(3,5)):
                        kolikkolista.append(Kolikko())
                Kolikko.osui = True
                Kolikko.osuneet = 0
            if tapahtuma.key == pygame.K_F1:
                help = True
            if tapahtuma.key == pygame.K_ESCAPE:
                help = False
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    naytto.fill((0,0,0))
    pygame.draw.circle(naytto,(255,255,0),(300,60),50)
    pygame.draw.circle(naytto,(0,0,0),(320,60),50)
 
    #kolikon kasittely
    if help == False:
        for k in kolikkolista:
            k.game_over()
            k.osuma(robo_x,robo_y)
            if k.y < 550:
                naytto.blit(k.kolikko, (k.x, k.y))
            else:
                Kolikko.osuneet += 1
                k.nollaa()
 
        if Kolikko.osui == False:
            suunta = 0
            if Kolikko.osuneet > Kolikko.paras_tulos:
                Kolikko.paras_tulos = Kolikko.osuneet
        else:
            if suunta == 1:
                if robo_x > 0:
                    robo_x -= 5
            if suunta == 2:
                if robo_x < 750:
                    robo_x += 5
 
    naytto.blit(robo, (robo_x, robo_y))
 
    if Kolikko.osui == False:
        text1 = font.render(f"Pisteet: {Kolikko.osuneet}", True, green, blue)
        naytto.blit(text1, textRect)
        text2 = font.render(f"Paras tulos: {Kolikko.paras_tulos}", True, green, blue)
        naytto.blit(text2, textRect2)
    if help == True:
        pygame.draw.rect(naytto, (255,255,255),[100, 100, 600, 300], 0)
        txtsurf = font.render("Ohjeet:", True, blue)
        naytto.blit(txtsurf,(120,120))
        txtsurf = font.render("F1 Ohjeet, ESC Poistu ohjeista", True, blue)
        naytto.blit(txtsurf,(120,150))
        txtsurf = font.render("Kerää taivaalta putoavia kolikoita", True, blue)
        naytto.blit(txtsurf,(120,180))
        txtsurf = font.render("--> Siirtyminen oikealle", True, blue)
        naytto.blit(txtsurf,(120,230))
        txtsurf = font.render("<-- Siirtyminen vasemmalle", True, blue)
        naytto.blit(txtsurf,(120,260))
        txtsurf = font.render("Välilyonti Uusi pelikierros", True, blue)
        naytto.blit(txtsurf,(120,290))
        txtsurf = font.render("Näyttää kierroksen tuloksen ja parhaan tuloksen", True, blue)
        naytto.blit(txtsurf,(120,330))
 
    pygame.display.flip()
    kello.tick(60)