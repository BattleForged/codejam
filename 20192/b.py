npeople = 100
nvases = 20


def doit():
    sum = [0] * 21
    choice = None
    for i in range(1, npeople+1):
        assert i == int(input())
        if i in range(nvases+1):
            print(i, npeople)
        elif i <= 60:
            print(((i-1) % (10))+1, npeople)
        elif i <= 70:
            need_check = (i-1) % (10)+11
            print(need_check, 0)
            tmp = [int(x) for x in input().split()]
            sum[need_check] = (70-i)/20+tmp[0]
            if (i == 70):
                min_value = min(sum[11:21])
                choice = sum.index(min_value)
        else:
            need_up = 0
            min_value = 100
            for i in range(11, 21):
                if i != choice and min_value > sum[i]:
                    min_value = sum[i]
                    need_up = i
            sum[need_up] += 1
            print(need_up, 100)


T = int(input())
for t in range(1, T + 1):
    doit()
