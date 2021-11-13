import random as r
import tkinter as tk


wrongs = 0
hangman = ""
hangmen = []
updatehangman = 0
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
        updatehangman+=1
    wrongs = 0
    for j in updatehangman:
        hangman += hangmen[j]

