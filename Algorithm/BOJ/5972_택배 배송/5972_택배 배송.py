import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## 기본적인 다익스트라

def dijk(start_node, end_node):
    weight = [50000001] * (n + 1)
    weight[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        w, e = heapq.heappop(pq)
        if e == end_node:
            return weight[end_node]
        
        if w > weight[e]:
            continue
        
        for nw, ne in dic[e]:
            new_weight = w + nw
            if new_weight < weight[ne]:
                weight[ne] = new_weight
                heapq.heappush(pq, (new_weight, ne))

n, m = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(dic[s], (w, e))
    heapq.heappush(dic[e], (w, s))

print(dijk(1, n))

