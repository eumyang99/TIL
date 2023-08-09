from pprint import pprint
import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize

## 2차원 배열에서 다익스트라 활용!
## heapq에 담아 짧은 거리부터 지나가기 때문에
## 무료로 갈 수 있는 곳을 먼저 다 순회한다.
## 그리고 나서 가중치가 있는 곳의 주변을 탐색하기 때문에
## 가장 싼 녀석들을 방문하고 그리고 그 다음 싼 녀석들 전부, 그리고 그 다음 싼 녀석들 전부...
## 이런 식으로 진행된다.
## 따라서 while문을 통해 목표 노드에 도달했다는 것은 가장 싸게 도달했다는 뜻.

n = int(input())
lst = [list(map(int, input().rstrip())) for _ in range(n)]

weight = [[INF]*(n) for _ in range(n)]
weight[0][0] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pq = [(0, 0, 0)]

while pq:
    # 해당 노드에서 
    w, x, y = heapq.heappop(pq)
    if (x, y) == (n-1, n-1):
        break
    ## 네 방향을 다 탐색한다
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            ## 탐색한 한 곳이 빈방이라면
            if lst[nx][ny] == 1:
                ## 현재까지 온 거리 보다 해당 방까지의 거리가 더 크다면
                ## (만약 같다면 추가하지 않는다. 값이 작을 때만 추가한다. 따라서 while문의 반복이 무한하지 않다.)
                if weight[nx][ny] > w:
                    ## 현재까지의 거리를 해당 방의 거리로 갱신하고
                    weight[nx][ny] = w
                    ## 갈 곳의 노드를 heap에 담는다.
                    heapq.heappush(pq, (w, nx, ny))
            ## 탐색한 곳이 검은 방이라면
            else:
                ## 현재까지 온 거리 + 1(검은 방이라 개척해야 하니까)이 해당 방까지의 거리보다 작다면
                if weight[nx][ny] > w + 1:
                    ## 현재까지 온 거리 + 1 로 해당 방의 거리를 갱신하고
                    weight[nx][ny] = w + 1
                    ## 갈 곳의 노드를 heap에 담는다.
                    heapq.heappush(pq, (w+1, nx, ny))
pprint(weight)
print(weight[n-1][n-1])



## 발상
## 모든 덩어리(node)를 bfs로 구한다.
## 모든 node를 이루고 있는 좌표를 모두 비교하며 node간의 가중치를 구하고
## dijkstra를 돌린다.
## 이 발상은 노드 간의 거리를 구한다는 점에서 너무 오래 걸린다.
## 따라서 쓰레기 발상!

# def dijk(start, node_cnt):
#     weight = [INF] * node_cnt
#     weight[start] = 0
#     pq = [(0, start)]
#     while pq:
#         w, e = heapq.heappop(pq)
#         if e == end:
#             return weight[end]
#         if w > weight[e]:
#             continue
#         for nw, ne in dic[e]:
#             new_w = w + nw
#             if weight[ne] > new_w:
#                 weight[ne] = new_w
#                 heapq.heappush(pq, (new_w, ne))


# n = int(input())
# lst = [list(map(int, input().rstrip())) for _ in range(n)]

# visited = [[0]*(n) for _ in range(n)]
# node = []

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# for x in range(n):
#     for y in range(n):
#         if visited[x][y] == 0 and lst[x][y] == 1:
#             que = deque()
#             que.append((x, y))
#             temp_nodes = [(x, y)]
#             visited[x][y] = 1
#             while que:
#                 p, q = que.popleft()
#                 for i in range(4):
#                     nx, ny = p+dx[i], q+dy[i]
#                     if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and lst[nx][ny] == 1:
#                         temp_nodes.append((nx, ny))
#                         visited[nx][ny] = 1
#                         que.append((nx, ny))
#             node.append(temp_nodes)

# dic = defaultdict(list)
# node_cnt = len(node)
# for x in range(node_cnt-1):
#     for y in range(x+1, node_cnt):
#         weight = INF
#         for p in range(len(node[x])):
#             for q in range(len(node[y])):
#                 dx = abs(node[x][p][0] - node[y][q][0])
#                 dy = abs(node[x][p][1] - node[y][q][1])
#                 if dx + dy - 1 < weight:
#                     weight = dx + dy - 1
#         dic[x].append((weight, y))
#         dic[y].append((weight, x))

# for i in range(node_cnt):
#     if (0,0) in node[i]:
#         start = i
#         break
# for i in range(node_cnt-1, -1, -1):
#     if (n-1, n-1) in node[i]:
#         end = i
#         break

# print(dijk(start, node_cnt))

