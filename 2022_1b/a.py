def doit(n):
    d = [int(x) for x in input().split()]
    l = 0
    r = n-1
    res = 0
    last = 0
    while(l <= r):
        if (d[l] < d[r]):
            res += 1 if d[l] >= last else 0
            last = max(last, d[l])
            l += 1
        else:
            res += 1 if d[r] >= last else 0
            last = max(last, d[r])
            r -= 1
    return res

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    print('Case #{}: {}'.format(t, doit(n)))
    