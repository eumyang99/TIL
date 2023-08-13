from pprint import pprint
import sys
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
robot = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]
lst[robot[0]][robot[1]] = 2

res = 1
stack = [(robot)]
while stack:
    x, y, d = stack.pop()
    for i in range(4):
        di = (d - i + 3) % 4
        nx, ny, nd = x+dx[di], y+dy[di], di
        if lst[nx][ny] == 0:
            res += 1
            lst[nx][ny] = 2
            pprint(lst)
            stack.append((nx, ny, nd))
            break
    else:
        di = abs(d-2)
        nx, ny = x+dx[di], y+dy[di]
        if lst[nx][ny] == 1:
            break
        stack.append((nx, ny, d))

print(res)

# 0 -1 -2 -3 -4
# 1  0 -1 -2- 3
# 2  1  0 -1 -2
# 3  2  1  0 -1
