class fraction():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, b):
        return self.x * b.y == self.y * b.x

    def __ne__(self, b):
        return self.__eq__(b)

    def __lt__(self, b):
        return self.x * b.y < self.y * b.x

    def __gt__(self, b):
        return b.__lt__(self)

    def __str__(self):
        return '{}/{}'.format(self.x, self.y)


def doit():
    n = int(input())
    x = [[int(x) for x in input().split()] for i in range(n)]

    mid_point = []
    for i in range(n):
        for j in range(n):
            if (j != i):
                a = x[j][0] - x[i][0]
                b = x[j][1] - x[i][1]
                if a <= 0 and b <= 0:
                    continue
                elif a >= 0 and b >= 0:
                    continue
                else:
                    if a > 0:
                        mid_point.append(fraction(-b, a))
                    else:
                        mid_point.append(fraction(b, -a))
    mid_point.sort()
    cnt = len(mid_point) + 1
    for i in range(1, len(mid_point)):
        if (mid_point[i] == mid_point[i-1]):
            cnt -= 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
