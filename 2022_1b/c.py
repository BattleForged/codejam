def appendzero(s):
  return s + '0' * len(s)

def expand(s):
  return s + s

def P(k):
  if k == 0:
      return ['1']
  seq = P(k - 1)
  seq_with_zero = [appendzero(s) for s in seq]
  seq_with_copy = [expand(s) for s in seq]
  res = seq_with_copy[:]
  for ins in seq_with_zero:
      res += [ins]
      res += seq_with_copy
  return res

x = P(3)

def doit():
    for i in x:
      print(i)
      ans = int(input())
      if (ans == 0):
        return

T = int(input())
for t in range(1, T + 1):
    doit()
