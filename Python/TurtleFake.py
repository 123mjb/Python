import pygame
from pygame import *
import random as r
pygame.init()
DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
LIST_DISPLAY_SIZE = list(DISPLAY_SIZE)
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
# pygame.display.toggle_fullscreen()
WHITE = pygame.Color(255,255,255) 
BLACK = pygame.Color(0,0,0)
DISPLAYSURF
# pygame.FULLSCREEN
print(tuple(map(lambda i, j: i - j, pygame.display.get_desktop_sizes()[0], (10,10))))
turtle = (0,0)
pygame.display.set_caption("Draw")
icon = pygame.image.load("Python/R.png")
pygame.display.set_icon(icon)
move=0
M_w=False
M_a=False
M_s=False
M_d=False
randommove=False

def turtle_randommove():
    move = r.randrange(0,3)
    if move == 0:
        M_w = True
    elif move == 1:
        M_a = True
    elif move == 2:
        M_s = True
    elif move == 3:
        M_d = True

def turtle_move(turtle1):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a]or M_a==True:
        t=list(turtle1)
        if t[0]>0 and t[0]<LIST_DISPLAY_SIZE[0]-6:
            t[0]-=1
        turtle1=tuple(t)
    if pressed_keys[K_d] or M_d==True:
        t=list(turtle1)
        if t[0]>-1 and t[0]<LIST_DISPLAY_SIZE[0]-7:
            t[0]+=1
        turtle1=tuple(t)
    if pressed_keys[K_s] or M_s==True:
        t=list(turtle1)
        if t[1]>-1 and t[1]<LIST_DISPLAY_SIZE[1]-75:
            t[1]+=1
        turtle1=tuple(t)
    if pressed_keys[K_w] or M_w==True:
        t=list(turtle1)
        if t[1]>0 and t[1]<LIST_DISPLAY_SIZE[1]-74:
            t[1]-=1
        turtle1=tuple(t)
    return turtle1
def turtle_display(turtle2):
    pygame.draw.rect(DISPLAYSURF,BLACK,(list(turtle2)[0],list(turtle2)[1],5,5),0)
DISPLAYSURF.fill(WHITE)

running  = True

while running: 
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_i]: 
        if randommove: randommove=False
        elif not randommove: randommove=True
    if randommove: turtle_randommove()
    # DISPLAYSURF.fill(WHITE)
    turtle = turtle_move(turtle)
    turtle_display(turtle)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False
    if pressed_keys[K_p]:
        pygame.display.toggle_fullscreen()
        DISPLAYSURF.fill(WHITE)
    if pressed_keys[K_c]:
        DISPLAYSURF.fill(WHITE)
    pygame.display.update()
    print(M_w,M_a,M_s,M_d)
    M_w,M_a,M_s,M_d= False,False,False,False
    # print(turtle)