class path:
    def __init__(self,l,r,x=0,xx=0):
        self.l = l
        self.r = r
        self.x = x
        self.xx = xx
    def copy(self):
        return path(self.l,self.r,self.x,self.xx)
    def out(self):
        print(self.l, self.r, self.x,self.xx)

def ans(n, f):
    l = [x[0]+x[1] for x in f]
    r = [x[0]-x[2] for x in f]
    ans = 1
    cnt = 1
    ll = path(l[0],r[0])
    rr = path(l[0],r[0])
    for i in range(1,n):
        if ll.l == l[i]:
            ltmp = ll.copy()
        else:
            ltmp = rr.copy()
            if ltmp.l != l[i]:
                ltmp.l = l[i]
                ltmp.x = ltmp.xx
            ltmp.xx = i
        if rr.r == r[i]:
            rtmp = rr.copy()
        else:
            rtmp = ll.copy()
            if rtmp.r != r[i]:
                rtmp.r = r[i]
                rtmp.x = rtmp.xx
            rtmp.xx = i
        ll = ltmp
        rr = rtmp
        maxx = max(i-ll.x+1,i-rr.x+1)

        if ans < maxx:
            ans = maxx
            cnt =0
        if ans == maxx:
            cnt += 1
    return '{} {}'.format(ans,cnt)

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  f= []
  for j in range(n):
    f.append([int(s) for s in input().split(" ")])
  print("Case #{}: {}".format(i, ans(n,f)))
  # check out .format's specification for more formatting options
