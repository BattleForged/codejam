class link:
    def __init__(self):
        self.next = [None] * 26
    def insert(self, str, i):
        if i >= len(str):
            return
        if self.next[c_to_i(str[i])] is None:
            self.next[c_to_i(str[i])] = link()
        self.next[c_to_i(str[i])].insert(str, i+1)
    def search(self, valid, i, l):
        if i >= l:
            return None
        for j in range(26):
            if valid[i][j] and self.next[j] is None:
                ans = chr(65+j)
                for k in range(i+1, l):
                    for l in range(26):
                        if valid[k][l]:
                            ans += chr(65+l)
                            break
                return ans
        for j in range(26):
            if  self.next[j] is not None:
                ans = self.next[j].search(valid, i+1, l)
                if ans is not None:
                    return chr(65+j) + ans
        return None


def c_to_i(chr):
    return ord(chr)-ord('A')

def doit(n, l):
    valid = [[False] * 26 for i in range(l)]
    head = link()
    for i in range(n):
        x = input()
        for j in range(l):
            valid[j][c_to_i(x[j])] = True
        head.insert(x, 0)
    ans = head.search(valid, 0, l)
    if ans is None:
        return '-'
    return ans

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n, l = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, doit(n, l)))
