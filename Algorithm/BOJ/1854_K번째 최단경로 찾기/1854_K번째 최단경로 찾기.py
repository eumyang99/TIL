import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## 발상
## heap을 사용하는 다익스트라는 pq에서 나오는 거리 자체가 가장 짧은 거리가 나온다.
## 따라서 A에서 B로 이동하는 가중치가 처음에 3이 나왔고 차후 6이 나왔다면 A에서 B로 가는 가장 짧은 가중치는 3과 6이다.
## 그리고 k가 2일 때, A에서 B를 거쳐 C로 가야 한다면 A에서 B로 가는 3과 6 이외의 다른 경로가 필요치 않다.
## EX) A -> B : 3, 6 // B -> C : 3, 5
## 굳이 A -> B : 3, 6, 8인 경우가 필요치 않다. 8은 B를 지나 다른 노드로 가는 경로에 필요치 않다. 
## k가 3이면 필요하다.

## 따라서 pq에서 pop한 노드에 몇번째 도착한 건지 확인한다.
## k번 보다 덜 도착한 상황이면 그 거리를 저장하고 도착 카운트를 늘린다.
## 그리고 해당 노드에서 갈 수 있는 노드를 pq에 담을 때,
## 그 노드의 도착 카운트를 확인하고 도착 카운트가 충족 됐다면 굳이 pq에 넣지 않는다.

def dijk(start_node):
    pq = [(0, start_node)]
    ## 가중치를 이차원배열로 만들어서 노드에 도착하면 넣는다.
    weight = list([] for _ in range(n+1))
    ## 해당 노드에 몇번 도착했는지 카운트
    visited = [0] * (n+1)
    while pq:
        w, e = heapq.heappop(pq)
        ## 해당 노드에 k번 이하로 도착했다면
        if visited[e] < k:
            ## 도착 카운트 늘려주고
            visited[e] += 1
            ## 해당 노드로 도착한 가중치를 추가한다
            ## max_heap을 사용한다.
            heapq.heappush(weight[e], -w)
        ## 해당 노드에 이미 충분히 도착했다면 넘어간다
        else:
            continue

        ## 해당 노드에서 갈 수 있는 노드를 순회하며
        for nw, ne in dic[e]:
            ## 만약 다음 갈 노드의 도착 카운트가 k보다 작다면 가야하니까
            if visited[ne] < k:
                ## 가중치 누적하고
                new_weight = w + nw
                ## heap에 넣는다
                heapq.heappush(pq, (new_weight, ne))
    return (visited, weight)

n, m, k = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(dic[s], (w, e))


visited, weight = dijk(1)

## 각 노드를 순회하며
for node in range(1, n+1):
    ## 해당 노드의 도착 카운트를 확인하고 k보다 작다면 -1을
    if visited[node] < k:
        print(-1)
    ## 그렇지 않다면 가중치를 출력한다
    else:
        ## max_heap으로 저장했기 때문에 가장 첫 인덱스에 -1을 곱해서 출력
        print(-weight[node][0])
