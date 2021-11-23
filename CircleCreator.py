import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
test1 = False
test2 = False
randcirclesy = 0
randcirclesx = 0
randcircleslistx = []
randcircleslisty = []

DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Circles")

def randcircles():
    global test1, test2, randcircleslistx, randcircleslisty, randcirclesx, randcirclesy
    for p in range(0, 100):
        test1 = True
        test2 = True
        while test1 or test2:
            test1 = False
            test2 = False
            randcirclesy = random.randrange(0, 600)
            randcirclesx = random.randrange(0, 800)
            for h in randcircleslistx:
                if randcirclesx == h-5 or randcirclesx == h+5:
                    test1 = True
                else:
                    test1 = False
            for t in randcircleslisty:
                if randcirclesy==t-5 or randcirclesy==t+5:
                    test2 = True
                else:
                    test2 = False
            print(randcirclesx, randcirclesy)
        
        randcircleslistx.append(randcirclesx)
        randcircleslisty.append(randcirclesy)
        randcirclesx=0
        randcirclesy=0
    print(randcircleslistx)
    print(randcircleslisty)    
randcircles()

while True:
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    """for j in range(5, 605, 10):
        for i in range(5, 805, 10):
            pygame.draw.circle(DISPLAYSURF, BLACK, (i, j), 5, 1)  """
    for o in range(0, 100):
        pygame.draw.circle(DISPLAYSURF, BLACK, (randcircleslistx[o], randcircleslisty[o]), 5, 1)

    pygame.display.update()
    FramePerSec.tick(FPS)