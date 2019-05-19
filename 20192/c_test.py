MAX = 110
def check(a, b):
    for i in range(1, MAX):
        for j in range(1, MAX):
            possible = True
            if a*i+b*j <= 0:
                possible = False
            if possible:
                return True
    return False


for a in range(0, MAX):
    for b in range(0, MAX):
        if not check(a, b):
            print(a, b)
