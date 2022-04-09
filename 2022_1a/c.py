INF = 10**8
def dist(a, b, n):
    aList = []
    bList = []
    while(a > 0):
        aList.append(a%n)
        a = a// n
    while(b > 0):
        bList.append(b%n)
        b = b// n
    aLen = len(aList)
    bLen = len(bList)
    k = 0
    for i in range(min(aLen, bLen)):
        if (aList[i] == bList[i]):
            k += 1
    return aLen - k + bLen - k

def check(x, list):
    cnt = [0] * len(list)
    n = len(list)
    while(x > 0):
        cnt[x%n] += 1
        x = x // n
    for i in range(n):
        if(cnt[i] != list[i]):
            return False
    return True

def generate(list):
    out = []
    for i in range(len(list)**sum(list)):
        if(check(i, list)):
            out.append(i)
    return out

def simple(x):
    last = 0
    out = 0
    for i in range(x):
        now = int(input())
        out += abs(now - last)
        last = now
    return out + last

def doit():
    [e, w] = [int(x) for x in input().split()]
    last = {0: 0}

    if w == 1:
        return simple(e)
    for i in range(e):
        step = [int(x) for x in input().split()]
        possible = generate(step)
        next = {}
        for i in possible:
            now = INF
            for j in last.keys():
                now = min(last[j] + dist(i, j, w), now)
            next[i] = now
        last = next
    
    now = INF
    for j in last.keys():
        now = min(last[j] + dist(0, j, w), now)
    return now

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
    