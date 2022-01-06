from ctypes import string_at
import pygame, sys, random as r
from pygame.locals import *

pygame.init()

string2 = ""
numbers = "1234567890"
wordlength = 0
guessedwordlength = 0
FPS = 60
FramePerSec = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('comicsansms', 32)

DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Question")

def multiplication():
    global wordlength
    number1=r.randrange(0, 12)
    number2=r.randrange(0, 12)
    answer=number1*number2
    wordlength=len(answer)
    questionbox = "■" * wordlength
    pygame.font.Font.render(questionbox)
def strchangecertainletter(string, ltrnumber, changeto):
    new = list(string)
    new[ltrnumber] = changeto
    return "".join(str(new))
def input():
    global questionbox
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_1]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 1)
    if pressed_keys[K_2]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 2)
    if pressed_keys[K_3]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 3)
    if pressed_keys[K_4]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 4)
    if pressed_keys[K_5]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 5)
    if pressed_keys[K_6]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 6)
    if pressed_keys[K_7]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 7)
    if pressed_keys[K_8]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 8)
    if pressed_keys[K_9]:
        questionbox = strchangecertainletter(questionbox, guessedwordlength, 9)
        
number1=r.randrange(0, 12)
number2=r.randrange(0, 12)
answer=number1*number2
wordlength=len(str(answer))
questionbox = "■" * wordlength    
    
    
    
while True:
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    input()
    for o in questionbox:
        string2 += o
    text = pygame.font.Font.render(font, string2, True, BLACK)
    string2 = ""
    DISPLAYSURF.blit(text, (5, 5))
    pygame.display.update()
    FramePerSec.tick(FPS)