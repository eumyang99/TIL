from collections import deque

import sys
sys.stdin = open('input.txt')


T = int(input())
for case in range(T):
    size = int(input())
    # 1로 감싸서 데이터 받음
    lst = [[1]*(size+2)] + [[1] + list(map(int, input())) + [1] for _ in range(size)] + [[1]*(size+2)]

    # 시작점 sx, sy에 할당
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

    # 큐 생성해서 처음 시작점 넣어둠
    que = deque()
    que.append((sx, sy))

    # visited를 set으로 만들고 시작점 추가
    visited = set()
    visited.add((sx,sy))
    # 거리를 저장할 똑같은 사이즈의 리스트를 생성
    dist_lst = [[0]*(size+2) for i in range(size+2)]
    goal = []

    while que: # 큐 비어버릴 때까지 반복
        p, q = que.popleft() # 큐에 저장된 첫 녀석을 뽑아서
        for i in range(4): # 사방을 탐색해서 3이 있는지 탐색
            nx = p + dx[i]
            ny = q + dy[i]
            if lst[nx][ny] == 3: # 3이 있다면 
                dist_lst[nx][ny] = dist_lst[p][q] + 1 # 거리 리스트에서 +1
                goal.append(nx) # 해당 지점 goal에 append
                goal.append(ny)
                break   # 찾았으면 break
        if lst[nx][ny] == 3: 
            break   # 찾았으면 break

        for i in range(4): # 3을 못 찾았으면
            nx = p + dx[i]
            ny = q + dy[i]
            if (nx, ny) not in visited and lst[nx][ny] == 0: # visited에 없으면서 통로가 0인 경우
                dist_lst[nx][ny] = dist_lst[p][q] + 1   # 거리 +1
                visited.add((nx, ny)) # visited에 추가
                que.append((nx, ny)) # 큐에 append

    if goal: # goal이 있다면
        print(f'#{case+1} {dist_lst[goal[0]][goal[1]]-1}') # 해당 거리 출력
    else: # 찾지 못해서 goal이 없다면 0출력
        print(f'#{case+1} 0')



                




            
        


