class D(object):
    def __init__(self, k):
        self.nei = [None] * 4 # l d u r
        self.k = k
        self.changed = -1
        self.die = False
    
    def is_lose(self):
        cnt = 0
        sum = 0
        for i in self.nei:
            if i != None:
                cnt += 1
                sum += i.k
        return self.k * cnt < sum

    def out(self, round):
        pos = []
        self.die = True
        for i in range(len(self.nei)):
            if self.nei[i] != None and not self.nei[i].die:
                if self.nei[i].changed < round:
                    pos.append(self.nei[i])
                self.nei[i].nei[3-i] = self.nei[3-i]
                self.nei[i].changed = round
        return pos


def doit():
    [r, c] = [int(x) for x in input().split()]
    map = []
    now = 0
    ans = 0
    for _ in range(r):
        tmp = [int(x) for x in input().split()]
        map.append([D(num) for num in tmp])
        now += sum(tmp)

    pos = []
    for i in range(r):
        for j in range(c):
            pos.append(map[i][j])
            map[i][j].pos = (i, j)
            if j > 0:
                map[i][j].nei[0] = map[i][j-1]
            if j < c-1:
                map[i][j].nei[3] = map[i][j+1]
            if i > 0:
                map[i][j].nei[2] = map[i-1][j]
            if i < r-1:
                map[i][j].nei[1] = map[i+1][j]
    
    round = 0

    while(True):
        round += 1
        ans += now
        if len(pos) <= 0:
            return ans
        out = []
        for d in pos:
            if not d.die and d.is_lose():
                out.append(d)
                now -= d.k
        if len(out) <= 0:
            return ans
        pos = []
        for d in out:
            pos.extend(d.out(round))



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, doit()))
