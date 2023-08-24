from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 풀이법
## 잡텐더 친구들과 스터디를 하면서 트리의 지름을 구하는 개념에 대해 상의했었다.
## 트리의 지름(즉, mst에서 가장 큰 누적 가중치를 갖는 경로)은
## 임의의 노드에서 가장 먼 노드를 찾고
## 그 찾은 노드에서 가장 먼 노드를 찾으면 된다.
## 필연적으로 그것이 트리의 지름이 된다.
## 따라서 다익스트라를 두 번 사용하면 된다.


INF = sys.maxsize

def dijk(start, ready):
    weight = [INF] * (n+1)
    weight[start] = 0
    pq = [(0, start)]

    cnt = 0
    while pq:
        w, e = heapq.heappop(pq)

        if w > weight[e]:
            continue

        cnt += 1
        if cnt == n:
            if ready:
                m = weight.index(max(weight[1:]))
                return dijk(m, False)
            else:
                return print(max(weight[1:]))
            
        for nw, ne in dic[e]:
            new_weight = w + nw
            if weight[ne] > new_weight:
                weight[ne] = new_weight
                heapq.heappush(pq, (new_weight, ne))



n = int(input())
if n == 1:
    print(0)
else:
    dic = defaultdict(list)
    for _ in range(n-1):
        s, e, w = map(int, input().split())
        dic[s].append((w, e))
        dic[e].append((w, s))
    else:
        start = s

    dijk(start, True)

