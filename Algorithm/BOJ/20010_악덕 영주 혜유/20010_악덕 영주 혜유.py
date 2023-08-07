import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## 프림으로 풀어봤다.

def prim(start):
    visited = [0] * n
    pq = []
    pq.append((0, start))
    res = []
    cnt = 0
    while pq:
        w, e = heapq.heappop(pq)
        if visited[e] == 0:
            res.append((w, e))
            visited[e] = 1
            cnt += 1
            if cnt == n:
                break
            for w, e in dic[e]:
                if visited[e] == 0:
                    heapq.heappush(pq, (w, e))
    return res


n, k = map(int, input().split())
dic = defaultdict(list)
for _ in range(k):
    s, e, w = map(int, input().split())
    dic[s].append((w, e))
    dic[e].append((w, s))
else:
    start = s

lst = prim(s)
cost = 0
for e in lst:
    cost += e[0]
print(cost)


