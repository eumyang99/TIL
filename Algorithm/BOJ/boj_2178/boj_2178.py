import sys
input = sys.stdin.readline
from collections import deque

# readline으로 받을 때는 개행문자를 제거해야 한다.
# 이것 때문에 3번 틀렸네..ㅠㅠ
n, m = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(n)]

visited = [[n*m+1]*m for _ in range(n)]
visited[0][0] = 1
q = deque()
q.append((0,0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if lst[nx][ny] == 1:
                if visited[x][y] + 1 < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

print(visited[-1][-1])


