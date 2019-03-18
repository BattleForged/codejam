def doit(x, y):
  x_delta = max(x) - min(x)
  y_delta = max(y) - min(y)
  return (max(x_delta, y_delta) + 1) // 2


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  x_points = []
  y_points = []
  for j in range(0, n):
    x = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    x_points.append(x[0])
    y_points.append(x[1])

  print("Case #{}: {}".format(i, doit(x_points, y_points)))