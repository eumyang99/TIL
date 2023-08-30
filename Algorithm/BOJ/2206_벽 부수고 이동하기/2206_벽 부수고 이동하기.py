from collections import deque
import sys
input = sys.stdin.readline

## 정석적인 방법을 찾아보았다.
## visited에 거리를 계산할 때 벽을 깨고 온 거리와 벽을 깨지 않고 온 거리를 둘 다 기록한다.
## 그리고 que에 append할 때도 벽을 깨고 그 곳에 간건지 그냥 간건지를 기록한다(망치를 들고 그곳에 갔는지 망치를 써서 없는 상태로 그곳에 갔는지)
## 망치가 없는 상태로 다음 벽을 만났다면 que에 append하지 않는다.
## 망치가 있는 상태로 벽을 만났다면 que에 append하면서 망치가 없는 정보를 같이 넘긴다.
## 3차원 배열인데 상당히 헷갈린다.


## 나의 발상
## 시작점에서 BFS를, 도착점에서 BFS를 돌린다.
    ## 시작점에서 벽을 부수지 않고 이동하여 도착한 모든 지점의 거리를 start_arr 저장한다.
    ## 도착점에서도 마찬가지로 end_arr에 저장한다.
## 그리고 모든 벽을 순회하며
## 그 벽이 뚫렸을 때 이어지는 두 지점 A, B에 대해
## 시작점에서 A로 가는 거리 + 도착점에서 B로 가는 거리 + 1(벽 부수고 이동한 거리)
## 시작점에서 B로 가는 거리 + 도착점에서 A로 가는 거리 + 1(벽 부수고 이동한 거리)
## 이 둘 중 작은 것을 찾고 이것을 res(초기값 = 불가능한 큰 값)와 비교해서 작으면 갱신한다.
## res가 불가능한 값이면 -1을 그렇지 않으면 res를 출력한다.

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def bfs(sx, sy):
    que = deque()
    que.append((sx, sy, 1))
    visited = [[n*m+1]*m for _ in range(n)]
    visited[sx][sy] = 1
    while que:
        x, y, cnt = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not lst[nx][ny] and visited[nx][ny] == n*m+1:
                visited[nx][ny] = cnt+1
                que.append((nx, ny, cnt+1))

    return visited

n, m = map(int, input().split())
lst = [list(map(int, input().rstrip())) for _ in range(n)]

start_arr = bfs(0, 0)
end_arr = bfs(n-1, m-1)
res = n*m+1 if start_arr[n-1][m-1] == n*m+1 else start_arr[n-1][m-1]
for x in range(n):
    for y in range(m):
        if lst[x][y]:
            for i in range(2):
                a, b = i, i+2
                ax, ay = x + dx[a], y + dy[a]
                bx, by = x + dx[b], y + dy[b]
                if 0 <= ax < n and 0 <= ay < m and 0 <= bx < n and 0 <= by < m and not lst[ax][ay] and not lst[bx][by]:
                    res = min(res, min(start_arr[ax][ay] + end_arr[bx][by], start_arr[bx][by] + end_arr[ax][ay])+1)

print(res if res != n*m+1 else -1)