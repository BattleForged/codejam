def doit():
    n = int(input())
    x = [[int(x) for x in input().split()] for i in range(n)]
    k = sum([x[i][i] for i in range(n)])
    r = 0
    for i in range(n):   
        checked = [0] * (n+1)
        repeated = 0
        for j in range(n):
            checked[x[i][j]] += 1
            if checked[x[i][j]] > 1:
                repeated = 1
        r += repeated

    c = 0
    for i in range(n):   
        checked = [0] * (n+1)
        repeated = 0
        for j in range(n):
            checked[x[j][i]] += 1
            if checked[x[j][i]] > 1:
                repeated = 1
        c += repeated
    return '{} {} {}'.format(k, r, c)
        



T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))