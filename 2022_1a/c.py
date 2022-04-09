INF = 10**8

def generate_overlap(step, e, w):
    ret = []
    for i in range(e+2):
        tmp = []
        for j in range(e+2):
            tmp.append([0]*w)
        ret.append(tmp)
    
    for i in range(e+2):
        x = [a for a in step[i]]
        for j in range(i, e+2):
            for k in range(w):
                x[k] = min(x[k], step[j][k])
                ret[i][j][k] = x[k]
    return ret

def empty_matrix(a, value):
    ret = []
    for i in range(a):
        ret.append([value] * a)
    for i in range(a):
        ret[i][i] = 0
    return ret

def cal(overlap, a, b, w):
    ret = 0
    for i in range(w):
        ret += a[i] + b[i] - 2*overlap[i]
    return ret

def generate_tepResult(overlap, step, e, w):
    ret = []
    for i in range(e+2):
        tmp = []
        for j in range(e+2):
            tmp.append([0]*(e+2))
        ret.append(tmp)

def doit():
    [e, w] = [int(x) for x in input().split()]
    step = []
    step.append([0]*w)
    for i in range(e):
        step.append([int(x) for x in input().split()])
    step.append([0]*w)
    
    overlap = generate_overlap(step, e, w)
    result = empty_matrix(e+2, INF)

    overlap_sum = empty_matrix(e+2, 0)
    for i in range(1, e+2):
        for j in range(i, e+2):
            overlap_sum[i][j] = sum(overlap[i][j])
    step_sum = [sum(step[i]) for i in range(e+2)]

    for i in range(1, e+2):
        for j in range(e+2-i):
            for k in range(0, i):
                result[j][j+i] = min(result[j][j+k] + result[j+k+1][j+i] + (step_sum[j+k] + step_sum[j+k+1] - 2 * overlap_sum[j][j+i]), result[j][j+i])
    return result[0][e+1]

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))
    