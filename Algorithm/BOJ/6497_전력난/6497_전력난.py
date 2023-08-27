import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline


## 프림

def prim(start, n):
    res = 0
    visited = [0]*n
    pq = [(0, start)]
    cnt = 0
    while pq:
        w, e = heapq.heappop(pq)
        if not visited[e]:
            visited[e] = 1
            res += w
            cnt += 1
            if cnt == n:
                return res
            for nw, ne in dic[e]:
                if not visited[ne]:
                    heapq.heappush(pq, (nw, ne))

while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    else:
        dic = defaultdict(list)
        total = 0
        for _ in range(m):
            s, e, w = map(int, input().split())
            dic[s].append((w, e))
            dic[e].append((w, s))
            total += w
        else:
            start = s

        print(total - prim(start, n))


# ## 크루스칼

# def find(x):
#     if x == parent[x]:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

# while 1:
#     n, m = map(int, input().split())
#     if n == 0:
#         break
#     else:
#         pq = []
#         total = 0
#         for _ in range(m):
#             s, e, w = map(int, input().split())
#             heapq.heappush(pq, (w, s, e))
#             total += w

#         parent = [i for i in range(n)]

#         res = 0
#         cnt = 0
#         while pq:
#             w, s, e = heapq.heappop(pq)
#             ps, pe = find(s), find(e)
#             if ps != pe:
#                 res += w
#                 cnt += 1
#                 if cnt == n-1:
#                     print(total - res)
#                     break
#                 parent[pe] = ps











