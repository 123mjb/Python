import random as r
import tkinter as tk


wrongs = 0
pront = ""
hangman = ""
hangmen = [
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
    " ", " ", " ", " ", " ", 
]
h = [
    "+", "-", "-", "+", " ", 
    "|", " ", " ", "|", " ", 
    "|", " ", " ", "0", " ", 
    "|", " ", "/", "|", "\\", 
    "|", " ", "/", " ", "\\", 
    "|", " ", " ", " ", " ", 
    "+", "-", "-", "-", "+", 
]
uh = 0
wordlength = 0
wrdplce = 0
number = 58110
file = open("EveryWordInTheEnglishLanguage.txt", "r")
string = file.read()
list1 = string.split("\n")
word = list1[r.randint(0, number)]
for i in word:
    wordlength += 1
prnt = "_" * wordlength
while prnt != word:
    print(prnt)
    letter = input()
    for y in word:
        if letter == y:
            new = list(prnt)
            new[wrdplce] = word[wrdplce]
            prnt = "".join(new)
        else:
            wrongs += 1 
        wrdplce += 1
    if wrongs == wordlength:
        uh+=1
    wrongs = 0
    if uh == 1:
        for j in range(31, 35):
            hangmen[j] = h[j]
    elif uh == 2:
        hangmen[1] = h[1]
        hangmen[6] = h[6]
        hangmen[11] = h[11]
        hangmen[16] = h[16]
        hangmen[21] = h[21]
        hangmen[26] = h[26]
        
    for k in range(1, 35): pront += hangmen[k]
    

