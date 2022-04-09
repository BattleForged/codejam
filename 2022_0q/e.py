from random import random


def doit():
    [n, k] = [int(x) for x in input().split()]
    if (n <= k + 1):
        [r, p] = [int(x) for x in input().split()]
        pByT = p
        for i in range(1, n+1):
            if (i != r):
                print('T {}'.format(i))
                [rx, px] = [int(x) for x in input().split()]
                pByT += px
        print('E {}'.format(pByT//2))
    else:
        [r, p] = [int(x) for x in input().split()]
        pKnown = [0] * n
        pKnown[r-1] = p
        pByT = p
        randomList = getRandomList(n, r)
        for i in range(1, k//2+1):
            print('W')
            [rx, px] = [int(x) for x in input().split()]
            pKnown[rx-1] = px
            print('T {}'.format(randomList[i][1]))
            [rx, px] = [int(x) for x in input().split()]
            pKnown[rx-1] = px
            pByT += px
        knownRoomCnt = sum(i > 0 for i in pKnown)
        print('E {}'.format(round(pByT*(n-knownRoomCnt)/2/(k//2+1))+sum(pKnown)//2))

def getRandomList(n, r):
    randomP = []
    for i in range(n):
        randomP.append((random(), i+1))
    randomP[r-1] = (-1, r)
    randomP.sort()
    return randomP

T = int(input())
for t in range(1, T + 1):
    doit()
