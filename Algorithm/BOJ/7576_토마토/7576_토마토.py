import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]

not_ready = 0
q = []
for x in range(m):
    for y in range(n):
        if lst[x][y] == 0:
            not_ready += 1
        elif lst[x][y] == 1:
            q.append((x, y))

res = 0
while q:
    n_q = []
    for x, y in q:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if lst[nx][ny] == 0:
                    lst[nx][ny] = 1
                    n_q.append((nx, ny))
                    not_ready -= 1
    res += 1
    q = n_q

print(res if not_ready == 0 else -1)


    





