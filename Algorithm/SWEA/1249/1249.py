from collections import deque
import sys
sys.stdin = open('input.txt')
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 이게 왜 돌아갈까....

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]

    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = 0
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y] + lst[nx][ny]:
                    visited[nx][ny] = visited[x][y] + lst[nx][ny]
                    q.append((nx, ny))


    print(f'#{case+1} {visited[-1][-1]}')

