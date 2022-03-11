import pygame
from pygame import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,400),pygame.RESIZABLE)
# pygame.display.toggle_fullscreen()










running  = True

while running:  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False