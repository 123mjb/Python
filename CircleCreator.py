import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Circles")

while True:
    for i in range(5, 395, 5):
        pygame.draw.circle(DISPLAYSURF, BLACK, (int(i), 5), 5, 1)