import heapq
from collections import defaultdict, deque
import sys
# sys.stdin = open('C:\\Users\\RYU\\Desktop\\github\\Algorithm\\BOJ\\5719_거의 최단 경로\\input.txt')
input = sys.stdin.readline
INF = sys.maxsize

## 풀이 참조
## 1. 간선 정보를 받을 때, 간선 정보와, 역 간선 정보를 같이 저장한다.
## 2. 처음 다익스트라를 돌려서 최단 거리 리스트를 만든다.
## 3. 도착점에서부터 bfs를 돌리면서 최단 거리 리스트를 활용해 최단 경로를 이루는 간선을 set에 저장한다
## 4. 최단 경로를 이루는 간선을 제외하며 다시 다익스트라를 돌린다
## 5. 도착점 거리를 출력한다

## 2. 추가 설명
## 다익스트라를 돌리면서 도착점에 도착하면 다익스트라 함수를 끝낸다
## 그래도 되는 이유는 처음 도착점에 도착했을 때 큐에 담긴 가중치들은 도착점까지의 가중치와 같거나 크다(heapq)
## 따라서 도착점에 도착하기 바로 전 노드들까지 이미 weight 리스트에 담겨있는 상태이다

## 3. 추가 설명
## 도착점에서 역 간선 정보를 활용하여 bfs를 돌린다
## 만약 역으로 탐색 중 큐에 담긴 노드가 3번이라고 할 때,
## 3번에서 역으로 갈 수 있는 노드가 2번이라고 하자
## 이때 (2번에서 3번으로 가는 가중치)와 weight 리스트에 담긴 (weight[2])를 더한 값이 weight[3]과 같다면 최단 경로에 포함되는 도로이다
## 왜냐하면 다익스트라로 만든 weight 리스트는 시작점에서 도착점까지 갈 때 거치는 모든 노드들에 대한 최단 거리를 담고 있기 때문이다
## 위 조건에 만족하면 다시 역추적을 위해 que에 2번 노드를 담는다

def dijk(n, start, end, dic, used_road):
    weight = [INF] * n
    weight[start] = 0
    que = [(0, start)]

    while que:
        w, e = heapq.heappop(que)

        if e == end:
            break

        if w > weight[e]:
            continue
        
        for nw, ne in dic[e]:
            if (e, ne) in used_road:
               continue
            new_weight = nw + w
            if new_weight < weight[ne]:
                weight[ne] = new_weight
                heapq.heappush(que, (new_weight, ne))

    return weight

def get_used_road(weight_lst, rev_dic, start, end):
    used_road = set()
    que = deque([end])
    while que:
       now_node = que.popleft()

       if now_node == start:
           continue

       for w, pre_node in rev_dic[now_node]:
          if weight_lst[pre_node] + w == weight_lst[now_node] and (pre_node, now_node) not in used_road:
             que.append(pre_node)
             used_road.add((pre_node, now_node))

    return used_road

def make_dic(m):
    dic = defaultdict(list)
    rev_dic = defaultdict(list)

    for _ in range(m):
        s, e, w = map(int, input().split())
        dic[s].append((w, e))
        rev_dic[e].append((w, s))
    
    return dic, rev_dic

while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    dic, rev_dic = make_dic(m)

    weight_lst = dijk(n, start, end, dic, {})
    if weight_lst[end] == INF:
        print(-1)
        continue

    used_road = get_used_road(weight_lst, rev_dic, start, end)
    res_weight_lst = dijk(n, start, end, dic, used_road)
    print(res_weight_lst[end] if res_weight_lst[end] != INF else -1)
