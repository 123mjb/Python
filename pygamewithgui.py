import pygame
from pygame import *
import random as r 
import time, sys

pygame.init()
RUNNING = True
DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
LIST_DISPLAY_SIZE = list(DISPLAY_SIZE)
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
SCREENSIZE = DISPLAYSURF.get_size()
FONT = pygame.font.SysFont('Tahoma',int((SCREENSIZE[0]+SCREENSIZE[1])/40),False,False)
WHITE = pygame.Color(255,255,255) 
BLACK = pygame.Color(0,0,0)
TIMEDELAY = pygame.time.get_ticks()
ESC = False
HOVER = False
playerpos = (0,int(SCREENSIZE[1]/20))
DELAY2 = pygame.time.get_ticks()
movementdistx = 35
movementdisty = 35
movementspd = 100
collectables = []

def update():
    global HOVER, RUNNING, pressed_keys, playerpos, DELAY2, movementdist, movementspd, kpl, collectables
    SCREENSIZE = DISPLAYSURF.get_size()
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a] and pygame.time.get_ticks()>=DELAY2+movementspd and playerpos[0]>=movementdistx:
        DELAY2 = pygame.time.get_ticks()
        playerpos = (playerpos[0]-movementdistx,playerpos[1])
    if pressed_keys[K_d] and pygame.time.get_ticks()>=DELAY2+movementspd and playerpos[0]<=SCREENSIZE[0]-movementdistx:
        DELAY2 = pygame.time.get_ticks()
        playerpos = (playerpos[0]+movementdistx,playerpos[1])
    if pressed_keys[K_s] and pygame.time.get_ticks()>=DELAY2+movementspd and playerpos[1]<=SCREENSIZE[1]-movementdisty:
        DELAY2 = pygame.time.get_ticks()
        playerpos = (playerpos[0],playerpos[1]+movementdisty)
    if pressed_keys[K_w] and pygame.time.get_ticks()>=DELAY2+movementspd and playerpos[1]>=int(SCREENSIZE[1]/20)+movementdisty:
        DELAY2 = pygame.time.get_ticks()
        playerpos = (playerpos[0],playerpos[1]-movementdisty)
        
    if playerpos[0]>SCREENSIZE[0]-25: playerpos = (playerpos[0]-25,playerpos[1])
    if playerpos[1]>SCREENSIZE[1]-35: playerpos = (playerpos[0],playerpos[1]-35)
    
    DISPLAYSURF.fill(WHITE)

    pygame.draw.rect(DISPLAYSURF,pygame.Color(127,127,127),(0,0,SCREENSIZE[0],int(SCREENSIZE[1]/20)),0)
    
    pygame.draw.rect(DISPLAYSURF,pygame.Color(255,0,0),(playerpos[0]+5,playerpos[1],15,15),0)
    pygame.draw.rect(DISPLAYSURF,pygame.Color(0,255,0),(playerpos[0],playerpos[1]+10,5,15),0)
    pygame.draw.rect(DISPLAYSURF,pygame.Color(0,255,0),(playerpos[0]+20,playerpos[1]+10,5,15),0)
    pygame.draw.rect(DISPLAYSURF,pygame.Color(255,255,0),(playerpos[0]+5,playerpos[1]+15,7.5,20),0)
    pygame.draw.rect(DISPLAYSURF,pygame.Color(0,255,255),(playerpos[0]+12.5,playerpos[1]+15,8,20),0)
    
    # collectables
    if len(collectables)<1:
        collectables.append([r.randrange(0,SCREENSIZE[0],25),r.randrange(int(SCREENSIZE[1]/20),SCREENSIZE[1],35)])
    [pygame.draw.rect(DISPLAYSURF,pygame.Color(255,0,0),(i[0],i[1],25,35),0) for i in collectables]
    
    [collectables.remove(i) if playerpos[0]>i[0]-30 and playerpos[0]<i[0]+25 and playerpos[1]>i[1]-15 and playerpos[1]<i[1]+35 else "" for i in collectables]
    
    if ESC:
        if not HOVER:
            FONT = pygame.font.SysFont('Tahoma',int((SCREENSIZE[0]+SCREENSIZE[1])/40),False,False)
            pygame.draw.rect(DISPLAYSURF, pygame.Color(100,100,100), (2/6*SCREENSIZE[0],SCREENSIZE[1]/2-int(SCREENSIZE[1]/20),2/6*SCREENSIZE[0],SCREENSIZE[1]/10),0)
            buttontext = FONT.render("Escape",True,(0,0,0))
            DISPLAYSURF.blit(buttontext, (2/6*SCREENSIZE[0]+2/24*SCREENSIZE[0],SCREENSIZE[1]/2-int(SCREENSIZE[1]/20)))
            MOUSELOCATION = pygame.mouse.get_pos()
            if MOUSELOCATION[0]>2/6*SCREENSIZE[0] and MOUSELOCATION[0]<2/6*SCREENSIZE[0]+2/6*SCREENSIZE[0] and MOUSELOCATION[1]>SCREENSIZE[1]/2-int(SCREENSIZE[1]/20) and MOUSELOCATION[1]<SCREENSIZE[1]/2-int(SCREENSIZE[1]/20)+SCREENSIZE[1]/10:
                HOVER = True
        if HOVER:
            FONT = pygame.font.SysFont('Tahoma',int((SCREENSIZE[0]+SCREENSIZE[1])/35),False,False)
            pygame.draw.rect(DISPLAYSURF, pygame.Color(100,100,100), (5/18*SCREENSIZE[0],SCREENSIZE[1]/2-SCREENSIZE[1]/15,8/18*SCREENSIZE[0],SCREENSIZE[1]*2/15),0)
            buttontext = FONT.render("Escape",True,(0,0,0))
            DISPLAYSURF.blit(buttontext, (2/6*SCREENSIZE[0]+2/24*SCREENSIZE[0],SCREENSIZE[1]/2-int(SCREENSIZE[1]/20)))
            MOUSELOCATION = pygame.mouse.get_pos()
            if not (MOUSELOCATION[0]>5/18*SCREENSIZE[0] and MOUSELOCATION[0]<5/18*SCREENSIZE[0]+3/18*SCREENSIZE[0] and MOUSELOCATION[1]>SCREENSIZE[1]/2-SCREENSIZE[1]/15 and MOUSELOCATION[1]<SCREENSIZE[1]/2-SCREENSIZE[1]/15+SCREENSIZE[1]*2/15):
                HOVER = False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN: 
                    RUNNING = False
    pygame.display.update()

while RUNNING:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  RUNNING = False
    if pressed_keys[K_ESCAPE] and not ESC and pygame.time.get_ticks()>TIMEDELAY+500: 
        ESC = True
        TIMEDELAY = pygame.time.get_ticks()
    if pressed_keys[K_ESCAPE] and ESC and pygame.time.get_ticks()>TIMEDELAY+500: 
        ESC = False
        TIMEDELAY = pygame.time.get_ticks()
    
    update()

