class Tool(object):

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = [[False] * m for i in range(n)]

    def search_all(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.search(i, j, 1):
                    # print(i, j)
                    return True
        return False

    def search(self, a, b, depth):
        if depth == self.n*self.m:
            return True
        perhaps = False
        self.map[a][b] = True
        for i in range(self.n):
            for j in range(self.m):
                if (i != a) and (j != b) and (i - j != a - b) and (i + j != a + b) and not self.map[i][j]:
                    if self.search(i, j, depth+1):
                        # print(i, j)
                        self.map[a][b] = False
                        return True
        self.map[a][b] = False
        return False


for i in range(1, 20):
    for j in range(1, 20):
        print(f'{i}, {j}: {Tool(i,j).search_all()}')
