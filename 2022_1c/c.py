P = 10 ** 9+7

bigM = 5*10**5

def recip(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    if b == 0:
        return 1, 0, a
    else:
        while (r != 0):
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
    return old_s % b

recip_list = [recip(i, P) for i in range(bigM+10)]


def doit():
    [n, k] = [int(x) for x in input().split()]
    p = [[0] * (k+1) for _ in range(n+1)]
    p[0][0] = 1
    for l in range(0, n*(n-1)//2+1):
        for i in range(1, n+1):
            for j in range(0, k+1):
                for l0 in range(0, l)
                p[i][j] = (n-i) * (i) * p[i-1][j]
                if (i >= 2 and j >= 1):
                    p[i][j] += (i-1) * i // 2 * p[i-2][j-1]
    print(p)
    return p[n][k]


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))