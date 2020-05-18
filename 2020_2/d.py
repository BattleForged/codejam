import time
import heapq

def dijkstra(G,start):     ###dijkstra算法    
    INF = 10**12

    dis = [INF] * len(G)   # start到每个点的距离
    dis[start] = 0
    vis = [False] * len(G)    #是否访问过，1位访问过，0为未访问
    ###堆优化
    pq = []    #存放排序后的值
    heapq.heappush(pq,[dis[start],start])

    t3 = time.time()
    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
        if vis[v] == True:
            continue
        vis[v] = True
        for (node, disx) in G[v]:    #与v直接相连的点
            new_dis = dis[v] + disx
            if new_dis < dis[node] and (not vis[node]):    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis    #更新点的距离
              #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                heapq.heappush(pq,[dis[node],node])

    t4 = time.time()
    # print('Dijkstra算法所用时间:',t4-t3)
    return dis
    

"""
if __name__ == '__main__':
    
    G = {1:{1:0, 2:10, 4:30, 5:100},
         2:{2:0, 3:50},
         3:{3:0, 5:10},
         4:{3:20, 4:0, 5:60},
         5:{5:0},
         }
    distance,path = dijkstra(G,1)
    print(distance)
"""

def doit():
    [n, q] = [int(x) for x in input().split()]
    s = input()
    l = [int(x) for x in input().split()]
    r = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    next = [0] * n
    depth = [0] * n
    stack = 0
    for i in range(n):
        if s[i] == '(':
            depth[stack] = i
            stack += 1
        else:
            next[i] = depth[stack-1]
            next[depth[stack-1]] = i
            stack -= 1
    # print(next)
    b = [int(x) for x in input().split()]
    e = [int(x) for x in input().split()]
    G = []
    for i in range(n):
        tmp = {}
        if i > 0:
            tmp[i-1] = l[i]
        if i < n-1:
            tmp[i+1] = r[i]
        if next[i] != i+1 and next[i] != i-1:
            tmp[next[i]] = p[i]
        else:
            tmp[next[i]] = min(p[i], next[i])
        tmpx = []
        for key in tmp:
            tmpx.append((key,tmp[key]))
        G.append(tmpx)
    dd = []
    qq = []
    for i in range(q):
        qq.append((b[i]-1,e[i]-1))
    qq.sort()
    now = -1
    distance = []
    ans = 0
    for i in range(q):
        if (now < qq[i][0]):
            now = qq[i][0]
            distance = dijkstra(G,now)
        ans += distance[qq[i][1]]
    return ans

        
T = int(input())
for t in range(1, T + 1):
    print('Case #{}: {}'.format(t, doit()))