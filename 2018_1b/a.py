class language:
    def __init__(self, n, to_next):
        self.n = n
        self.to_next = to_next

def ans(n, m, x):
    ans = [(i*1000+5*n)//(10*n) for i in range(n+1)]
    if_round = [(i*100)//(n) != (i*1000+5*n)//(10*n) for i in range(n+1)]
    closed_round = [0] * (n+1)
    closed_round[n] = n+1
    for i in range(n-1, -1, -1):
        if if_round[i]:
            closed_round[i] = i
        else:
            closed_round[i] = closed_round[i+1]
    left = n - sum(x)
    new_x = [language(i, closed_round[i] - i) for i in x]
    new_x.sort(key=lambda x:x.to_next)
    zero_to_next = closed_round[0]
    ret = 0
    for i in range(m):
        if new_x[i].to_next <= zero_to_next:
            if left >= new_x[i].to_next:
                left -= new_x[i].to_next
                ret += ans[closed_round[new_x[i].n]]
                continue
        ret += ans[new_x[i].n]
    while left >= zero_to_next:
        left -= zero_to_next
        ret += ans[zero_to_next]
    ret += ans[left]
    return ret

if __name__ == "__main__":
    t = int(input()) # read a line with a single integer
    for i in range(1, t + 1):
      n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
      x = [int(s) for s in input().split(" ")]
      print("Case #{}: {}".format(i, ans(n, m, x)))
  # check out .format's specification for more formatting options
