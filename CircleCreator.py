import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Circles")

while True:
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for j in range(5, 605, 10):
        for i in range(5, 805, 10):
            pygame.draw.circle(DISPLAYSURF, BLACK, (i, j), 5, 1)  

    pygame.display.update()
    FramePerSec.tick(FPS)