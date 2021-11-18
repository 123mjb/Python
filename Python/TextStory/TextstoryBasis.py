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