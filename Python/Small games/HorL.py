import random, os

print("Would you like to play a game?")
answer = input()
if answer == "yes" or answer == "Yes":
    print("What do you want the max number to be?")
    max = int(input())
    num = random.randrange(1, max)
    nc = False
    tries = 0
    while nc != True:
        tries += 1
        print("Choose a number from 1 to " + max)
        choice = int(input())
        if choice == num:
            nc = True
        else:
            if choice > num:
                print("Lower")
            else:
                print("Higher")
    print("You got it in " + str(tries) + " goes!")
else:
    print("Well bye then.")
    os.abort


