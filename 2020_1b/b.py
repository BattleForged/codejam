from logging.handlers import WatchedFileHandler
from pickle import TRUE


maxInt = 10**9
enumList = [-5 * 10 ** 8, 0, 5 * 10 ** 8]
HIT, MISS, CENTER, WRONG = "HIT", "MISS", "CENTER", "WRONG"

isWrong = False

f = open('out.txt', 'w')

def nextDo(x, y):
    global isWrong
    print(f'{-maxInt} {y}')
    a = (0, 0)
    result = input()
    if (result == WRONG):
        isWrong = TRUE
        return
    if (result == HIT):
        a = (-maxInt, y)
    else:
        l = -maxInt
        r = x
        while(l < r):
            mid = (l + r)//2
            print(f'{mid} {y}')
            result = input()
            if (result == CENTER):
                return
            if (result == WRONG):
                isWrong = TRUE
                return
            if (result == HIT):
                r = mid
            if (result == MISS):
                l = mid + 1
        a = (r, y)
    
    print(f'{maxInt} {y}')
    b = (0, 0)
    result = input()
    if (result == WRONG):
        isWrong = TRUE
        return
    if (result == HIT):
        b = (maxInt, y)
    else:
        l = x
        r = maxInt
        while(l < r):
            mid = (l + r + 1)//2
            print(f'{mid} {y}')
            result = input()
            if (result == CENTER):
                return
            if (result == WRONG):
                isWrong = TRUE
                return
            if (result == HIT):
                l = mid
            if (result == MISS):
                r = mid - 1
        b = (l, y)
    
    print(f'{x} {-maxInt}')
    c = (0, 0)
    result = input()
    if (result == WRONG):
        isWrong = TRUE
        return
    if (result == HIT):
        c = (x, -maxInt)
    else:
        l = -maxInt
        r = y
        while(l < r):
            mid = (l + r)//2
            print(f'{x} {mid}')
            result = input()
            if (result == CENTER):
                return
            if (result == WRONG):
                isWrong = TRUE
                return
            if (result == HIT):
                r = mid
            if (result == MISS):
                l = mid + 1
        c = (x, r)
    
    print(f'{x} {maxInt}')
    d = (0, 0)
    result = input()
    if (result == WRONG):
        isWrong = TRUE
        return
    if (result == HIT):
        d = (x, maxInt)
    else:
        l = y
        r = maxInt
        while(l < r):
            mid = (l + r + 1)//2
            print(f'{x} {mid}')
            result = input()
            if (result == CENTER):
                return
            if (result == WRONG):
                isWrong = TRUE
                return
            if (result == HIT):
                l = mid
            if (result == MISS):
                r = mid - 1
        d = (x, l)
    
    x = (a[0] + b[0]) // 2
    y = (c[1] + d[1]) // 2
    for i in [x-2, x-1, x, x+1, x+2]:
        for j in [y-2, y-1, y, y+1, y+2]:
            print(f'{i} {j}')
            
            result = input()
            if (result == CENTER):
                return
            if (result == WRONG):
                isWrong = TRUE
                return
    print(f'{2 * maxInt} {2 * maxInt}')
    result = input()
    isWrong = TRUE
    return


def doit():
    global isWrong
    for i in enumList:
        for j in enumList:
            if isWrong:
                return
            print(f'{i} {j}')
            result = input()
            if (result == CENTER):
                return
            if (result == HIT):
                return nextDo(i, j)
            if (result == WRONG):
                isWrong = TRUE
                return



def batchDo():
    [T, a, b] = [int(x) for x in input().split()]
    for t in range(1, T + 1):
        doit()

batchDo()