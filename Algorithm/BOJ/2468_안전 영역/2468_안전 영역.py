import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
flood = [[1]*n for _ in range(n)]

max_h = 0
for row in lst:
    temp = max(row)
    if temp > max_h:
        max_h = temp

res = 1
for h in range(1, max_h):
    temp = 0

    for x in range(n):
        for y in range(n):
            if lst[x][y] <= h:
                flood[x][y] = 0

    visited = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            stack = []
            if flood[x][y] == 1 and visited[x][y] == False:
                stack.append((x,y))
                visited[x][y] = True
                while stack:
                    a, b = stack.pop()
                    for d in range(4):
                        nx, ny = a-dx[d], b-dy[d]
                        if 0 <= nx < n and 0 <= ny < n and flood[nx][ny] == 1 and visited[nx][ny] == False:
                            stack.append((nx, ny))
                            visited[nx][ny] = True
                else:
                    temp += 1
    
    if temp > res:
        res = temp

print(res)