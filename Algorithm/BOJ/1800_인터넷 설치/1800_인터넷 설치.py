from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 발상(구글링 참고)
## 정말 어려운 문제이다.
## 다익스트라의 작동 원리를 정확히 알아야 풀 수 있는 문제이다.
## 나아가 이분탐색을 활용할 수 있어야 한다.

## 지불할 금액을 이분탐색으로 지정한다.
## 해당 금액(cost)를 기준으로
## cost를 넘는 간선이라면 각 노드까지 가는 초과 카운팅을 +1
## cost를 넘지 않는 간선이라면 각 노드까지 가는 초과 카운팅을 그대로 유지한다.
## 목표 노드에 도착했을 때 cost를 몇번 초과했는지 확인 후
## 초과했으면 이분탐색에서 left를 mid + 1
## 초과하지 않았으면 더 작은 cost도 가능하지 확인하기 위해 right 를 mid - 1
## 이분탐색이 끝나고 결과를 출력한다.

def dijk(norm):
    weight = [float("inf")] * (n+1)
    pq = [(0, 1)]
    weight[1] = 0
    while pq:
        w, e = heapq.heappop(pq)
        if e == n:
            return weight[n]
        if w > weight[e]:
            continue

        for nw, ne in dic[e]:
            if nw > norm:
                if weight[ne] > w + 1:
                    weight[ne] = w + 1
                    heapq.heappush(pq, (w+1, ne))
            else:
                if weight[ne] > w:
                    weight[ne] = w
                    heapq.heappush(pq, (w, ne))
    return weight[n]

n, p, k = map(int, input().split())
dic = defaultdict(list)
for _ in range(p):
    s, e, w  = map(int, input().split())
    dic[s].append((w, e))
    dic[e].append((w, s))

left = 0
right = 1000000
res = -1

while left <= right:
    mid = (left + right) // 2
    if dijk(mid) <= k:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
