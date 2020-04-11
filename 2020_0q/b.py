def doit():
    x = input()
    n = len(x)
    out = ''

    now = 0
    for i in x:
        delta = int(i) - now
        if delta > 0:
            out += '(' * delta
        elif delta < 0:
            out += ')' * (-delta)
        out += i
        now = int(i)
    out += ')' * int(x[n-1])
    return out
        



T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))