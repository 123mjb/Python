import random
count = 0



def grn(l, m):
    return random.randrange(l, m)
# print(grn(int(input()), int(input())))
def splt(t, s):
    x = t.split(s)
    return x
# print(splt(input(), input()))
def file():
    f = input("\n File name")
    fl = f + ".txt"
    fil = open(fl, "w")
    fil.write(input("\n File write"))
# file()
def randr(n):
    global count
    if count == 10:
        return random.randrange(1, n)
    count += 1
    return random.randrange(1, randr(n))
# print(randr(int(input())))
def shout(p):
    s = str(p)
    print(s.upper() + "!")
# shout(input())
def amount(h):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in h:
        if i.isupper():
            count1 += 1
        if i.islower():
            count2 += 1
        if i.isspace():
            count3 += 1
    print("There are " + str(count1) + " uppercase letters.")
    print("There are " + str(count2) + " lowercase letters.")
    print("There are " + str(count3) + " spaces.")
# amount(input())
def inpt(*args):
    inp = input(*args)
    print(inp)
# inpt("hello \n")
def hello():
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    h = ""
    h += "h"
    h += "e"
    h += "l"
    h += "l"
    h += "o"
    print(h)
hello()
