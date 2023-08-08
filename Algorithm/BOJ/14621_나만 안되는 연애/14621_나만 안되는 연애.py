from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 크루스칼과 프림으로 풀어 봤다

## 1. 프림
def prim(start):
    visited = [0] * (n+1)
    res = 0
    pq = [(0, start)]
    cnt = n
    while pq:
        w, e = heapq.heappop(pq)
        if visited[e] == 0:
            visited[e] = 1
            res += w
            cnt -= 1
            if cnt == 0:
                break
            for nw, ne in dic[e]:
                if visited[ne] == 0:
                    heapq.heappush(pq, (nw, ne))
    if cnt == 0:
        return res
    else:
        return -1


n ,m = map(int, input().split())
mfm = tuple(input().split())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    if mfm[s-1] != mfm[e-1]:
        dic[s].append((w, e))
        dic[e].append((w, s))
else:
    start = s

print(prim(start))

## 2. 크루스칼
# def find(x):
#     if x == parent[x]:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

# def union(ps, pe):
#     parent[pe] = ps

# n ,m = map(int, input().split())
# mfm = tuple(input().split())
# pq = []
# for _ in range(m):
#     s, e, w = map(int, input().split())
#     if mfm[s-1] != mfm[e-1]:
#         heapq.heappush(pq, (w, s, e))

# parent = [i for i in range(n+1)]

# res = 0
# cnt = n-1
# for _ in range(len(pq)):
#     w, s, e = heapq.heappop(pq)
#     ps, pe = find(s), find(e)
#     if ps != pe:
#         union(ps, pe)
#         res += w
#         cnt -= 1
#         if cnt == 0:
#             break

# print(res if cnt == 0 else -1)