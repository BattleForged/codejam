class ANS:
    def __init__(self,m,n):
        a = [[-1 for i in range(n+1)] for j in range(m+1)]
        changed = False
        for i in range(m+1):
            for j in range(n+1):
                changed = False
                for i0 in range(m-i,-1,-1):
                    for j0 in range(n-j,-1,-1):
                        if a[i0+i][j0+j] < a[i0][j0] + 1:
                            a[i0+i][j0+j] = a[i0][j0] + 1
                            changed = True
                if not changed:
                    break
            if j==0 and not changed:
                break
        self.a = a
    def get(self,m,n):
        return self.a[m][n]


t = int(input()) # read a line with a single integer
ans = ANS(500,500)
for i in range(1, t + 1):
  m,n =  [int(s) for s in input().split(" ")]
  print("Case #{}: {}".format(i, ans.get(m,n)))
