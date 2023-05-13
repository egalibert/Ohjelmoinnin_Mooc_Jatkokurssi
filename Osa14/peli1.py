import pygame
from random import randint
class Kolikkopeli:
    def __init__(self):
        pygame.init()
 
        self.uusi_peli()
 
        self.naytto = pygame.display.set_mode((640, 480 + 50))
        self.fontti = pygame.font.SysFont("Arial", 20)
        pygame.display.set_caption("Kerää 20 kolikkoa ja varo hirviötä!")
        self.robo = pygame.image.load("robo.png")
        self.kolikko = pygame.image.load("kolikko.png")
        self.hirviö = pygame.image.load("hirvio.png")
        self.robokorkeus = self.robo.get_height()
        self.roboleveys = self.robo.get_width()
        self.kolikkokorkeus = self.kolikko.get_height()
        self.kolikkoleveys = self.kolikko.get_width()
        self.hirviökorkeus = self.hirviö.get_height()
        self.hirviöleveys = self.hirviö.get_width()
        self.kello = pygame.time.Clock()
 
        self.silmukka()
 
    def uusi_peli(self):
# robo = rx, ry  --  kolikko = kx, ky  ---- hirviö = hx, hy
        self.rx = 0
        self.ry = 0
        self.kx = 200
        self.ky = 200
        self.hx = 500
        self.hy = 400
        self.oikealle = False
        self.vasemmalle = False
        self.ylös = False
        self.alas = False
        self.d = False
        self.a = False
        self.w = False
        self.s = False
        self.kerätytkolikot = 0
 
    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.liiku()
            self.keräys()
            self.piirra_naytto()
            self.kello.tick(100)
            
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylös = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True
                
                if tapahtuma.key == pygame.K_a:
                    self.a = True
                if tapahtuma.key == pygame.K_d:
                    self.d = True
                if tapahtuma.key == pygame.K_w:
                    self.w = True
                if tapahtuma.key == pygame.K_s:
                    self.s = True
 
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylös = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
                
                if tapahtuma.key == pygame.K_a:
                    self.a = False
                if tapahtuma.key == pygame.K_d:
                    self.d = False
                if tapahtuma.key == pygame.K_w:
                    self.w = False
                if tapahtuma.key == pygame.K_s:
                    self.s = False
 
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()
                    
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
 
            if tapahtuma.type == pygame.QUIT:
                exit()
 
    def liiku(self):
        if self.peli_läpi():
            return
        
        if self.häviö():
            return
 
        if self.oikealle:
            self.rx += 1
        if self.vasemmalle:
            self.rx -= 1
        if self.ylös:
            self.ry -= 1
        if self.alas:
            self.ry += 1
 
        if self.d:
            if (self.ky in range(self.hy, self.hy + self.hirviökorkeus) or self.ky+self.kolikkokorkeus in range(self.hy, self.hy + self.hirviökorkeus)) and self.kx == self.hx + self.hirviöleveys:
                return
            self.hx += 1
        if self.a:
            if (self.hy in range(self.ky-23, self.ky + self.kolikkokorkeus+23) or self.hy+self.hirviökorkeus in range(self.ky-23, self.ky + self.kolikkokorkeus+23))and self.hx == self.kx + self.kolikkoleveys:
                return
            self.hx -= 1
        if self.w:
            if (self.hx in range(self.kx-5, self.kx+self.kolikkoleveys+5) or self.hx+self.hirviöleveys in range(self.kx-5, self.kx+self.kolikkoleveys+5))and self.hy == self.ky + self.kolikkokorkeus:
                return
            self.hy -= 1
        if self.s:
            if (self.kx in range(self.hx, self.hx + self.hirviöleveys+1) or self.kx+self.kolikkoleveys in range(self.hx, self.hx + self.hirviöleveys+1))and self.ky == self.hy + self.hirviökorkeus:
                return
            self.hy += 1
 
    def keräys(self):
        if (self.rx in range(self.kx-5, self.kx+self.kolikkoleveys+5) or self.rx+self.roboleveys in range(self.kx-5, self.kx+self.kolikkoleveys+5))and self.ry in range(self.ky, self.ky + self.kolikkokorkeus):
            self.kx = randint(0, 640-self.kolikkoleveys)
            self.ky = randint(0, 480-self.kolikkokorkeus)
            self.kerätytkolikot += 1
 
        elif (self.ry in range(self.ky-23, self.ky + self.kolikkokorkeus+23) or self.ry+self.robokorkeus in range(self.ky-23, self.ky + self.kolikkokorkeus+23))and self.rx in range(self.kx, self.kx + self.kolikkoleveys):
            self.kx = randint(0, 640-self.kolikkoleveys)
            self.ky = randint(0, 480-self.kolikkokorkeus)
            self.kerätytkolikot += 1
 
        elif (self.kx in range(self.rx, self.rx + self.roboleveys+1) or self.kx+self.kolikkoleveys in range(self.rx, self.rx + self.roboleveys+1))and self.ky in range(self.ry, self.ry + self.robokorkeus):
            self.kx = randint(0, 640-self.kolikkoleveys)
            self.ky = randint(0, 480-self.kolikkokorkeus)
            self.kerätytkolikot += 1
 
        elif (self.ky in range(self.ry, self.ry + self.robokorkeus) or self.ky+self.kolikkokorkeus in range(self.ry, self.ry + self.robokorkeus)) and self.kx in range(self.rx, self.rx + self.roboleveys):
            self.kx = randint(0, 640-self.kolikkoleveys)
            self.ky = randint(0, 480-self.kolikkokorkeus)
            self.kerätytkolikot += 1
        
        else:
            return
 
    def piirra_naytto(self):
        self.naytto.fill((255, 255, 255))
        self.naytto.blit(self.robo, (self.rx, self.ry))
        self.naytto.blit(self.kolikko, (self.kx, self.ky))
        self.naytto.blit(self.hirviö, (self.hx, self.hy))
 
        teksti = self.fontti.render("Kerätyt kolikot: " + str(self.kerätytkolikot), True, (0, 0, 255))
        self.naytto.blit(teksti, (5, 480 + 25))
 
        teksti = self.fontti.render("F2 = uusi peli", True, (0, 0, 255))
        self.naytto.blit(teksti, (270, 480 + 25))
 
        teksti = self.fontti.render("Esc = sulje peli", True, (0, 0, 255))
        self.naytto.blit(teksti, (520, 480 + 25))
 
        if self.peli_läpi():
            teksti = self.fontti.render("Keräsit tarpeeksi kolikoita!", True, (0, 0, 0))
            teksti_x = 200
            teksti_y = 200
            pygame.draw.rect(self.naytto, (146, 216, 255), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))
 
        if self.häviö():
            teksti = self.fontti.render("Voi ei! Hirviö sai sinut kiinni!", True, (0, 0, 0))
            teksti_x = 200
            teksti_y = 200
            pygame.draw.rect(self.naytto, (255, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))
 
        pygame.display.flip()
 
    def peli_läpi(self):
        if self.kerätytkolikot == 20:
            return True
        return False
 
    def häviö(self):
        if (self.hx in range(self.rx, self.rx+self.roboleveys+1) or self.hx+self.hirviöleveys in range(self.rx, self.rx+self.roboleveys+1))and self.hy in range(self.ry, self.ry + self.robokorkeus):
            return True
 
        elif (self.hy in range(self.ry, self.ry + self.robokorkeus+1) or self.hy+self.hirviökorkeus in range(self.ry, self.ry + self.robokorkeus+1))and self.hx in range(self.rx, self.rx + self.roboleveys):
            return True
 
        elif (self.rx in range(self.hx, self.hx + self.hirviöleveys+1) or self.rx+self.roboleveys in range(self.hx, self.hx + self.hirviöleveys+1))and self.ry in range(self.hy, self.hy + self.hirviökorkeus):
            return True
 
        elif (self.ry in range(self.hy, self.hy + self.hirviökorkeus) or self.ry+self.robokorkeus in range(self.hy, self.hy + self.hirviökorkeus)) and self.rx in range(self.hx, self.hx + self.hirviöleveys):
            return True
        
        else:
            return False
        
if __name__ == "__main__":
    Kolikkopeli()