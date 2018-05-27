
def doit():
    n = int(input())
    p = [0] * n
    sold = [False] * n
    for k in range(n):
        x = [int(s) for s in input().split(" ")]
        if x[0] == -1:
            return
        perhaps = -1
        for i in range(1, x[0]+1):
            p[x[i]] += 1
            if perhaps < 0 or p[perhaps] > p[x[i]]:
                if not sold[x[i]]:
                    perhaps = x[i]
        if perhaps >= 0:
            sold[perhaps] = True
        print(perhaps)

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  doit()
