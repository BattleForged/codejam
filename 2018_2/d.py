def check(f,a,b):
    x = 1 if f[a][b] =='B' else 0
    x += 2 if f[a][b+1] =='B' else 0
    x += 4 if f[a+1][b] =='B' else 0
    x += 8 if f[a+1][b+1] =='B' else 0
    return x

def get(i,j,a,b):
    x = 0 if i<=a else 2
    x+= 0 if j<=b else 1
    return x


class dfs:
    def __init__(self,map,m,n):
        self.map = map
        self.m=m
        self.n=n
        self.pos = [[1,0],[0,1],[-1,0],[0,-1]]
        self.c=[[False for i in range(n)] for j in range(m)]
    def search(self):
        ret = 0
        for i in range(m):
            for j in range(n):
                if not self.c[i][j]:
                    now = self.s(i,j)
                    ret = max(now, ret)
        return  ret

    def s(self,a,b):
        if not self.map[a][b] or self.c[a][b]:
            return 0
        self.c[a][b] = True
        ret = 1
        for i,j in self.pos:
            if a+i in range(self.m) and b+j in range(self.n):
                if self.map[a+i][b+j] and not self.c[a+i][b+j]:
                    ret += self.s(a+i,b+j)
        return ret

def calculate(f,m,n,a,b,p):
    B = [0]*4
    W = [0]*4
    ret = 0
    for k in range(16):
        if p[k]:
            map = [[(((1<<get(i,j,a,b))|k) == k)==(f[i][j] == 'B') for i in range(n)] for j in range(m)]
            now = dfs(map,m,n).search()
            ret = max(now,ret)
    return ret

def doit(m,n,f):
    p = [False]*16
    if m == 1:
        if 'B' in f[0]:
            p[15] = True
        if 'W' in f[0]:
            p[0] = True
        if 'BW' in f[0]:
            p[5] = True
        if 'WB' in f[0]:
            p[10] = True
    if n == 1:
        tmp = ''.join(f)
        if 'B' in tmp:
            p[15] = True
        if 'W' in tmp:
            p[0] = True
        if 'BW' in tmp:
            p[3] = True
        if 'WB' in tmp:
            p[12] = True
    for i in range(m-1):
        for j in range(n-1):
            p[check(f,i,j)] = True
    ret = 0
    for i in range(-1,m):
        for j in range(-1,n):
            ans = calculate(f,m,n,i,j,p)
            ret = max(ans,ret)
    return ret

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  m, n = [int(s) for s in input().split(" ")]
  f = [input() for i in range(m)]
  print("Case #{}: {}".format(i, doit(m,n,f)))
  # check out .format's specification for more formatting options
