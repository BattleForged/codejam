GUESS = ['A', 'B', 'C', 'D', 'E']

[T, f] = [int(x) for x in input().split()]
for t in range(1, T + 1):
    ans = ''
    first = {}
    guess = set(GUESS)
    for i in guess:
        first[i] = []
    for i in range(119):
        print(i * 5 + 1)
        first[input()].append(i)
    for i in guess:
        if len(first[i]) == 24 - 1:
            now = i
    ans += now
    need = first[now]
    guess.remove(now)

    second = {}
    for i in guess:
        second[i] = []
    for i in need:
        print(i * 5 + 2)
        second[input()].append(i)
    for i in guess:
        if len(second[i]) == 6 - 1:
            now = i
    ans += now
    need = second[now]
    guess.remove(now)

    third = {}
    for i in guess:
        third[i] = []
    for i in need:
        print(i * 5 + 3)
        third[input()].append(i)
    for i in guess:
        if len(third[i]) == 2 - 1:
            now = i
    ans += now
    need = third[now]
    guess.remove(now)

    last_check = need[0]
    print(last_check * 5 + 4)
    forth = input()
    for i in guess:
        if i != forth:
            now = i

    ans += now
    guess.remove(now)

    for i in guess:
        ans += i

    print(ans)
    assert input() == 'Y'
