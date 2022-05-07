A = ord('A')

def simplify(x):
    ret = ''
    for i in range(len(x)):
        if i == 0 or x[i] != x[i-1]:
            ret += x[i]
    return ret

class Chain:
    def __init__(self, no) -> None:
        self.no = no
        self.l = None
        self.r = None

    def add_right(self, other):
        # print(self.no, other.no)
        other.l = self
        self.r = other
    
    def find_start(self):
        if self.l != None:
            return self.l.find_start()
        else:
            return self.no

    def find_end(self):
        if self.r != None:
            return self.r.find_end()
        else:
            return self.no
    
    def out(self):
        ret = []
        now = self
        while now != None:
            ret.append(now.no)
            now = now.r
        return ret

def doit():
    n = int(input())
    origin_str = input().split()
    simple_str = [simplify(x) for x in origin_str]
    # print(simple_str)
    only_char = [[False] * 26 for _ in range(n)]
    has_char = [[False] * 26 for _ in range(n)]
    chains = [Chain(i) for i in range(n)]

    for i in range(n):
        if len(simple_str[i]) == 1:
            only_char[i][ord(simple_str[i]) - A] = True
        for j in range(26):
            if chr(A+j) in simple_str[i]:
                has_char[i][j] = True
                if simple_str[i].count(chr(A+j)) > 1:
                    return 'IMPOSSIBLE'
    for i in range(26):
        # print(chr(A+i))
        has_it = [j for j in range(n) if has_char[j][i]]
        only_it = [j for j in range(n) if only_char[j][i]]
        not_only = [j for j in has_it if j not in only_it]

        starts = [chains[j].find_start() for j in has_it]
        if len(list(set(starts))) < len(starts):
            return 'IMPOSSIBLE'
        l = None
        r = None
        # print(not_only)
        if len(not_only) > 2:
            return 'IMPOSSIBLE'
        elif len(not_only) == 2:
            for imp in not_only:
                # print(simple_str[imp])
                if simple_str[imp][0] == chr(A+i):
                    r = chains[imp]
                elif simple_str[imp][-1] == chr(A+i):
                    l = chains[imp]
            if (l == None or r == None):
                # print(chr(A+i))
                return 'IMPOSSIBLE'
        elif len(not_only) == 1:
            imp = not_only[0]
            if simple_str[imp][0] == chr(A+i):
                r = chains[imp]
            elif simple_str[imp][-1] == chr(A+i):
                l = chains[imp]
            if (l == None and r == None and len(only_it) > 0):
                # print(chr(A+i))
                return 'IMPOSSIBLE'
        elif len(not_only) == 0:
            pass
        
        for j in range(1, len(only_it)):
            chains[only_it[j-1]].add_right(chains[only_it[j]])
        if (l != None and len(only_it) > 0):
            l.add_right(chains[only_it[0]])
        if (r != None):
            if len(only_it) > 0:
                chains[only_it[-1]].add_right(r)
            elif l != None:
                l.add_right(r)
   
    pairs = list(dict.fromkeys([(chain.find_start(), chain.find_end()) for chain in chains]))
    # print(pairs)
    for i in range(1, len(pairs)):
        chains[pairs[i-1][1]].add_right(chains[pairs[i][0]])

    retList = chains[pairs[0][0]].out()
    ret = ''
    for i in retList:
        ret += origin_str[i]
    return ret

T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))