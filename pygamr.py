import pygame, sys
import time
from pygame.locals import *

LARGEUR = 640
HAUTEUR = 480

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([0,0,0])

x = 300
y = 200
dx = 4
dy = -3
couleur = (45,170,250)

while True :
    fenetre.fill([0,0,0])
    pygame.draw.circle(fenetre,couleur,(x,y),10)

    x += dx
    y += dy
    if y < 0:
        dy = -1*dy
    if x > 640:
        dx= -1*dx
    if y > 480:
        dy = -1*dy
    if x < 0:
        dx = -1*dx
       

    pygame.display.update()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


    time.sleep(0.01)




