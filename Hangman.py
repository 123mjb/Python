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
    wrdplce = 0
    if wrongs == wordlength:
        uh+=1
    wrongs = 0
    if uh == 1: # bottom plank
        for j in range(30, 35):
            hangmen[j] = h[j]
    elif uh == 2: # side plank
        hangmen[0] = h[0]
        hangmen[5] = h[5]
        hangmen[10] = h[10]
        hangmen[15] = h[15]
        hangmen[20] = h[20]
        hangmen[25] = h[25]
    elif uh == 3: # top plank
        hangmen[1] = h[1]
        hangmen[2] = h[2]
        hangmen[3] = h[3]
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
    if hangmen == h:
        print("You lost!")
        sys.exit
