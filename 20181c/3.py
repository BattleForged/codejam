def doit(n):
    x = [int(s) for s in input().split(" ")]
    dp = [0]
    ans = 0
    for weight in x:
        for j in range(ans, -1, -1):
            if dp[j] <= 6 * weight:
                if j == ans:
                    dp.append(dp[j]+weight)
                    ans += 1
                elif dp[j+1] > dp[j] + weight:
                    dp[j+1] = dp[j] + weight
    return ans

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  print("Case #{}: {}".format(i, doit(n)))
