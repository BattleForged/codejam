
def main():
    input = open('a.in', 'r')
    output = open('a.out', 'w')
    T = int(input.readline().split()[0])
    for I in range(T):
        N, P = [int(i) for i in input.readline().split()]
        G = [int(i) for i in input.readline().split()]
        cnt = [0] * P

        for i in range(N):
            cnt[G[i] % P] += 1
        print(cnt)
        if P==2:
            ans = cnt[0]+cnt[1]//2
            if cnt[1] % 2 >0:
                ans += 1
        elif P==3:
            max = cnt[2] if cnt[1] > cnt [2] else cnt[1]
            ans = cnt[0] + max
            cnt[2] -= max
            cnt[1] -= max
            ans += cnt[2]//3 + cnt[1]//3
            if cnt[2]%3>0 or cnt[1]%3>0:
                ans += 1
        elif P==4:
            ans = cnt[0]
            let3_1 = cnt[3] if cnt[1] > cnt [3] else cnt[1]
            ans += let3_1
            cnt[3] -= let3_1
            cnt[1] -= let3_1
            let2_2 = cnt[2] // 2
            ans += let2_2
            cnt[2] -= let2_2 * 2
            if cnt[2] > 0 and cnt[1] > 1:
                ans += 1
                cnt[2] = 0
                cnt[1] -= 2
            if cnt[2] > 0 and cnt[3] > 1:
                ans += 1
                cnt[2] = 0
                cnt[3] -= 2
            ans += cnt[1]//4+cnt[3]//4
            if cnt[1]%4+cnt[3]%4+cnt[2]%2>0:
                ans += 1
        output.write('Case #{}: {}\n'.format(I+1, ans))



if __name__ == "__main__":
    main()
