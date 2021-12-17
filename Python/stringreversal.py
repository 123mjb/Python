string = input()
stringlength = len(string)-1
outputstring = ""
for i in range(stringlength,-1,-1):
    outputstring += string[i]
    print(outputstring)
