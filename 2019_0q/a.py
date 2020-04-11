split_ways = {
 '0': ('0', '0'),
 '1': ('1', '0'),
 '2': ('1', '1'),
 '3': ('2', '1'),
 '4': ('2', '2'),
 '5': ('3', '2'),
 '6': ('3', '3'),
 '7': ('5', '2'),
 '8': ('5', '3'),
 '9': ('6', '3'),
}
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input()
    a = ''
    b = ''
    for num in n:
        split_way = split_ways[num]
        a += split_way[0]
        b += split_way[1]

    print("Case #{}: {} {}".format(i, a.lstrip('0'), b.lstrip('0')))
