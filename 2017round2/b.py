# '/' 1,0-> 0,-1 -1,0->0,1
# '\' 1,0->0,1
start =[[0,1],[0,-1]][[1,0],[-1,0]]
class node(object):
    def __init__(self, type):
        """
            type:0 allhead
            type:1 empty place head
            type:2 lazer head
        """
        self.type = type
        self.head = self
        self.all = 0
        self.l = self
        self.r = self
        self.u = self
        self.d = self

    def insert_right(self, node_i):
        node_i.r = self.r
        self.r.l = node_i
        self.r = node_i
        node_i.l = self

def check(map,R,C,i,j):
    achieved = [None, None]
    for ii in range(2):
        achieved_map = [[0]*C]*R
        possible = True
        for jj in range(2):
            i0 = i + start[ii][jj][0]
            j0 = j + start[ii][jj][1]
            possion = start[ii][jj]
            while(i0 in range(R) and j0 in range(C) and map[i0][j0] !='#'):
                if map[i0][j0] == '-' or map[i0][j0] == '|':
                    possible = False
                    break
                if map[i0][j0] == '.':
                    achieved_map[i0][j0] = 1
                if map[i0][j0] == '\':
                    tmp = possion[0]
                    possion[0] = possion[1]
                    possion[1] = tmp
                if map[i0][j0] == '/':
                    tmp = possion[0]
                    possion[0] = -possion[1]
                    possion[1] = -tmp
                i0 += possion[0]
                j0 += possion[1]
            if possible == False:
                break
        if possible:
            achieved[ii] = achieved_map
    return achieved




def doit(R,C,map):
    allhead = node(0)
    headmap = [[None]*C]*R
    for i in range(R):
        for j in range(C):
            if map[i][j] == '.':
                heapmap[i][j] = node(1)
            if map[i][j] == '-' or map[i][j] == '|':
                heapmap[i][j] = node(2)
    for i in range(R):
        for j in range(C):
            if headmap[i][j] is not None:
                allhead.insert_right(headmap[i][j])
    for i in range(R):
        for j in range(C):
            if map[i][j] == '-' or map[i][j] == '|':
                perhaps = check(map,R,C,i,j)
                if perhaps[0] is None and perhaps[1] is None:
                    return 'IMPOSSIBLE'
                if perhaps[0] is not None:
                    now = headmap[i][j]
                        



def main():
    input = open('a.in', 'r')
    output = open('a.out', 'w')
    T = int(input.readline().split()[0])
    for I in range(T):
        R,C = [int(i) for i in input.readline().split()]
        map = [input.readline() for i in range(R)]
        ans = doit(R,C,map)

        output.write('Case #{}: {}\n'.format(I+1, ans))



if __name__ == "__main__":
    main()
