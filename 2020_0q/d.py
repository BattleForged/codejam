def check(out, same, diff):
    if same > 0 and diff > 0:
        print(same)
        a = input()
        print(diff)
        b = input()
        comp = out[same-1] != a
        one_change = out[diff-1] != b
        return (one_change!=comp, comp)
    if diff > 0:
        print(diff)
        b = input()
        print(diff)
        b = input()
        return (False, out[diff-1] != b)
    if same > 0:
        print(same)
        a = input()
        print(same)
        a = input()
        return (False, out[same-1] != a)
def doit(B):
    changed = False
    out = ['0'] * B
    real = ['0'] * B
    now = 0
    same = -1
    diff = -1
    reve_all = False
    comp_all = False
    while True:
        if changed:
            max_loop = 4
            (reve, comp) = check(out, same, diff)
            if reve:
                out.reverse()
            if comp:
                out = ['1' if x == '0' else '0' for x in out]
            reve_all = reve_all != reve
            comp_all = comp_all != comp
        else:
            max_loop = 5
        for _ in range(max_loop):
            print(now+1)
            out[now] = input()
            print(B-now)
            out[B-now-1] = input()
            if out[now] == out[B-now-1]:
                same = now+1
            else:
                diff = now+1
            now += 1
            if (now >= B/2):
                print(''.join(out))
                return
        changed = True


[T, B] = [int(x) for x in input().split()]
for t in range(T):
    doit(B)
    checked = input()
    if checked != 'Y':
        break