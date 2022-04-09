def doit(s):
    out = ''
    n = len(s)
    i = 0
    while i < n:
        j = i
        while (j < n-1) and s[j] == s[j+1]:
            j += 1
        if (j < n-1) and s[j] < s[j+1]:
            out += s[i] * (j-i+1) * 2
        else:
            out += s[i] * (j-i+1)
        i = j + 1
    return out

T = int(input())
for t in range(1, T + 1):
    s = input()
    print('Case #{}: {}'.format(t, doit(s)))
    