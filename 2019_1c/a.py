MAX_DEPTH = 500
CHOICE = ['R', 'S', 'P']
NG = {'R': 'S', 'S': 'P', 'P': 'R'}


def doit():
    a = int(input())
    oppos = [input() for _ in range(a)]
    ans = ''
    for i in range(MAX_DEPTH):
        perhaps = CHOICE.copy()
        for oppo in oppos:
            o = oppo[i % len(oppo)]
            if NG[o] in perhaps:
                perhaps.remove(NG[o])
        life = len(perhaps)
        if life == 0:
            return None
        elif life == 1:
            slt = perhaps[0]
            oppos = [oppo for oppo in oppos if oppo[i % len(oppo)] == slt]
            ans += slt
        else:
            for slt in perhaps:
                if NG[slt] in perhaps:
                    ans += slt
                    return ans
    return ans


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    ans = doit()
    if ans:
        print('Case #{}: {}'.format(i, ans))
    else:
        print('Case #{}: IMPOSSIBLE'.format(i))
