class Node(object):

    def __init__(self, parent):
        self.next = [None] * 26
        self.end = False
        self.cnt = [0] * 26

    def insert(self, str):
        if str == '':
            self.end = True
            return
        now = ord(str[0]) - ord('A')
        if not self.next[now]:
            self.next[now] = Node(self)
        self.cnt[now] += 1
        self.next[now].insert(str[1:])

    def search(self, not_root=False):
        not_paired = 0
        paired = 0
        tmp = 0
        if self.end:
            not_paired += 1
        for i in range(26):
            if self.next[i]:
                tmp = self.next[i].search()
                paired += tmp
                not_paired += self.cnt[i] - tmp
        if not not_root and not_paired >= 2:
            paired += 2
        return paired


def doit():
    n = int(input())
    root = Node(None)
    for i in range(n):
        tmp_str = (input())
        root.insert(tmp_str[::-1])
    return root.search(not_root=True)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, doit()))
