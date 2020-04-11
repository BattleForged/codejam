def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def doit():
    n = int(input())
    x = [[int(x) for x in input().split()] for i in range(n)]
    pair_a = (-1, -1)
    pair_b = (-1, -1)
    for i in range(1, n):
        a = x[i][0] - x[i - 1][0]
        b = x[i][1] - x[i - 1][1]
        if a >= 0 and b >= 0:
            continue
        if a <= 0 and b <= 0:
            return 'IMPOSSIBLE'
        if a > 0:
            if pair_a[0] < 0 or (-b * pair_a[0]) > (-a * pair_a[1]):
                pair_a = (a, -b)
        if b > 0:
            if pair_b[1] < 0 or (-b * pair_b[0]) < (-a * pair_b[1]):
                pair_b = (-a, b)
    if pair_a[0] < 0 and pair_b[1] < 0:
        return '1 1'
    if pair_a[0] < 0:
        if pair_b[0] < pair_b[1]:
            return '1 1'
        else:
            return '1 {}'.format((pair_b[0]+1)//pair_b[1])
    if pair_b[1] < 0:
        if pair_a[0] > pair_a[1]:
            return '1 1'
        else:
            return '{} 1'.format((pair_a[1]+1)//pair_a[0])
    if pair_b[1]*pair_a[0] <= pair_b[0]*pair_a[1]:
        return 'IMPOSSIBLE'
    if pair_b[1] <= pair_b[0]:
        return '1 {}'.format((pair_b[0]+1)//pair_b[1])
    k1 = pair_b[0]*pair_a[1]
    k3 = pair_b[0]*pair_a[0]
    k2 = pair_a[0]*pair_b[1]
    k = (gcd(k1, k2), k3)
    k1 //= k
    k2 //= k
    k3 //= k
    if k1+1 < k3:
        return '{} {}'.format(k1, k2-1)
    else:
        return '{} {}'.format(2*k1, 2*k2-1)


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
