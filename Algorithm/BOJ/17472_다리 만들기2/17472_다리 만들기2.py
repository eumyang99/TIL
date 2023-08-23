import heapq
import sys
input = sys.stdin.readline

## 발상
## 1. dfs를 돌며 섬들의 좌표를 묶는다.
## 2. 각 섬의 좌표들을 순회하며 문제의 조건에 맞는 다른 섬을 찾고 (거리, 시작점, 도착점)을 heapq에 저장한다.
## 3. 크루스칼을 활용해서 mst를 구한다.

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(ps, pe):
    parent[pe] = ps



dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

## 섬의 좌표들을 묶어 node에 담는 과정
node = []
visited = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if lst[x][y] == 1 and visited[x][y] == 0:
            temp = [(x, y)]
            visited[x][y] = 1
            stack = [(x, y)]
            while stack:
                px, py = stack.pop()
                for i in range(4):
                    nx, ny = px+dx[i], py+dy[i]
                    if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        temp.append((nx, ny))
                        stack.append((nx, ny))
            else:
                node.append(temp)

## 편의를 위해서 섬의 좌표값들을 섬의 번호로 바꿈(땅에 섬의 번호 표시)
## input 받은 lst에서는 모든 땅이 1로 되어 있으니까 불편
map = [[0]*m for _ in range(n)]
for i in range(1, len(node)+1):
    for x, y in node[i-1]:
        map[x][y] = i

## 섬의 각 좌표를 순회하며 다른 섬들과의 거리를 저장하는 과정
pq = []
for i in range(1, len(node)+1):
    for x, y in node[i-1]:
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            dist = 0
            while 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == i:
                    break
                if map[nx][ny] != 0:
                    if dist == 1:
                        break
                    heapq.heappush(pq, (dist, i, map[nx][ny]))
                    break
                else:
                    nx += dx[d]
                    ny += dy[d]
                    dist += 1

## 출력할 res
res = 0

## 크루스칼을 멈출 cnt
## mst는 간선의 개수가 노드의 개수 - 1임을 활용
cnt = 0

## union-find를 위한 parent 리스트
parent = [i for i in range(len(node)+1)]

## union-find
while pq:
    w, s, e = heapq.heappop(pq)
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        ## 연결한 간선 개수 cnt에 추가
        cnt += 1
        ## 가충치 누적
        res += w
        ## mst 완성했으면 그만!
        if cnt == len(node)-1:
            break 

## mst를 완성하지 못했으면(연결한 간선 개수 != 노드 개수 - 1) -1 출력
print(res if cnt == len(node)-1 else -1)
