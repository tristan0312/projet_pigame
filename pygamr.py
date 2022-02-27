import pygame, sys
from pygame.locals import *
import time

pygame.init()
pygame.key.set_repeat(50)

fenetre = pygame.display.set_mode((1250, 1000))
fenetre.fill([204,204,255])
cpt = 0
chrono_record = 0
font = pygame.font.Font(pygame.font.get_default_font(), 30)
text = font.render("le but est de faire 100 clic avec la fleche du haut le plus rapidement possible ", True, (0, 0, 0))
fenetre.blit(text, dest=(0,50))


while True :
    top = time.time()
    for event in pygame.event.get() :    
        if event.type == KEYDOWN:
            if event.key == K_UP :
                cpt = cpt + 1
                if cpt == 100:
                    font = pygame.font.Font(pygame.font.get_default_font(), 50)
                    text = font.render("100 clic on etait efectué", True, (76, 0, 153))
                    fenetre.blit(text, dest=(400,400))
                    chrono_parti = time.time() - top
                    if chrono_parti > chrono_record:
                        chrono_record = chrono_parti
                        print("ton record actuelle est de",chrono_record)
                    else:
                        print("ton record actuelle est de",chrono_record)
                    
                        
                        

                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
    
                pygame.display.flip()




