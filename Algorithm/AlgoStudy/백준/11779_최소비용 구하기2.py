## 발상
## 다익스트라로 최소비용을 갱신해 가면서
## 특정 노드까지의 비용이 갱신될 때마다 이전 노드와 parent 관계를 기록
## 목표 노드에 도착하면 도착 노드부터 parent를 추적하며 경로 확인

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijk(n, start, end):
    parent = [i for i in range(n+1)]
    weight = [INF] * (n+1)
    weight[start] = 0

    que = [(0, start, start)]
    while que:
        w, node, before_node = heapq.heappop(que)
        if weight[node] < w: continue
        parent[node] = before_node
        if node == end:
            break

        for (next_weight, next_node) in dic[node]:
            new_weight = next_weight + w
            if new_weight < weight[next_node]:
                weight[next_node] = new_weight
                heapq.heappush(que, (new_weight, next_node, node))


    answer_weight = weight[end]
    answer_cnt = 0
    answer_route = []
    
    node = end
    while parent[node] != node:
        answer_route.append(node)
        answer_cnt += 1
        node = parent[node]
    else:
        answer_route.append(node)
        answer_cnt += 1
        answer_route.reverse()

    print(answer_weight)
    print(answer_cnt)
    print(*answer_route)



n, m = int(input()), int(input())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    dic[s].append((w, e))
start, end = map(int, input().split())
dijk(n, start, end)