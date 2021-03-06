import pygame;from pygame import *;import random as r ;import time;pygame.init();DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0];LIST_DISPLAY_SIZE = list(DISPLAY_SIZE);DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE);font = pygame.font.SysFont('Tahoma', 30, False, False);WHITE = pygame.Color(255,255,255) ;BLACK = pygame.Color(0,0,0);colourused = 0;size=4;clicking=False;timeschecked=0;heightofhud=45;COLOURS=[pygame.Color(0,0,0),pygame.Color(255,255,255),pygame.Color(255,0,0),pygame.Color(0,255,0),pygame.Color(0,0,255),pygame.Color(255,255,0),pygame.Color(255,0,255),pygame.Color(0,255,255),pygame.Color(127,127,127),pygame.Color(255,127,0),];COLOURSNOTDOT=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(127,127,127),(255,127,0)];print(tuple(map(lambda i, j: i - j, pygame.display.get_desktop_sizes()[0], (10,10))));turtle = (int(size/2),int(heightofhud+size/2));pygame.display.set_caption("Draw");icon = pygame.image.load("Python/R.png");pygame.display.set_icon(icon);move=0;M_w=False;M_a=False;M_s=False;M_d=False;randommove=False;checker = True;
def turtle_move(turtle1):
    global M_a,M_d,M_s,M_w
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a]or M_a==True:
        t=list(turtle1)
        if t[0]>0 and t[0]<LIST_DISPLAY_SIZE[0]-3:
            if randommove:t[0]-=size
            else:t[0]-=1
        turtle1=tuple(t)
    if pressed_keys[K_d] or M_d:
        t=list(turtle1)
        if t[0]>-1 and t[0]<LIST_DISPLAY_SIZE[0]-4-size:
            if randommove:t[0]+=size
            else:t[0]+=1
        turtle1=tuple(t)
    if pressed_keys[K_s] or M_s:
        t=list(turtle1)
        if t[1]>heightofhud-1+size/2 and t[1]<LIST_DISPLAY_SIZE[1]-72-size:
            if randommove:t[1]+=size
            else:t[1]+=1
        turtle1=tuple(t)
    if pressed_keys[K_w] or M_w:
        t=list(turtle1)
        if t[1]>heightofhud+size/2 and t[1]<LIST_DISPLAY_SIZE[1]-71:
            if randommove:t[1]-=size
            else:t[1]-=1
        turtle1=tuple(t)
    return turtle1
turtle_displaylambda = lambda turtle2: pygame.draw.rect(DISPLAYSURF,COLOURS[colourused],(int(list(turtle2)[0]-size/2),int(list(turtle2)[1]-size/2),size,size),0)
def colourchanging():
    global colourused, pressed_keys
    if pressed_keys[K_1]:
        colourused = 0
    if pressed_keys[K_2]:
        colourused = 1
    if pressed_keys[K_3]:
        colourused = 2
    if pressed_keys[K_4]:
        colourused = 3
    if pressed_keys[K_5]:
        colourused = 4
    if pressed_keys[K_6]:
        colourused = 5
    if pressed_keys[K_7]:
        colourused = 6
    if pressed_keys[K_8]:
        colourused = 7
    if pressed_keys[K_9]:
        colourused = 8
    if pressed_keys[K_0]:
        colourused = 9
DISPLAYSURF.fill(WHITE)
def HUD():
    pygame.draw.rect(DISPLAYSURF,COLOURS[8],(0,0,LIST_DISPLAY_SIZE[0]-2,heightofhud),0)
    text = font.render(str(size), True,(0,0,0))
    DISPLAYSURF.blit(text, (int((LIST_DISPLAY_SIZE[0]-2)*2/3), 5))
running  = True
while running: 
    pressed_keys = pygame.key.get_pressed()# getting pressed keys
    if pressed_keys[K_i]: 
        if randommove: randommove=False
        elif not randommove: randommove=True
        time.sleep(1)
    if randommove:
        while checker:
            move = r.randrange(0,4)
            print(turtle,move,LIST_DISPLAY_SIZE)
            if move == 0:
                if list(turtle)[1]>heightofhud+3/2*size:
                    if DISPLAYSURF.get_at((list(turtle)[0],list(turtle)[1]-(size)))!=COLOURSNOTDOT[colourused]:
                        checker = False
                        M_w = True
            elif move == 1:
                if list(turtle)[0]>3/2*size:
                    if DISPLAYSURF.get_at((list(turtle)[0]-(size),list(turtle)[1]))!=COLOURSNOTDOT[colourused]:
                        checker = False
                        M_a = True
            elif move == 2:
                if list(turtle)[1]<int(LIST_DISPLAY_SIZE[1]-(65+3/2*size)):
                    if DISPLAYSURF.get_at((list(turtle)[0],list(turtle)[1]+(size)))!=COLOURSNOTDOT[colourused]:
                        checker = False
                        M_s = True
            elif move == 3:
                if list(turtle)[0]<LIST_DISPLAY_SIZE[0]-(7+3/2*size):
                    if DISPLAYSURF.get_at((list(turtle)[0]+(size),list(turtle)[1]))!=COLOURSNOTDOT[colourused]:
                        checker = False
                        M_d = True
            timeschecked+=1
            if timeschecked==64:turtle = (r.randrange(heightofhud+1/2*size,LIST_DISPLAY_SIZE[0]-7,size),r.randrange(heightofhud+1/2*size,LIST_DISPLAY_SIZE[1]-77,size));checker=False
        checker = True;timeschecked=0
    colourchanging();turtle = turtle_move(turtle);turtle_displaylambda(turtle)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:running = False
        if event.type == MOUSEBUTTONDOWN:clicking = True
        if event.type == MOUSEBUTTONUP:clicking = False
    if clicking:turtle = pygame.mouse.get_pos()
    if pressed_keys[K_p]:pygame.display.toggle_fullscreen();DISPLAYSURF.fill(WHITE)
    if pressed_keys[K_c]:DISPLAYSURF.fill(WHITE)
    if pressed_keys[K_UP] and size<100:size+=1;time.sleep(0.125)
    if pressed_keys[K_DOWN] and size>0:size-=1;time.sleep(0.125)
    if pressed_keys[K_b]:DISPLAYSURF.fill(BLACK)
    HUD();pygame.display.update();M_w,M_a,M_s,M_d= False,False,False,False