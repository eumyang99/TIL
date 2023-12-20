import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
INF = sys.maxsize

## 발상
## 1. 엘리베이터를 갈아탈 필요 없기 때문에 한 엘리베이터로 1층에서 n층까지 한 번에 이동한다
## 2. 무조건 출발점 -> 엘리베이터 -> 사장실 루트를 탄다
## 3. 따라서 최단거리 비교 횟수는 엘리베이터가 설치된 방의 개수이다

## 풀이
## 출발점과 사장실에서 시작한 다익스트라를 2개 구한다
## 전체 방을 순회하며 엘리베이터가 설치된 방마다 아래의 1, 2, 3 을 더한 값을 구해서 최소값을 출력한다
##  1) 출발점에서 엘리베이터까지의 소요 시간
##  2) 사장실 층까지 올라가는 엘리베이터 소요 시간
##  3) 엘리베이터에서 사장실까지의 소요 시간

def dijk(start):
    weight = [INF] * (n+1)
    weight[start] = 0
    que = [(0, start)]
    while que:
        w, s = heapq.heappop(que)

        if weight[s] < w:
            continue
        for next_w, next_s in edges[s]:
            new_w = w + next_w
            if new_w < weight[next_s]:
                weight[next_s] = new_w
                heapq.heappush(que, (new_w, next_s))
    
    return weight

START = 1
n, m, k = map(int, input().split())
edges = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    edges[s].append((w, e))
    edges[e].append((w, s))
elevator = [0] + list(map(int, input().split()))

start_dijk = dijk(START)
end_dijk = dijk(n)
res = INF
for room in range(1, n+1):
    if elevator[room] == -1: continue

    to_elevator = start_dijk[room]
    elevator_time = elevator[room]*(k-1)
    from_elevator = end_dijk[room]
    taking_time = to_elevator + elevator_time + from_elevator
    if taking_time < res:
        res = taking_time

print(res if res != INF else -1)