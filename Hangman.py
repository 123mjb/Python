import random as r
import sys

wrongs = 0
pront = ""
hangmen = [
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
    " ", " ", " ", " ", " \n", 
]
h = [
    "+", "-", "-", "+", " \n", 
    "|", " ", " ", "|", " \n", 
    "|", " ", " ", "0", " \n", 
    "|", " ", "/", "|", "\\\n", 
    "|", " ", "/", " ", "\\\n", 
    "|", " ", " ", " ", " \n", 
    "+", "-", "-", "-", "+\n", 
]
uh = 0
wordlength = 0
number = 58110
file = open("EveryWordInTheEnglishLanguage.txt", "r")
string = file.read()
list1 = string.split("\n")
word = list1[r.randint(0, number)]
for i in word:
    wordlength += 1
prnt = "_" * wordlength
while prnt != word:
    wrdplce = 0
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
    if uh == 1: # bottom plank
        for j in range(30, 35):
            hangmen[j] = h[j]
    elif uh == 2: # side plank
        for j in range(0, 30, 5): hangmen[j] = h[j]     
    elif uh == 3: # top plank
        for j in range(1, 4): hangmen[j] = h[j]
    elif uh == 4: # rope
        hangmen[8] = h[8]
    elif uh == 5: # head
        hangmen[13] = h[13]
    elif uh == 6: # torso
        hangmen[18] = h[18]
    elif uh == 7: # left arm
        hangmen[17] = h[17]
    elif uh == 8: # right arm
        hangmen[19] = h[19]
    elif uh == 9: # left leg
        hangmen[22] = h[22]
    elif uh == 10: # right leg
        hangmen[24] = h[24]
    for o in hangmen:
        pront += o
    print(pront)
    pront = ""
    if uh == 10: 
        print("You failed!")
        sys.exit
