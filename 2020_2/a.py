def guess(a,b,limit):
    # a*x^2+bx/2 <= limit
    l0 = 0
    r0 = 10**11
    while l0 != r0:
        mid = (l0 + r0 + 1) // 2
        # print(l0, r0, mid * mid * a + mid * b, 2 * limit)
        if mid * mid * a + mid * b <= 2 * limit :
            l0 = mid
        else:
            r0 = mid-1
    # print(l0, r0, mid, (r0+2) * (r0+2) * a + (r0+2) * b, 2 * limit)
    return l0

def doit(l, r):
    delta = l - r
    if delta >= 0:
        x0 = guess(1, 1, delta)
        l -= (x0 * x0  +  x0) // 2

    else:
        x0 = guess(1, 1, -delta)
        r -= (x0 * x0  +  x0) // 2
    if l >= r:
        x1 = guess(2, 2*x0, l)
        x2 = guess(2, 2*x0+2, r)
        if x1 > x2+1:
            x1 = x2+1
        if x2 > x1+1:
            x2 = x1+1
        l -= x1*x1 + x1*(x0)
        r -= x2*x2 + x2*(x0+1)
        
    else:
        x1 = guess(2, 2*x0, r)
        x2 = guess(2, 2*x0+2, l)
        if x1 > x2+1:
            x1 = x2+1
        if x2 > x1+1:
            x2 = x1+1
        r -= x1*x1 + x1*(x0)
        l -= x2*x2 + x2*(x0+1)
    return '{} {} {}'.format(x0+x1+x2, l, r)

def force(l, r):
    k = 1
    while True:
        if l >= r:
            if l >= k:
                l -= k
                k += 1
            else:
                break
        else:
            if r >= k:
                r -= k
                k += 1
            else:
                break
    return '{} {} {}'.format(k-1, l, r)

"""
for i in range(1000):
    for j in range(1000):
        print(i, j)
        a = force(i, j) 
        b = doit(i, j)
        if a != b:
            print(i, j, '!!!', a, '!!!', b)
            exit()

"""
T = int(input())
for t in range(1, T + 1):
    [l, r] = [int(x) for x in input().split()]
    print('Case #{}: {}'.format(t, doit(l, r)))
