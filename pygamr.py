import pygame, sys
import time
from pygame.locals import *
from random import randint

LARGEUR = 1200
HAUTEUR = 800
RAYON = 40


pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])


class Balle:
    def __init__(self):
        self.x = randint(10,LARGEUR-20)
        self.y = randint(10,HAUTEUR-20)
        self.couleur = (randint(0,255), randint(0,255), randint(0,255))
        self.rayon = randint(10,40)
        self.dx = randint(2,10)
        self.dy = randint(2,10)
        
    def dessine(self,):
        pygame.draw.circle(fenetre,self.couleur,(self.x,self.y),self.rayon)
        
    def bouge(self):
        self.x += self.dx
        self.y += self.dy
        if (self.y <= self.rayon) or (self.y >= HAUTEUR - self.rayon):
            self.dy = -self.dy
        if (self.x <= self.rayon) or (self.x >= LARGEUR - self.rayon):
            self.dx = -self.dx
        for balle in sac_a_balles:
            if ((self.x - balle.x)**2 + (self.y - balle.y)**2)**0.5 < self.rayon + balle.rayon:
                self.dx, balle.dx = balle.dx, self.dx
                self.dy, balle.dy = balle.dy, balle.dy
                
            
sac_a_balles = []
for _ in range(10):
    sac_a_balles.append(Balle())
    
    
        
  
    
            
            
           



while True :
    fenetre.fill([0,0,0])
    
    for balle in sac_a_balles:
        balle.dessine()
        balle.bouge()
        
    
    
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


    time.sleep(0.02)



