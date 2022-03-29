import random as r
new=[1,2,3,4,5,6,7,8,9]
hwile=0
while hwile<=100:
    new = [i+new[r.randrange(0,len(new))] for i in new]
    hwile+=1
print([i/(10**len(str(i))) for i in new])
