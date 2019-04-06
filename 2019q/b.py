def doit(way):
    ret = ''
    for choice in way:
        ret += 'E' if choice == 'S' else 'S'
    return ret


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    l = input()

    print("Case #{}: {}".format(i, doit(l)))
