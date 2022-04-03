from random import random

# So consider a troublesome case where most rooms have low degree, and a small set of rooms have high degree — few enough that we are unlikely to find one of them by teleporting randomly.
def doit():
    [n, k] = [int(x) for x in input().split()]
    if (n <= k + 1):
        [r, p] = [int(x) for x in input().split()]
        sum = p
        for i in range(1, n+1):
            if (i != r):
                print('T {}'.format(i))
                [rx, px] = [int(x) for x in input().split()]
                sum += px
        print('E {}'.format(sum//2))
    else:
        [r, p] = [int(x) for x in input().split()]
        sum = p
        randomList = getRandomList(n, r)
        for i in range(1, k+1):
            print('T {}'.format(randomList[i][1]))
            [rx, px] = [int(x) for x in input().split()]
            sum += px
        print('E {}'.format(round(sum*n/2/(k+1))))

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
