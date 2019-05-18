class ans_solver():

    def __init__(self):
        [self.n, self.m] = [int(x) for x in input().split()]
        self.map = [input() for i in range(self.n)]
        self.dp = [[[[0] * self.m for i in range(self.m)] for j in range(self.n)] for k in range(self.n)]
        self.legal = [[[[None] * self.m for i in range(self.m)] for j in range(self.n)] for k in range(self.n)]

    def doit(self):
        for i in range(0, self.n):
            for j in range(0, self.m):
                for x1 in range(0, self.n - i):
                    x2 = x1 + i
                    for y1 in range(0, self.m - j):
                        y2 = y1 + j
                        possible_way = self.check(x1, x2, y1, y2)
        return possible_way

    def check(self, x1, x2, y1, y2):
        possible_way = 0
        sg_next_set = set([])
        # print('check', x1, x2, y1, y2)
        for i in range(x1, x2 + 1):
            if self.if_legal(i, i, y1, y2):
                up = self.get(x1, i - 1, y1, y2)
                down = self.get(i + 1, x2, y1, y2)
                sg_next = up ^ down
                sg_next_set.add(sg_next)
                # print('ud', i, i, y1, y2, up, down, sg_next)
                if sg_next == 0:
                    possible_way += y2 - y1 + 1
        for i in range(y1, y2 + 1):
            if self.if_legal(x1, x2, i, i):
                left = self.get(x1, x2, y1, i - 1)
                right = self.get(x1, x2, i + 1, y2)
                sg_next = left ^ right
                sg_next_set.add(sg_next)
                # print('lr', x1, x2, i, i, left, right, sg_next)
                if sg_next == 0:
                    possible_way += x2 - x1 + 1
        for i in range(50):
            if i not in sg_next_set:
                sg = i
                break
        self.dp[x1][x2][y1][y2] = sg
        # print(x1, x2, y1, y2, sg, sg_next_set)
        return possible_way

    def get(self, x1, x2, y1, y2):
        # print('get', x1, x2, y1, y2)
        if x1 > x2:
            return 0
        if y1 > y2:
            return 0
        # print('get', x1, x2, y1, y2, self.dp[x1][x2][y1][y2])
        return self.dp[x1][x2][y1][y2]

    def if_legal(self, x1, x2, y1, y2):
        if self.legal[x1][x2][y1][y2] is not None:
            return self.legal[x1][x2][y1][y2]
        legal = True
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if self.map[i][j] == '#':
                    legal = False
        self.legal[x1][x2][y1][y2] = legal
        # print(x1, x2, y1, y2, legal)
        return self.legal[x1][x2][y1][y2]


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print('Case #{}: {}'.format(i, ans_solver().doit()))
