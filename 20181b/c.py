class helper:
  def __init__(self, n, f, x):
    self.n =n
    self.f =f
    self.x =x

  def check(self, pos, need):
    if self.owe[pos-1] == True:
        return False
    if self.tmp[pos-1] >= need:
        self.tmp[pos-1] -= need
        return True
    else:
        tmp = self.tmp[pos-1]
        self.tmp[pos-1] = 0
        self.owe[pos-1] = True
        if self.check(self.f[pos-1][0],need-tmp) and self.check(self.f[pos-1][1],need-tmp):
            self.owe[pos-1] = False
            return True
        return False


  def get(self):
    l=0
    r=sum(self.x)
    while l<r:
      mid = (l+r+1)//2
      self.tmp = self.x.copy()
      self.owe = [False]*n
      if self.check(1, mid):
        l = mid
      else:
        r = mid -1
    return l

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  f= []
  for j in range(n):
    f.append([int(s) for s in input().split(" ")])
  x = [int(s) for s in input().split(" ")]
  ans = helper(n,f,x)
  print("Case #{}: {}".format(i, ans.get()))
  # check out .format's specification for more formatting options
