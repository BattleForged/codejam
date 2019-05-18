class STreeBest():
    def __init__(self, l0, r0, x):
        if l0 == r0:
            self.best = x[l0]
            return
        mid = (l0+r0)/2
        self.ls = STreeBest(l0, mid, x)
        self.rs = STreeBest(mid+1, r0, x)
        self.mid = mid
        self.l = l0
        self.r = r0
        self.best = max(self.ls.best, self.rs.best)

    def find(self, pos, max):
        if pos < self.l:
            return -1, -1
        if self.r < pos:
            return -1, -1
        if self.best <= max:
            return self.l, self.r
        if pos <= self.mid:
            tmpl, tmpr = self.ls.find(pos, max)
            if tmpr == self.mid:
                tmplx, tmprx = self.rs.find(self.mid+1, max)
                if tmplx == tmpr:
                    return tmpl, tmprx
                else:
                    return tmpl, tmpr
            else:
                return tmpl, tmpr
        else:
            if self.mid < pos:
                tmpl, tmpr = self.rs.find(pos, max)
                if tmpl == self.mid+1:
                    tmplx, tmprx = self.ls.find(self.mid, max)
                    if tmprx == tmpl:
                        return tmplx, tmpr
                else:
                    return tmpl, tmpr


def delta(a, b):
    if a > b:
        return a-b
    return b-a


def doit(t, n, k):
    x1 = [int(x) for x in input().split()]
    x2 = [int(x) for x in input().split()]
    ret = 0
    for i in range(n):
        best1 = x1[i]
        best2 = x2[i]
        for j in range(i, n):
            best1 = x1[j] if best1 < x1[j] else best1
            best2 = x2[j] if best2 < x2[j] else best2
            if delta(best1, best2) <= k:
                ret += 1

    print('Case #{}: {}'.format(t, ret))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    [n, k] = [int(x) for x in input().split()]
    doit(i, n, k)
