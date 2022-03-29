# from Python.TurtleFake import DISPLAYSURF
import pygame
from pygame import *

pygame.init()
DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
WINDOWSIZE = DISPLAYSURF.get_size()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()