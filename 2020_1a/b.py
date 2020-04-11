def ana(n):
    out = []
    while (n>0):
        out.append(n % 2)
        n = n // 2
    return out

def cal_0(l):
    return len(l) - sum(l)

def out(base, delta):
    path = []
    now = (0, 1)
    for i0 in range(len(base)):
        all = base[i0] == 1
        i = i0 + 1
        if now[1] == 1:
            if all:
                for k in range(i):
                    path.append((i, k+1))
                now = (i, i)
            else:
                path.append((i, 1))
                now = (i, 1)
        else:
            if all:
                for k in range(i):
                    path.append((i, i-k))
                now = (i, 1)
            else:
                path.append((i, i))
                now = (i, i)
    for i in range(delta):
        if now[1] == 1:
            path.append((now[0]+i+1, 1))
        else:
            path.append((now[0]+i+1, now[0]+i+1))
    for i in path:
        print('{} {}'.format(i[0], i[1]))
            


def doit(n):
    tmp = n
    while(True):
        
        base = ana(tmp)
        delta = n - cal_0(base) - tmp 
        if delta >= 0:
            out(base, delta)
            return
        tmp -= 1
        if tmp < 0:
            raise Exception


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}:".format(i))
    doit(n)
