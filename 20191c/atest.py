dic = {0: 'R', 1: 'S', 2: 'P'}
for i in range(255):
    x = [0] * 500
    now = i

    j = 0
    while now != 0:
        x[j] = now % 3
        now = now // 3
        j += 1
    ans = ''
    x.reverse()
    for i in x:
        ans += dic[i]
    print(ans)
