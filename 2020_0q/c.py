def doit():
    n = int(input())
    x = []
    for i in range(n):
        [a, b] = [int(x) for x in input().split()]
        x.append((a, b, i))
    x.sort()

    plan = ['X'] * n
    C_empty = 0
    J_empty = 0
    for (a, b, i) in x:
        if C_empty <= a:
            plan[i] = 'C'
            C_empty = b
        elif J_empty <= a:
            plan[i] = 'J'
            J_empty = b
        else:
            return 'IMPOSSIBLE'
    return ''.join(plan)


T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))