from collections import deque
import sys
sys.stdin = open('input_5_4.txt')

n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]


# BFS
target_x = n-1                  # 목표 x값
target_y = m-1                  # 목표 y값
visited = set()                 # visited 생성
visited.add((0, 0))             # 시작값 추가
que = deque()                   # queue 생성
que.append((0,0))               # 시작값 추가                 

# 델타
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

goal = False                    # 목표지점에 도착하면 True로 변환 예정

cnt_lst = []                    # cnt를 카운트할 리스트
for i in range(n):              # 좀더 깊은 복사(??? 되나??)를 위해서 
    cnt_lst.append(lst[i][:])

cnt_lst[0][0] = 1               # 시작값은 미리 카운트 +1


while 1:
    x, y = que.popleft()        # 큐를 팝해서
    for i in range(4):          # 델타 탐색 후
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == target_x and ny == target_y:       # 목표값에 도달했으면
            cnt_lst[nx][ny] = cnt_lst[x][y] + 1     # 카운트 +1
            goal = True                             # goal은 True로 하고 종료
            break
        if 0 <= nx <= target_x and 0 <= ny <= target_y:         # 리스트 범위 내에서 
            if lst[nx][ny] == 1 and (nx, ny) not in visited:    # 길이 있으면서 visited에 없으면
                cnt_lst[nx][ny] = cnt_lst[x][y] + 1             # 카운트 리스트에 +1
                visited.add((nx, ny))                           # visited에 추가
                que.append((nx, ny))                            # que에 append
    if goal == True:                # while문 종료를 위해서
        break                       # goal에 True면 종료

print(cnt_lst[target_x][target_y])




