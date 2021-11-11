import pygame, math, sys
import random as r
from pygame.locals import *

directionx = r.randrange(-5, 5)
directiony = r.randrange(-5, 5)
FPS = 60
FramePerSec = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((800,600))

pygame.init()

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (560, 520)
       
    def move(self):
        self.rect.move_ip(directionx, directiony)
        
        

while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Moves and Re-draws all Sprites
    Player2.move()
    DISPLAYSURF.blit(Player2.image, Player2.rect)
        
    pygame.display.update()
    FramePerSec.tick(FPS)