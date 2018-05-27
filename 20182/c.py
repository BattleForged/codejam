class BQ:
    def __init__(self, v,n,m):
        self.v = v
        self.n = n
        self.m = m

    def get(self):
        self.b_to = [-1]*self.m
        matched = 0
        for i in range(self.n):
            self.a_checked = [False]*self.n
            if(self.search(i)):
                matched += 1
        return matched

    def search(self, now):
        self.a_checked[now] = True
        for i in self.v[now]:
            if self.b_to[i] == -1:
                self.b_to[i] = now
                return True
            else:
                if not self.a_checked[self.b_to[i]]:
                    if self.search(self.b_to[i]):
                        self.b_to[i] = now
                        return True
        return False

def doit():
    n = int(input())
    map = [[int(j) for j in input().split()]for i in range(n)]
    a = []
    r_cnt = 0
    c_cnt = 0
    bucket = [[] for i in range(2*n+1)]
    for j in range(n):
        for k in range(n):
            bucket[map[j][k]+n].append((j,k))
    matched = 0
    for i in range(-n, 1+n):
        r_dict = [-1]*n
        c_dict = [-1]*n
        for (j,k) in bucket[i+n]:
            if r_dict[j] < 0:
                r_dict[j] = r_cnt
                r_cnt += 1
                a.append([])
            if c_dict[k] < 0:
                c_dict[k] = c_cnt
                c_cnt += 1
            a[r_dict[j]].append(c_dict[k])
    bq = BQ(a,r_cnt,c_cnt)
    return n*n-bq.get()

T = int(input())
for I in range(1, T+1):
    print('Case #{}: {}'.format(I,doit()))
