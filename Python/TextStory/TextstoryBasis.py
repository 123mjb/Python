import random as r
def printvalues(lst, lst2):
    for i in range(0, 4):
        print(lst[i], "is", lst2[i])
def addvalues(values, addlst):
    for i in range(0, 4):
        values[i] += addlst[i]
def chooseupgrade(values, b, w, h, t):
    inpt = input()
    for i in range(0, 4):
        if inpt == "b":
            values[i] += b[i]
        elif inpt == "w":
            values[i] += w[i]
        elif inpt == "h":
            values[i] += h[i]
        elif inpt == "t":
            values[i] += t[i]
    return values
def FoundBlank(Found,values,Goodvals,Badvals,MChance,HChance):
    print("You found a", Found, ".")
    work = True
    while work:
        Choise=input("Do you want to steal/take (Y/N).\n")
        if Choise == "Y" or Choise == "y":
            if r.randrange(0, HChance)<MChance:
                values = addvalues(values, Goodvals)
            else:
                values = addvalues(values, Badvals)
            work = False
        elif Choise == "N" or Choise == "n":
            True
        else:
            work = True
    return values

