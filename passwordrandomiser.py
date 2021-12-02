import random as r

diction = {}
password = input()
new = ""
text = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_"
for l in text:
    diction[l] = r.randint(1, 1000000)
for o in password:
    new += str(diction[o])
print(new)
