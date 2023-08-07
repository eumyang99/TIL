import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## MST는 크루스칼로
## 최장거리경로는 다익스트라와 BFS로 풀어봤음
## 그러나 다익스트라로 최대거리를 구할 때

# start_node1 = 0
# distance1 = dijkstra(start_node1)
# start_node2 = max(range(n), key=lambda x: distance1[x])
# distance2 = dijkstra(start_node2)

# 이렇게 다익스트라를 두 번만 사용해서 최대거리를 구하는데 이게 왜 가능한지 이해가 안된다.


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(ps, pe):
    parent[pe] = ps


# def dijk(start):
#     weight_lst = [float("inf")] * n
#     weight_lst[start] = 0
#     pq = [(0, start)]
#     cnt = 0

#     while pq:
#         w, e = heapq.heappop(pq)
#         if w > weight_lst[e]:
#             continue
#         cnt += 1
#         for nw, ne in dic[e]:
#             if w + nw < weight_lst[ne]:
#                 weight_lst[ne] = w + nw
#                 heapq.heappush(pq, (weight_lst[ne], ne))
#         if cnt == n:
#             break
#     return max(weight_lst)

def bfs(start):
    visited = [-1] * n
    visited[start] = 0
    q = [start]

    while q:
        start = q.pop(0)
        for w, e in dic[start]:
            if visited[e] == -1:
                visited[e] = visited[start] + w
                q.append(e)
    return max(visited)
    






n, m = map(int, input().split())
pq = []
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(pq, (w, s, e))

parent = [i for i in range(n)]


dic = defaultdict(list)

res = 0
cnt = 0
for _ in range(m):
    w, s, e = heapq.heappop(pq)
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        dic[s].append((w, e))
        dic[e].append((w, s))
        if cnt == n-1:
            break
print(res)

# expensive_1 = 0
# for start in dic.keys():
#     temp = dijk(start)
#     if temp > expensive_1:
#         expensive_1 = temp

# print(expensive_1)

expensive_2 = 0
for start in dic.keys():
    temp = bfs(start)
    if temp > expensive_2:
        expensive_2 = temp

print(expensive_2)
