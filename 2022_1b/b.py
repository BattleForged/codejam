def doit():
    [n, p] = [int(x) for x in input().split()]
    maxx = 0
    minx = 0
    resmax = 0
    resmin = 0
    for i in range(n):
        d = [int(x) for x in input().split()]
        maxy = max(d)
        miny = min(d)
        newresmax = min(resmax+abs(maxx-miny)+abs(miny-maxy),resmin+abs(minx-miny)+abs(miny-maxy))
        newresmin = min(resmax+abs(maxx-maxy)+abs(miny-maxy),resmin+abs(minx-maxy)+abs(miny-maxy))
        resmax = newresmax
        resmin = newresmin
        maxx = maxy
        minx = miny

    return min(resmin, resmax)

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
    