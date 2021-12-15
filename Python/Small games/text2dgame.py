level1=[
    "■ ", "■ ", "■ ", "■ ", "■ ", "■ ", "■\n",
    "■ ", "⯐ ", "  ", "  ", "  ", "  ", "■\n",
    "■ ", "  ", "  ", "  ", "  ", "  ", "■\n",
    "■ ", "  ", "  ", "⛾ ", "  ", "  ", "■\n",
    "■ ", "  ", "  ", "  ", "  ", "  ", "■\n",
    "■ ", "  ", "  ", "  ", "  ", "  ", "■\n",
    "■ ", "■ ", "■ ", "■ ", "■ ", "■ ", "■\n",
]
playerpos=8
moveblockpos=24
pront=""
def move():
    global playerpos
    inpt=input()
    if inpt=="w":
        if level1[playerpos-7]!="■ " and level1[playerpos-7]!="■\n":
            if level1[playerpos-7]=="⛾ ":
                if moveblock(-7):
                    level1[playerpos]="  "
                    playerpos-=7
                    level1[playerpos]="⯐ "
            else:
                level1[playerpos]="  "
                playerpos-=7
                level1[playerpos]="⯐ "           
    elif inpt == "a":
        if level1[playerpos-1]!="■ " and level1[playerpos-1]!="■\n":
            if level1[playerpos-1]=="⛾ ":
                if moveblock(-1):
                    level1[playerpos]="  "
                    playerpos-=1
                    level1[playerpos]="⯐ "
            else:
                level1[playerpos]="  "
                playerpos-=1
                level1[playerpos]="⯐ " 
    elif inpt == "s":
        if level1[playerpos+7]!="■ " and level1[playerpos+7]!="■\n":
            if level1[playerpos+7]=="⛾ ":
                if moveblock(+7):
                    level1[playerpos]="  "
                    playerpos+=7
                    level1[playerpos]="⯐ "
            else:
                level1[playerpos]="  "
                playerpos+=7
                level1[playerpos]="⯐ " 
    elif inpt == "d":
        if level1[playerpos+1]!="■ " and level1[playerpos+1]!="■\n":
            if level1[playerpos+1]=="⛾ ":
                if moveblock(+1):
                    level1[playerpos]="  "
                    playerpos+=1
                    level1[playerpos]="⯐ "
            else:
                level1[playerpos]="  "
                playerpos+=1
                level1[playerpos]="⯐ "      
def moveblock(direct):
    global moveblockpos
    if level1[moveblockpos+direct]!="■ " and level1[moveblockpos+direct]!="■\n":
        level1[moveblockpos]="  "
        moveblockpos+=direct
        level1[moveblockpos]="⛾ "
        answer = True
    else:
        answer = False
    return answer
while True:
    for x in level1: pront+=x
    print(pront)
    pront=""
    move()