def outRow (c, pattern):
    out = ['.'] * (c * 2 + 1)
    for i in range(c * 2 + 1):
        if (i % 2 == 0 and pattern == 0):
            out[i] = '+'
        if (i % 2 == 1 and pattern == 0):
            out[i] = '-'
        if (i % 2 == 0 and pattern == 1):
            out[i] = '|'
        if (i % 2 == 1 and pattern == 1):
            out[i] = '.'
    return out
        
def doit(r, c):
    out = []
    for i in range(r * 2 + 1):
        out.append(outRow(c, i%2))
    out[0][0] = '.'
    out[0][1] = '.'
    out[1][0] = '.'
    for i in range(r * 2 + 1):
        print(''.join(out[i]))

T = int(input())
for t in range(1, T + 1):
    [r, c] = [int(x) for x in input().split()]
    print('Case #{}:'.format(t))
    doit(r, c)