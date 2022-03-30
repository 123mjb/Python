# from Python.TurtleFake import DISPLAYSURF
# from Platformer import Player
# from Platformer import P1
import pygame
from pygame.locals import *
import time,sys

pygame.init()
vec = pygame.math.Vector2
FramePerSec = pygame.time.Clock()

DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
ACC = 0.5
FRIC = -0.12
FPS = 60

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()

        self.pos=vec((10,360))
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.score=0

    def move(self):
        self.acc=vec(0,0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > DISPLAYSURF.get_size()[0]:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = DISPLAYSURF.get_size()[0]
             
        self.rect.midbottom = self.pos
    
    def jump(self):
        pressed_keys = pygame.key.get_pressed()
        if self.pos.y < DISPLAYSURF.get_size()[1] and pressed_keys[K_SPACE]:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self):
        if self.vel.y>0:
            self.vel.y = 0
            self.jumping = False

P1 = player()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

while True:
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()

    if P1.rect.top > DISPLAYSURF.get_size()[1]:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            DISPLAYSURF.fill((255,0,0))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((0,0,0))
    f = pygame.font.SysFont("Verdana", 20)     
    g  = f.render(str(P1.score), True, (123,255,0))   
    DISPLAYSURF.blit(g, (DISPLAYSURF.get_size()[0]/2, 10))   
     
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.surf, entity.rect)
        entity.move()
 
    pygame.display.update()
    FramePerSec.tick(FPS)
