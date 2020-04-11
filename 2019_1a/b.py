TEST_LIST = [17, 9, 8, 5, 13, 11, 7]
ALL = 6126120

NUMBER = 18


def gcd(a, b):
    if b == 1:
        return (0, 1)
    (x1, x2) = gcd(b, a % b)
    # print(f'{x2}*{a}+{x1 - x2 * (a // b)}*{b} = {x2*a+(x1 - x2 * (a// b))*b}')
    return (x2, x1 - x2 * (a // b))


def generate(base):
    (a, b) = gcd(ALL // base, base)
    return a * ALL // base % ALL


ANS_PART = [generate(test) for test in TEST_LIST]


for i in range(7):
    assert ANS_PART[i] % TEST_LIST[i] == 1


def doit():
    mod_result = []
    for test_number in TEST_LIST:
        print(' '.join([str(test_number) for j in range(NUMBER)]))
        tmp = [int(s) for s in input().split(" ")]
        mod_result.append(sum(tmp))
    ans = 0
    for i in range(7):
        ans += ANS_PART[i] * mod_result[i] % ALL
    print(ans % ALL)


[t, n, m] = [int(s) for s in input().split(" ")]  # read a list of integers, 3 in this case
for i in range(1, t + 1):
    doit()
    if int(input()) != 1:
        break
