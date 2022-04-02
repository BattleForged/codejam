NEEDED_INK = 10**6
def doit():
    minInk = [NEEDED_INK] * 4
    for i in range(3):
        printer = [int(x) for x in input().split()]
        for j in range(4):
            minInk[j] = min(printer[j], minInk[j])
    if sum(minInk) < NEEDED_INK:
        return 'IMPOSSIBLE'
    need = NEEDED_INK
    for j in range(4):
        if minInk[j] <= need:
            need -= minInk[j]
        else:
            minInk[j] = need
            need = 0
    return ' '.join(map(lambda i: str(i), minInk))

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
