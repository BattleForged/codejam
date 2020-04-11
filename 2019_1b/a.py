class Person():
    def __init__(self, a, b, c):
        self.x = int(a)
        self.y = int(b)
        self.d = c
        if self.d == 'E':
            self.x_c = self.x+1
        elif self.d == 'W':
            self.x_c = self.x
        else:
            self.x_c = -1

        if self.d == 'S':
            self.y_c = self.y
        elif self.d == 'N':
            self.y_c = self.y+1
        else:
            self.y_c = -1


def get_key_in_row(p):
    return p.x_c


def get_key_in_col(p):
    return p.y_c


def doit(t, p, q):
    persons = []
    for i in range(p):
        [a, b, c] = input().split()
        persons.append(Person(a, b, c))
    persons.sort(key=get_key_in_row)

    ok = 0
    now = 0
    best_pos = 0
    for person in persons:
        if person.d == 'W':
            ok += 1
    best_ok = ok
    ret_x = 0
    for i in range(1, 1+q):
        while now < p and persons[now].x_c < i:
            now += 1
        while now < p and persons[now].x_c == i:
            if persons[now].d == 'W':
                ok -= 1
            elif persons[now].d == 'E':
                ok += 1
            now += 1
        if best_ok < ok:
            best_ok = ok
            ret_x = i

    persons.sort(key=get_key_in_col)
    ok = 0
    now = 0
    best_pos = 0
    for person in persons:
        if person.d == 'S':
            ok += 1
    best_ok = ok
    ret_y = 0
    for i in range(1, 1+q):
        while now < p and persons[now].y_c < i:
            now += 1
        while now < p and persons[now].y_c == i:
            if persons[now].d == 'S':
                ok -= 1
            elif persons[now].d == 'N':
                ok += 1
            now += 1
        if best_ok < ok:
            best_ok = ok
            ret_y = i

    print('Case #{}: {} {}'.format(t, ret_x, ret_y))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    [p, q] = [int(x) for x in input().split()]
    doit(i, p, q)
