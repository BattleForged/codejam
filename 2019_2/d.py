def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def doit():
    n = int(input())
    x = [[int(x) for x in input().split()] for i in range(n)]
    start = [int(x) for x in input().split()]
    


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
