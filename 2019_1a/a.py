class Choice(object):
    def __init__(self, a, b, value):
        self.a = a
        self.b = b
        self.value = value


def get_key(choice):
    return choice.value


class Tool(object):

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = [[False] * m for i in range(n)]
        self.not_bad_num = [[0] * m for i in range(n)]
        self.used = [{} for i in range(4)]
        for i in range(self.n):
            for j in range(self.m):
                self.use(i, j)
        for i in range(self.n):
            for j in range(self.m):
                self.not_bad_num[i][j] = n * m - (self.used[0][i] + self.used[1][j] + self.used[2][i + j] + self.used[3][i - j] - 3)
        for i in range(self.n):
            for j in range(self.m):
                self.clean(i, j)

    def use(self, a, b):
        self.map[a][b] = True
        if a not in self.used[0]:
            self.used[0][a] = 0
        self.used[0][a] += 1
        if b not in self.used[1]:
            self.used[1][b] = 0
        self.used[1][b] += 1
        if b + a not in self.used[2]:
            self.used[2][b + a] = 0
        self.used[2][b + a] += 1
        if a - b not in self.used[3]:
            self.used[3][a - b] = 0
        self.used[3][a - b] += 1

    def clean(self, a, b):
        self.map[a][b] = False
        self.used[0][a] -= 1
        self.used[1][b] -= 1
        self.used[2][b + a] -= 1
        self.used[3][a - b] -= 1

    def search_all(self):
        for i in range(self.n):
            for j in range(self.m):
                ret = self.search(i, j, 1)
                if ret is not None:
                    ret.append((i, j))
                    return ret
        return None

    def check_not_bad(self, i, j, depth):
        ret = self.not_bad_num[i][j] - depth
        return ret + self.used[0][i] + self.used[1][j] + self.used[2][i + j] + self.used[3][i - j]

    def check_not_good(self, i, j):
        ret = self.n * self.m - self.not_bad_num[i][j]
        return ret - (self.used[0][i] + self.used[1][j] + self.used[2][i + j] + self.used[3][i - j])

    def search(self, a, b, depth):
        if depth == self.n * self.m:
            return []
        self.use(a, b)
        choice_list = []
        for i in range(self.n):
            for j in range(self.m):
                if (i != a) and (j != b) and (i - j != a - b) and (i + j != a + b) and not self.map[i][j]:
                    choice_list.append(
                        Choice(
                            i, j, (
                                self.check_not_bad(i, j, depth),
                                self.used[2][i + j]+self.used[3][i - j],
                                self.used[0][i]+self.used[1][j]
                            )
                        )
                    )
        choice_list.sort(key=get_key, reverse=True)
        for choice in choice_list:
            ret = self.search(choice.a, choice.b, depth + 1)
            if ret is not None:
                ret.append((choice.a, choice.b))
                return ret
        self.clean(a, b)
        return None


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    [a, b] = [int(x) for x in input().split()]
    ans = Tool(a, b).search_all()
    if ans is None:
        print('Case #{}: IMPOSSIBLE'.format(i))
    else:
        print('Case #{}: POSSIBLE'.format(i))
        for (a, b) in ans:
            print('{} {}'.format(a+1, b+1))
