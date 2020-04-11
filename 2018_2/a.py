def doit(n, x):
    if sum(x) != n:
        return ''
    if x[0] < 1 or x[n-1] < 1:
        return ''
    now = 0
    to = [0] * n
    for i in range(n):
        if x[i] > 0:
            for j in range(x[i]):
                to[now] = i
                now += 1

    delta = [to[i] - i for i in range(n)]
    high = max([i if i>=0 else -i for i in delta])
    map = [['.' for j in range(n)] for i in range(high+1)]
    for i in range(n):
        if delta[i] >= 0:
            for j in range(delta[i]):
                map[j][j+i] = '\\'
        else:
            for j in range(-delta[i]):
                map[j][i-j] = '/'
    return [''.join(x) for x in map]




t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    x = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    map = doit(n, x)
    if map == '':
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
    else:
        high = len(map)
        print("Case #{}: {}".format(i, high))
        for j in range(high):
            print(map[j])
