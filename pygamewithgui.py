import pygame
from pygame import *
import random as r 
import time, sys

pygame.init()
running = True
DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
LIST_DISPLAY_SIZE = list(DISPLAY_SIZE)
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
screensize = DISPLAYSURF.get_size()
font = pygame.font.SysFont('Tahoma',int((screensize[0]+screensize[1])/40),False,False)
WHITE = pygame.Color(255,255,255) 
BLACK = pygame.Color(0,0,0)
timedelay = pygame.time.get_ticks()
esc = False
hover = False
playerpos = (0,screensize[1]/20)

def update():
    global hover, running
    screensize = DISPLAYSURF.get_size()

    DISPLAYSURF.fill(WHITE)

    pygame.draw.rect(DISPLAYSURF,pygame.Color(127,127,127),(0,0,screensize[0],screensize[1]/20),0)
    
    pygame.draw.rect(DISPLAYSURF)

    if esc:
        if not hover:
            font = pygame.font.SysFont('Tahoma',int((screensize[0]+screensize[1])/40),False,False)
            pygame.draw.rect(DISPLAYSURF, pygame.Color(100,100,100), (2/6*screensize[0],screensize[1]/2-screensize[1]/20,2/6*screensize[0],screensize[1]/10),0)
            buttontext = font.render("Escape",True,(0,0,0))
            DISPLAYSURF.blit(buttontext, (2/6*screensize[0]+2/24*screensize[0],screensize[1]/2-screensize[1]/20))
            mouselocation = pygame.mouse.get_pos()
            if mouselocation[0]>2/6*screensize[0] and mouselocation[0]<2/6*screensize[0]+2/6*screensize[0] and mouselocation[1]>screensize[1]/2-screensize[1]/20 and mouselocation[1]<screensize[1]/2-screensize[1]/20+screensize[1]/10:
                hover = True
        if hover:
            font = pygame.font.SysFont('Tahoma',int((screensize[0]+screensize[1])/35),False,False)
            pygame.draw.rect(DISPLAYSURF, pygame.Color(100,100,100), (5/18*screensize[0],screensize[1]/2-screensize[1]/15,8/18*screensize[0],screensize[1]*2/15),0)
            buttontext = font.render("Escape",True,(0,0,0))
            DISPLAYSURF.blit(buttontext, (2/6*screensize[0]+2/24*screensize[0],screensize[1]/2-screensize[1]/20))
            mouselocation = pygame.mouse.get_pos()
            if not (mouselocation[0]>5/18*screensize[0] and mouselocation[0]<5/18*screensize[0]+3/18*screensize[0] and mouselocation[1]>screensize[1]/2-screensize[1]/15 and mouselocation[1]<screensize[1]/2-screensize[1]/15+screensize[1]*2/15):
                hover = False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN: 
                    running = False
    pygame.display.update()

while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  running = False
    if pressed_keys[K_ESCAPE] and not esc and pygame.time.get_ticks()>timedelay+500: 
        esc = True
        timedelay = pygame.time.get_ticks()
    if pressed_keys[K_ESCAPE] and esc and pygame.time.get_ticks()>timedelay+500: 
        esc = False
        timedelay = pygame.time.get_ticks()
    update()

