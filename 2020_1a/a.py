def doit():
    n = int(input())
    start = []
    end = []
    mid = []
    for _ in range(n):
        tmp = input().split('*')
        l =len(tmp)
        if tmp[0] != '':
            start.append(tmp[0])
        if tmp[l-1] != '':
            end.append(tmp[l-1])
        for i in range(1, l-1):
            mid.append(tmp[i])

    s0 = ''
    for s in start:
        l0 = len(s0)
        l1 = len(s)
        for i in range(min(l0, l1)):
            if s0[i] != s[i]:
                return '*'
        if l0 < l1:
            s0 = s
    e0 = ''
    for e in end:
        l0 = len(e0)
        l1 = len(e)
        for i in range(min(l0, l1)):
            if e0[l0-1-i] != e[l1-1-i]:
                return '*'
        if l0 < l1:
            e0 = e
    return s0 + ''.join(mid) + e0


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, doit()))
