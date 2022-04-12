def reverse(steps, reverse_total, reverse_we, reverse_ns):
    real_step = {
        'N': 'N',
        'E': 'E',
        'W': 'W',
        'S': 'S'
    } if not reverse_total else {
        'N': 'E',
        'E': 'N',
        'W': 'S',
        'S': 'W' 
    }
    if (reverse_we and not reverse_total) or (reverse_ns and reverse_total):
        tmp = real_step['W']
        real_step['W'] = real_step['E']
        real_step['E'] = tmp
    if (reverse_we and reverse_total) or (reverse_ns and not reverse_total):
        tmp = real_step['N']
        real_step['N'] = real_step['S']
        real_step['S'] = tmp
    ret = []
    for i in range(len(steps)):
        ret.append(real_step[steps[i]])
    return ret

# x = a-c, y = b-d
def calculate(x, y):
    max = 1
    while (max-1 < x+y):
        max = max << 1
    minus = (max - (x+y)) // 2 # c+d
    plus = x + y + minus # a+b
    z = (max - (x-y)) // 2 # b+c
    b = plus & z
    c = z-b
    d = minus - c
    a = plus - b
    
    i = 1
    ret = []
    while i < max:
        if a & i == i:
            ret.append('E')
        elif b & i == i:
            ret.append('N')
        elif c & i == i:
            ret.append('W')
        elif d & i == i:
            ret.append('S')                     
        i = i << 1
    return ret

def doit():
    [x, y] = [int(x) for x in input().split()]
    if x == 0 and y == 0:
        return ''
    if (x + y) % 2  == 0:
        return 'IMPOSSIBLE'
    reverse_we = (x < 0)
    reverse_ns = (y < 0)
    x = abs(x)
    y = abs(y)
    reverse_total = (x < y)
    steps = calculate(y, x) if x < y else calculate(x, y)

    return ''.join(reverse(steps, reverse_total, reverse_we, reverse_ns))

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))