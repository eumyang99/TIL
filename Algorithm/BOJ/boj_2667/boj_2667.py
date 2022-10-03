import sys
input = sys.stdin.readline

n = int(input().strip())
lst = [list(map(int, input().strip())) for _ in range(n)]


stack = []
visited = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = []
for x in range(n):
    for y in range(n):
        if lst[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            stack.append((x,y))
            temp = 1
            while stack:
                x, y = stack[-1]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if lst[nx][ny] == 1 and visited[nx][ny] == 0:
                            temp += 1
                            visited[nx][ny] = 1
                            stack.append((nx, ny))
                            break
                else:
                    stack.pop()
            cnt.append(temp)


print(len(cnt))
cnt.sort()
for i in cnt:
    print(i)