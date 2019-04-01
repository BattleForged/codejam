import random

MAX_LABEL = 5
NEIBER_COUNT = 4


def output(x):
    # print(x)
    pass


def output_matrix(matrix, n):
    for i in range(n):
        output(','.join([str(num) for num in matrix[i]]))


def connect(matrix, n):
    visited = [False] * n
    points = [0]
    visited[0] = True
    bottom = 0
    top = 1
    while bottom < top:
        for i in range(bottom, top):
            for j in range(n):
                if matrix[i][j] != 0 and not visited[j]:
                    points.append(j)
                    visited[j] = True
        bottom = top
        top = len(points)
    return top == n


def generate_the_graph(n):
    x = list(range(n))
    while True:
        tmp = []
        for i in range(NEIBER_COUNT):
            random.shuffle(x)
            tmp.extend(x.copy())
        matrix = generate_empty_matrix(n)
        cnt = 0
        for i in range(0, n * 2):
            a = tmp[i * 2]
            b = tmp[i * 2 + 1]
            if a == b:
                output('self_loop')
                break
            if matrix[a][b] == 0:
                matrix[a][b] = 1
                matrix[b][a] = 1
                cnt += 1
            else:
                output('repeated')
                break

        if cnt != n * 2:
            continue
        output(tmp)
        output_matrix(matrix, n)
        output('\n')
        if not connect(matrix, n):
            output('not_connect')
            continue
        feature = calculate_feature(matrix, n)
        if check_graph(feature, n):
            output('good!!!')
            return matrix, feature
        output('sad!!!')
        continue


def generate_empty_matrix(n):
    ret = []
    for i in range(n):
        ret.append([0] * n)
    return ret


def feature_is_same(f1, f2):
    used = [False] * NEIBER_COUNT
    for i in range(NEIBER_COUNT):
        for j in range(NEIBER_COUNT):
            if not used[j] and f1[i] == f2[j]:
                used[j] = True
                break
        else:
            return False
    return True


def calculate_feature(matrix, n):
    label = [matrix]
    for l in range(1, MAX_LABEL):
        label.append(generate_empty_matrix(n))
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    label[l][i][k] += label[l - 1][i][j] * matrix[j][k]
    feature = []
    for i in range(n):
        feature_of_i = []
        for j in range(n):
            if label[0][i][j] != 0:
                tmp = []
                for k in range(0, MAX_LABEL):
                    tmp.append(label[k][i][j])
                feature_of_i.append(tmp)
        feature.append(feature_of_i)
    output(feature)
    output('\n')
    return feature


def check_graph(feature, n):
    for i in range(n):
        for j in range(i + 1, n):
            if feature_is_same(feature[i], feature[j]):
                output('{} === {}'.format(i, j))
                return False
    return True


def tell_interaction_matrix(matrix, n):
    print(n)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == 1:
                print('{} {}'.format(i+1, j+1))


def hear_matrix():
    n = int(input())
    matrix = generate_empty_matrix(n)
    for i in range(n*2):
        [l, r] = [int(s) for s in input().split(" ")]
        matrix[l-1][r-1] = 1
        matrix[r-1][l-1] = 1
    return matrix


def find_relation(fs1, fs2, n):
    ret = []
    used = [False] * n
    for i in range(n):
        for j in range(n):
            if not used[j] and feature_is_same(fs1[i], fs2[j]):
                ret.append(j+1)
                used[j] = True
                break
    return ret


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    [l, r] = [int(s) for s in input().split(" ")]
    matrix, feature = generate_the_graph(l)
    tell_interaction_matrix(matrix, l)
    new_matrix = hear_matrix()
    new_feature = calculate_feature(new_matrix, l)
    print(' '.join([str(num) for num in find_relation(feature, new_feature, l)]))
