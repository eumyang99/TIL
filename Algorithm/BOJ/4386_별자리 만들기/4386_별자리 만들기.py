import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## 간선이 많으니까 Prim으로 풀었다.

def prim():
    pq = []
    visited = [0] * n
    pq.append((0, 0))
    
    cnt = 0
    res = 0
    while pq:
        w, e = heapq.heappop(pq)
        if visited[e] == 0:
            res += w
            visited[e] = 1
            if cnt == n:
                break
            
            for nw, ne in dic[e]:
                if visited[ne] == 0:
                    heapq.heappush(pq, (nw, ne))


    return res

n = int(input())
lst = [tuple(map(float, input().split())) for _ in range(n)]
dic = defaultdict(list)
for x in range(n-1):
    for y in range(x+1, n):
        w = ((lst[x][0] - lst[y][0]) ** 2 + (lst[x][1] - lst[y][1]) ** 2) ** (1/2)
        dic[x].append((w, y))
        dic[y].append((w, x))

result = prim()
print(round(result, 2))