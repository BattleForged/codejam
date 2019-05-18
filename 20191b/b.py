[t, w] = [int(x) for x in input().split()]
for i in range(1, t + 1):
    print(210)
    y1 = int(input())
    y1 //= (2**35)
    x6 = y1 % (2**7)
    y1 //= (2**7)
    x5 = y1 % (2**10)
    x4 = y1 // (2**10)
    print(48)
    y2 = int(input())
    y2 -= (2**8) * x6 + (2**9) * x5 + (2**12) * x4
    y2 //= (2**16)
    x3 = y2 % (2**8)
    y2 //= (2**8)
    x2 = y2 % (2**24)
    x1 = y2 // (2**24)
    print('{} {} {} {} {} {}'.format(x1, x2, x3, x4, x5, x6))
    res = int(input())
    assert res==1
