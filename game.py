# from Python.TurtleFake import DISPLAYSURF
# from Platformer import Player
# from Platformer import P1
import pipes
import pygame
from pygame import *
from pygame.locals import *
import time,sys, random as r

pygame.init()
vec = pygame.math.Vector2
FramePerSec = pygame.time.Clock()

DISPLAY_SIZE = pygame.display.get_desktop_sizes()[0]
DISPLAYSURF = pygame.display.set_mode(tuple(map(lambda i, j: i - j, DISPLAY_SIZE, (2,60))),pygame.RESIZABLE)
ACC = 1
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
        self.jumping = False
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
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        if pressed_keys[K_s]:
            movedown = 2
        else:
            movedown = 1
        if self.pos.y*movedown > abs(movedown*4*self.vel.y)+abs(movedown*2*self.acc.y):
            self.pos.y += movedown*self.vel.y + movedown*0.5 * self.acc.y
         
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
        if self.vel.y>5:
            self.vel.y = 4
            self.jumping = False

class pipes():
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(12,r.randint(50,100))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (r.randint(0,DISPLAYSURF.get_size()[0]-10),
                                                r.randint(0,DISPLAYSURF.get_size()[1]-20)))
        self.speed = r.randint(-1,1)
        self.point = True   
        self.moving = True
    
    def move(self):
        if self.moving == True:
            self.rect.move_ip(self.speed,0 )
            if self.speed >0 and self.rect.left > DISPLAYSURF.get_size()[0]:
                    self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = DISPLAYSURF.get_size()[0]

 
def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False

def plat_gen():
    while len(pipesnum) < 6:
        width = r.randrange(50,100)
        p  = pipes()      
        C = True
         
        while C:
            p = pipes()
            p.rect.center = (r.randrange(DISPLAYSURF.get_size()[1] - width,0),
                            r.randrange(-50, 0))
            C = check(p, pipesnum)
        pipesnum.add(p)
        all_sprites.add(p)

P1 = player()
PT1 = pipes()

PT1.surf = pygame.Surface((DISPLAYSURF.get_size()[0], 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (DISPLAYSURF.get_size()[0]/2, DISPLAYSURF.get_size()[1] - 10))
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
pipesnum = pygame.sprite.Group()
pipesnum.add(PT1)

PT1.moving = False
PT1.point = False

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
