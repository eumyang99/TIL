import sys
sys.stdin = open('input.txt')


def exp(x, y):
    lst[x][y] = 5 # 왔던 곳
    for i in range(4): # 상하좌우에 3이 있으면 return
        if lst[x + dx[i]][y + dy[i]] == 3:
            return 1
    for i in range(4): # 상하좌우에 0이 있으면
        if lst[x + dx[i]][y + dy[i]] == 0:
            if exp(x + dx[i], y + dy[i]) == 1: # 그리고 0이 있는 곳에서 return 1을 받으면
                return 1    # 여기서도 return 1
                            # 한 뎁스 바깥의 함수도 return 해야 함
                            # 그래야 차례차례 함수가 종료됨
                            # 안그러면 바깥 함수에서는 none이 반환되어 결국 3을 찾아도 none으로 끝남


T = int(input())
for case in range(T):
    size = int(input())
    # 바깥 테두리에 더미 1을 쌓음
    lst = [[1]*(size+2)] + [[1] + list(map(int, input())) + [1] for _ in range(size)] + [[1]*(size+2)]

    for i in range(1, size+1):
        for j in range(1, size+1):
            if lst[i][j] == 2:
                x = i       # 시작점 x좌표
                y = j       # 시작점 y좌표

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if exp(x, y) == 1:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')

