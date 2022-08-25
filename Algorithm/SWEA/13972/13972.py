from collections import deque

import sys
sys.stdin = open('input.txt')



        

T = int(input())
for case in range(T):
    size = int(input())
    lst = [[1]*(size+2)] + [[1] + list(map(int, input())) + [1] for _ in range(size)] + [[1]*(size+2)]

    sx, sy = 0, 0
    for x in range(size+1, -1, -1):
        for y in range(size+1, -1, -1):
            if lst[x][y] == 2:
                sx = x
                sy = y
                break
            if sx != 0:
                break
        if sx != 0:
            break

                

    # 상 좌 우 하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]


    que = deque()
    visited = set()
    visited.add((sx,sy))
    dist_lst = [[0]*(size+2) for i in range(size+2)]
    gs = 0
    gy = 0

    def exp(start_x, start_y):
        global gs
        global gy

        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if lst[nx][ny] == 3:
                gs = nx
                gy = ny
                dist_lst[nx][ny] = dist_lst[start_x][start_y] + 1
                return True

        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if lst[nx][ny] == 0 and (nx, ny) not in visited:
                que.append((nx, ny))
                visited.add((nx, ny))
                dist_lst[nx][ny] = dist_lst[start_x][start_y] + 1

        if que:
            p, q = que.popleft()
            if exp(p, q) == True:
                return True


    if exp(sx, sy) == True:
        print(f'#{case+1} {dist_lst[gs][gy]-1}')
    else:
        print(f'#{case+1} 0')

                




            
        


