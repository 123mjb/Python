import random as r

wordlength = 0
wrdplce = 0
number = 58110
file = open("EveryWordInTheEnglishLanguage.txt", "r")
string = file.read()
list = string.split("\n")
word = list[r.randint(0, number)]
for i in word:
    wordlength += 1
prnt = "_" * wordlength
while prnt != word:
    print(prnt)
    letter = input()
    for y in word:
        if letter == y:
            prnt = prnt.replace(wrdplce, word[wrdplce])
        wrdplce += 1

