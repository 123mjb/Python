import random as r

number = 58110
file = open("EveryWordInTheEnglishLanguage.txt", "r")
string = file.read()
list = string.split("\n")
word = list[r.randint(0, number)]
print(word)