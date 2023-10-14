import sys
input = sys.stdin.readline

## 상 우 하 좌
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def uu(red, blue, befor_dir, cnt):
    global res

    if cnt > 10:
        return 
    if red_flag == True and blue_flag == True:
        return 
    if red_flag == True:
        res = min(res, cnt)
        return
    if blue_flag == True:
        return
    

    if befor_dir == -1: ## 처음
        for dir in range(4):
            new_red, new_blue = move(dir, red, blue)
            uu(new_red, new_blue, dir, cnt + 1)
            reset(red, blue, new_red, new_blue)
        return

    if befor_dir % 2 == 0: ## 이전에 상하 움직임
        for dir in [1, 3]:
            new_red, new_blue = move(dir, red, blue)
            uu(new_red, new_blue, dir, cnt + 1)
            reset(red, blue, new_red, new_blue)

    if befor_dir % 2 == 1: ## 이전에 좌우 움직임
        for dir in [0, 2]:
            new_red, new_blue = move(dir, red, blue)
            uu(new_red, new_blue, dir, cnt + 1)
            reset(red, blue, new_red, new_blue)

def move(dir, red, blue):
    rx, ry = red
    bx, by = blue
    if dir == 0:
        if rx < bx:
            nrx, nry = check(rx, ry, dir)
            nbx, nby = check(bx, by, dir)
        else:
            nbx, nby = check(bx, by, dir)
            nrx, nry = check(rx, ry, dir)

    elif dir == 1:
        if ry < by:
            nbx, nby = check(bx, by, dir)
            nrx, nry = check(rx, ry, dir)
        else:
            nrx, nry = check(rx, ry, dir)
            nbx, nby = check(bx, by, dir)

    elif dir == 2:
        if rx < bx:
            nbx, nby = check(bx, by, dir)
            nrx, nry = check(rx, ry, dir)
        else:
            nrx, nry = check(rx, ry, dir)
            nbx, nby = check(bx, by, dir)
    
    elif dir == 3:
        if ry < by:
            nrx, nry = check(rx, ry, dir)
            nbx, nby = check(bx, by, dir)
        else:
            nbx, nby = check(bx, by, dir)
            nrx, nry = check(rx, ry, dir)

    new_red, new_blue = (nrx, nry), (nbx, nby)
    return (new_red, new_blue)

def check(x, y, dir):
    global red_flag
    global blue_flag

    nx, ny = x, y
    for i in range(4):
        if i == dir:
            while 1:
                nx, ny = nx + dx[i], ny + dy[i] 
                if lst[nx][ny] == '.':
                    continue
                if lst[nx][ny] == 'O':
                    if lst[x][y] == "R":
                        red_flag = True
                    else:
                        blue_flag = True
                    lst[x][y], lst[nx][ny] = lst[nx][ny], lst[x][y]
                    return (nx, ny)
                else:
                    lst[x][y], lst[nx - dx[i]][ny - dy[i]] = lst[nx - dx[i]][ny - dy[i]], lst[x][y]
                    return (nx - dx[i], ny - dy[i])

def reset(red, blue, new_red, new_blue):
    global red_flag
    global blue_flag
    red_flag, blue_flag = False, False
    lst[new_red[0]][new_red[1]] = "."
    lst[red[0]][red[1]] = "R"
    lst[new_blue[0]][new_blue[1]] = "."
    lst[blue[0]][blue[1]] = "B"
    lst[goal[0]][goal[1]] = 'O'

n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if lst[x][y] == 'R':
            red = (x, y)
            continue
        if lst[x][y] == 'B':
            blue = (x, y)
            continue
        if lst[x][y] == 'O':
            goal = (x, y)

res = 12
red_flag, blue_flag = False, False
uu(red, blue, -1, 0)
print(res if res != 12 else -1)

