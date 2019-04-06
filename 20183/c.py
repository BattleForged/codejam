def doit(points, n):
    order = []
    used = [False] * n
    a = 0
    for i in range(1, n):
        if points[a][2] < points[i][2]:
            a = i
    used[a] = True
    order.append(a)

    b = -1
    slope_best = -1
    for i in range(0, n):
        if not used[i]:
            slope_now = ((points[i][2] - points[a][2])**2 / ((points[i][0] - points[a][0])**2 + (points[i][1] - points[a][1])**2))
            if b == -1 or slope_now < slope_best:
                b = i
            slope_best = slope_now
         used[b] = True
         order.append(b)

     for j in range(n-2):



    order.reverse()
    return [num+1 for num in order]


t = int(input())    # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    points = []
    for j in range(0, n):
        points.append([int(s) for s in input().split(" ")]) # read a list of integers, 2 in this case

    print("Case #{}: {}".format(i, doit(points, n)))
