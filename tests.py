from math import sqrt
hello=0
fibonacci=[1,1]
while hello<=10:
    fibonacci.append(fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])
    hello+=1
    print(fibonacci)
    print(sqrt(fibonacci[len(fibonacci)-1]))
