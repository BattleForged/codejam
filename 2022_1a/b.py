MAX = 10**9

def a_list():
    out = []
    for i in range(30):
        out.append(2**i)
    for j in range(1, 100):
        if j not in out:
            out.append(j)
        if len(out) == 100:
            return out
out_list = a_list()

def plus_list(need):
    out = []
    for i in range(30):
        k = 2**(i)
        if (k & need == k):
            out.append(k)
    return out

def doit():
    N = int(input())
    print(' '.join([str(a) for a in out_list]))
    b_list = [int(x) for x in input().split()]
    all = out_list + b_list
    all.sort(reverse = True)
    need = sum(all)//2
    out = []
    for i in all:
        if (need - i >= 0):
            out.append(i)
            need -= i
        else:
            break
    return out + plus_list(need)

T = int(input())
for t in range(1, T + 1):
    print(' '.join([str(a) for a in doit()]))