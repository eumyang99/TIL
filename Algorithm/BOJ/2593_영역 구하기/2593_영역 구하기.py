import sys
inpu = sys.stdin.readline

## 발상
## 단순 dfs 완전탐색

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

n, m, k = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(k)]

map = [[0]*m for _ in range(n)]


for x, y, p, q in lst:
    for row in range(y, q):
        for col in range(x, p):
            map[row][col] = 1

res = []
for x in range(n):
    for y in range(m):
        if not map[x][y]:
            cnt = 1
            stack = [(x, y)]
            map[x][y] = [1]
            while stack:
                x, y = stack.pop()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not map[nx][ny]:
                        map[nx][ny] = 1
                        cnt += 1
                        stack.append((nx, ny))
            res.append(cnt)

res.sort()
print(len(res))
print(*res)

