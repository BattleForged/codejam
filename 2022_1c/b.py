def doit():
    [n, k] = [int(x) for x in input().split()]
    e = [int(x) for x in input().split()]
    a = 0
    for i in range(n):
        for j in range(i+1, n):
            a += e[i] * e[j]
    b = sum(e)
    # k = 1 -> A + BX = 0
    if k == 1:
        if b == 0:
            if a == 0:
                return '0'
            else:
                return 'IMPOSSIBLE'
        else:
            if a % b == 0:
                return f'{-a//b}'
            else:
                return 'IMPOSSIBLE'

    # k > 2 -> A + B(X+Y) + XY = 0 -> Y = -(A+BX) / (B+X)
    else:
        return f'{1-b} {b*b - a - b}'

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))