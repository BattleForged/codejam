class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x*self.y)


class Line(object):

    def __init__(self, s, e):
        self.s = s
        self.e = e

    @property
    def mid(self):
        return Point((self.s.x+self.e.x)/2, (self.s.y+self.e.y)/2)

    def calculate(self, p):
        feature_same_side = (self.s.y - p.y) * (self.e.y - p.y)
        if feature_same_side > 0:
            return 0
        elif feature_same_side == 0:
            if (self.e.y - p.y) == 0:
                return 0
            # (self.s.y - p.y) == 0
            elif self.s.x < p.x:
                return 0
            return 1 if self.s.y - self.e.y > 0 else -1
        # diff_side
        if self.e.x == self.s.x:
            if self.e.x < p.x:
                return 0
            else:
                return 1 if self.s.y - self.e.y > 0 else -1
        k = 1 if self.s.x - self.e.x > 0 else -1
        tmp = (self.s.y - self.e.y) * (p.y - self.s.y) - (self.s.x - self.e.x) * (p.x - self.s.x)
        if k * tmp < 0:
            return 0
        return 1 if self.s.y - self.e.y > 0 else -1


class PointDict(object):
    def __int__(self):
        self.point_to_num = {}
        self.num_to_point = {}
        self.point_cnt = 0

    def ptn(self, p):
        if p not in self.point_to_num:
            self.point_to_num[p] = self.point_cnt
            self.num_to_point[self.point_cnt] = p
            self.point_cnt += 1
        return self.point_to_num[p]

    def ntp(self, n):
        return self.num_to_point[n]

class DfsRunner(object):
    def __int__(self, matrix):
        self.matrix = matrix
        self.visited = [False] * range(len(matrix))
        self.first_sum = [0] * range(len(matrix))

def doit():
    point_dict = PointDict()
    [f, k] = [int(s) for s in input().split(" ")]
    line_list = []
    for cnt in range(f):
        [x0, y0, x1, y1] = ([int(s) for s in input().split(" ")])  # read a list of integers, 4 in this case
        n_1 = point_dict.ptn(Point(x1, y1))
        n_0 = point_dict.ptn(Point(x0, y0))
        line_list.append(n_1, n_0)
    matrix = []
    for i in range(point_dict.point_cnt):
        matrix.append([False]*point_dict.point_cnt)
    for (p0, p1) in line_list:
        matrix[p0, p1] = True
        matrix[p1, p0] = True

    out = [False] * f
    out_cnt = f
    now = k-1
    ret = []
    while(out_cnt > 0):
        ret.append[now]
        out_cnt -= 1
        out[now] = True
        matrix[line_list[now][0]][line_list[now][1]] = False
        matrix[line_list[now][1]][line_list[now][0]] = False
        perhaps_list = [False] * f
        out_line = Line(point_dict.ntp(line_list[now][0]), point_dict.ntp(line_list[now][1]))
        while(True):
            for i in range(f):
                if not out[i] and not perhaps_list[i]:
                    checked_line = Line(point_dict.ntp(line_list[i][0]), point_dict.ntp(line_list[i][1]))
                    matrix[line_list[i][0]][line_list[i][1]] = False
                    matrix[line_list[i][1]][line_list[i][0]] = False
                    DfsRunner(matrix, visited)
                    if dfs(out_line.mid, checked_line.mid, matrix, visited):


                    matrix[line_list[i][0]][line_list[i][1]] = True
                    matrix[line_list[i][1]][line_list[i][0]] = True



t = int(input())    # read a line with a single integer
for i in range(1, t + 1):
    print("Case #{}: {}".format(i, doit()))
