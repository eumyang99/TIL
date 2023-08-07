from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijk(start):
    dist = [float("inf")] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        ## w는 여기 까지 e노드까지 왔을 때 걸리는 누적거리
        w, e = heapq.heappop(pq)

        ## e노드까지 걸리는 누적거리가 기존의 누적거리보다 크다면
        ## 이 간선은 pass
        if dist[e] < w:
            continue

        for nw, ne in dic[e]:
            ## nw는 ne노드까지 갈 때 걸리는 거리
            ## nd는 ne노드까지 갈 때 걸리는 누적거리
            nd = nw + w
            ## 그 누적거리가 현재 ne까지 가는데 걸리는 거리보다 작다면
            if nd < dist[ne]:
                ## ne까지 가는데 걸리는 거리를 갱신하고
                dist[ne] = nd
                ## 거리가 갱신되었으니 그 노드로부터 새롭게 뻗어나가기 위해 pq에 담음
                heapq.heappush(pq, (nd, ne))

    for d in dist[1:]:
        if d == float("inf"):
            print("INF")
        else:
            print(d)


n, m = map(int, input().split())
start = int(input())
dic = defaultdict(list)
for _ in range(m):
    s, e, w =  map(int, input().split())
    dic[s].append((w, e))

dijk(start)

