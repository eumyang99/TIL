from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
dz = [-1, 1]

n, m ,h = map(int, input().split())

lst = []
temp = []
for i in range(1, m*h+1):
    temp.append(list(map(int, input().split())))
    if i % m == 0:
        lst.append(temp)
        temp = []


not_ready = 0
stack = deque()
for z in range(h):
    for x in range(m):
        for y in range(n):
            if lst[z][x][y] == 1:
                stack.append((z,x,y))
            elif lst[z][x][y] == 0:
                not_ready += 1

res = 0
temp = []
while stack:
    z, x, y = stack.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and lst[z][nx][ny] == 0:
            lst[z][nx][ny] = 1
            not_ready -= 1
            temp.append((z, nx, ny))
    for i in range(2):
        nz = z + dz[i]
        if 0 <= nz < h and lst[nz][x][y] == 0:
            lst[nz][x][y] = 1
            not_ready -= 1
            temp.append((nz, x, y))
    if len(stack) == 0:
        stack = deque(temp[:])
        temp = []
        res += 1

print(res-1 if not_ready == 0 else -1)


