# 다익스트라 사용
from collections import deque
import heapq
INF = 50001


def solution(n, edge):
    edges = [[] for _ in range(n + 1)]
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)

    def dijk(start):
        weight = [INF] * (n + 1)
        weight[start] = 0
        weight[0] = 0
        que = [(0, start)]
        while que:
            w, s = heapq.heappop(que)
            if weight[s] < w:
                continue

            for next in edges[s]:
                if weight[next] <= w + 1:
                    continue
                weight[next] = w + 1
                heapq.heappush(que, (weight[next], next))

        return weight

    weight = dijk(1)
    return weight.count(max(weight))


# BFS 사용
def solution(n, edge):
    edges = [[] for _ in range(n + 1)]
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)

    dist = [-1] * (n + 1)
    dist[1] = 0
    que = deque([1])
    while que:
        n = que.popleft()
        for next in edges[n]:
            if dist[next] != -1:
                continue
            dist[next] = dist[n] + 1
            que.append(next)

    return dist.count(max(dist))
