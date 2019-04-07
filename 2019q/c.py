def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def doit(crypted_message):
    n = len(crypted_message)
    message = [0] * (n + 1)
    for i in range(n):
        if crypted_message[i] != crypted_message[i+1]:
            base = i+1
            message[base] = gcd(crypted_message[i], crypted_message[i + 1])
            break
    for i in range(base - 1, -1, -1):
        message[i] = crypted_message[i] // message[i + 1]
    for i in range(base, n):
        message[i + 1] = crypted_message[i] // message[i]
    all_alphabet = list(set(message))
    all_alphabet.sort()
    alphabet_dict = {value: chr(index + ord('A')) for index, value in enumerate(all_alphabet)}

    return ''.join([alphabet_dict[number] for number in message])


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    [n, l] = [int(s) for s in input().split(" ")]
    crypted_message = [int(s) for s in input().split(" ")]

    print("Case #{}: {}".format(i, doit(crypted_message)))
