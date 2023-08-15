import sys
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
robot = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]
lst[robot[0]][robot[1]] = 2

res = 1
x, y, d = robot
while 1:
    for i in range(4):
        di = (d - i + 3) % 4
        nx, ny, nd = x+dx[di], y+dy[di], di
        if lst[nx][ny] == 0:
            res += 1
            lst[nx][ny] = 2
            x, y, d = nx, ny, nd
            break
    else:
        di = (d + 2) % 4
        nx, ny = x+dx[di], y+dy[di]
        if lst[nx][ny] == 1:
            break
        x, y, d = nx, ny, d

print(res)

