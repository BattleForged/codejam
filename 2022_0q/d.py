IMPOSSIBLE_F = 10**9
def doit():
    n = int(input())
    f = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]

    fromList = []
    for i in range(n+1):
        fromList.append([])
    for i in range(n):
        fromList[p[i]].append(i+1)

    forLoopList = [0]
    for i in range(n+1):
        now = forLoopList[i]
        for j in fromList[now]:
            forLoopList.append(j)
    
    result = 0 
    for i in range(n, 0, -1):
        now = forLoopList[i]
        if len(fromList[now]) == 0:
            continue
        else:
            sum = 0
            tmp = IMPOSSIBLE_F
            for j in fromList[now]:
                sum += f[j-1]
                tmp = min(f[j-1], tmp)
            result += sum - tmp
            f[now-1] = max(f[now-1], tmp)

    for j in fromList[0]:
        result += f[j-1]
    return result

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
