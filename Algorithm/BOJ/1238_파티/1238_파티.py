from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 다익스트라로 풀었다
## 먼저 파티장에서 돌아오는 거리를 한번 구하고
## 모든 출발점에 대해서 파티장으로 가는 거리를 구했다
## 아직 확실히 이해되진 않았지만 pq에서 pop 되는 간선은 이미 확정된 간선이라고 생각
## 따라서 파티장으로 갈 때는 파티장 노드가 pq에서 pop되면 멈췄다.
## 그리고 거리의 합을 구해서 최대값을 찾았다.

def dijk(start):
    weight = [float("inf")] * (n+1)
    weight[start] = 0
    pq = [(0, start)]

    while pq:
        w, e = heapq.heappop(pq)
        if start != x and e == x:
            break
        if w > weight[e]:
            continue
        for nw, ne in dic[e]:
            new_weight = nw + w
            if new_weight < weight[ne]:
                weight[ne] = new_weight
                heapq.heappush(pq, (new_weight, ne))

    return(weight)



n, m, x = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    dic[s].append((w, e))

back = dijk(x)

res = 0
for start in range(1, n+1):
    if start != x:
        go = dijk(start)
        cost = go[x] + back[start]
        if cost > res:
            res = cost

print(res)