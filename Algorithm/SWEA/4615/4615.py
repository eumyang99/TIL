import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(m)]
    pan = [[0]*(n+2) for _ in range(n+2)]
    pan[n//2][n//2] = 2
    pan[n//2][n//2+1] = 1
    pan[n//2+1][n//2+1] = 2
    pan[n//2+1][n//2] = 1
    

    # 12시부터 시계방향으로 11시까지 델타 탐색
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    w = 2
    b = 2
    for put in lst:
        x = put[0]
        y = put[1]
        color = put[2]
        if color == 1:            # 흑이면
            pan[x][y] = 1
            b += 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                temp = []
                while pan[nx][ny] == 2:
                    temp.append([nx, ny])
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                else:
                    if pan[nx][ny] == 0:
                        temp = []

                for change in temp:
                    pan[change[0]][change[1]] = 1
                    b += 1
                    w -= 1


        else:                       # 백이면
            pan[x][y] = 2
            w += 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                temp = []
                while pan[nx][ny] == 1:
                    temp.append([nx, ny])
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                else:
                    if pan[nx][ny] == 0:
                        temp = []            
                for change in temp:
                    pan[change[0]][change[1]] = 2
                    w += 1
                    b -= 1

    print(f'#{case+1} {b} {w}')
