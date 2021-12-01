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
fails = 0

DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Circles")

def randcircles():
    global test1, test2, randcircleslistx, randcircleslisty, randcirclesx, randcirclesy, fails
    for p in range(0, 1000):
        test1 = False
        test2 = False
        while not test1 and not test2:
            test1 = True
            test2 = True
            randcirclesy = random.randrange(5, 595)
            randcirclesx = random.randrange(5, 795)
            for h in randcircleslistx:
                if randcirclesx > h-10 and randcirclesx < h+10:
                    test1 = False
            for t in randcircleslisty:
                if randcirclesy > t-10 and randcirclesy < t+10:
                    test2 = False
            print(randcirclesx, randcirclesy)
            fails += 1
            if fails == 200: break
        if fails != 200: randcircleslistx.append(randcirclesx), randcircleslisty.append(randcirclesy)
        fails, randcirclesx, randcirclesy = 0,0,0
    print(randcircleslistx, len(randcircleslistx))
    print(randcircleslisty, len(randcircleslisty))    
randcircles()

while True:
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    """for j in range(5, 605, 10):
        for i in range(5, 805, 10):
            pygame.draw.circle(DISPLAYSURF, BLACK, (i, j), 5, 1)  """
    for o in range(0, len(randcircleslistx)):
        pygame.draw.circle(DISPLAYSURF, BLACK, (randcircleslistx[o], randcircleslisty[o]), 5, 1)

    pygame.display.update()
    FramePerSec.tick(FPS)