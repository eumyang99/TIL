from collections import deque
import sys
input = sys.stdin.readline


## 발상
## bfs로 갈 수 있는 가장 가까운 먹이를 찾아간다.
## 그곳에서 새롭게 다시 bfs를 돌려서 가장 가까운 먹이를 찾아간다.
## 반복


## 상 좌 우 하
dx, dy = [-1, 0, 0, 1], [0, -1 ,1, 0]


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    for y in range(n):
        if lst[x][y] == 9:
            now = (x, y)
            lst[x][y] = 0

res = 0

visited = [[0]*n for _ in range(n)]
visited[now[0]][now[1]] = 1
que = []
size = 2
eat = 0
dist = 1
stack = deque([now])
temp = []
while stack:
    x, y = stack.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] <= size and visited[nx][ny] == 0:
            if 0 < lst[nx][ny] < size:
                que.append((dist, nx, ny))
            visited[nx][ny] = 1
            temp.append((nx, ny))

    if len(stack) == 0:
        
        if que:
            que.sort(key= lambda x: (x[0], x[1], x[2]))
            res += que[0][0]
            stack = deque([(que[0][1], que[0][2])])
            dist = 1
            temp = []
            visited = [[0]*n for _ in range(n)]
            visited[que[0][1]][que[0][2]] = 1
            eat += 1
            lst[que[0][1]][que[0][2]] = 0
            que = []
            if eat == size:
                eat = 0
                size += 1
            continue
        stack = deque(temp)
        temp = []
        dist += 1

print(res)


