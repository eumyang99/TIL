from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 발상
## 기본적인 다익스트라의 정석적인 풀이이다.


INF = sys.maxsize

def dijk(start, end):
    weight = [INF] * (n+1)
    pq = [(0, start)]
    while pq:
        w, e = heapq.heappop(pq)
        if e == end:
            return weight[end]
        
        if w > weight[e]:
            continue
        
        for nw, ne in dic[e]:
            new_weight = w + nw
            if new_weight < weight[ne]:
                weight[ne] = new_weight
                heapq.heappush(pq, (new_weight, ne))


n = int(input())
m = int(input())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    dic[s].append((w, e))
start, end = map(int, input().split())

print(dijk(start, end))