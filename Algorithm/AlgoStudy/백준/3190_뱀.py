from collections import deque
import sys
input = sys.stdin.readline

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
def uu(apples_set, change_dir_arr):
    ## 시간 초기화
    time = 0

    ## 방향 초기화
    ## 0, 1, 2, 3  =>  우, 하, 좌, 상
    direction = 0 

    ## 현재 위치 초기화
    cur_x, cur_y = 1, 1

    ## 방문 처리 초기화
    ## index가 작을 수록 꼬리에 가까움
    visited = deque([(1, 1)])

    for sec, dir in change_dir_arr:
        ## 현재 시간이 sec 보다 작을 때,
        ## sec == -1 일 때, 마지막으로 바꾼 방향으로 계속 진행
        while (time < sec) or (sec == -1):
            
            ## 방향에 따라 다음 좌표 설정
            for i in range(4):
                if i == direction:
                    nx, ny = cur_x + dx[i], cur_y + dy[i]

            ## 게임이 끝나지 않는 조건일 때,
            if 0 < nx <= n and 0 < ny <= n and (nx, ny) not in visited:
                ## 다음 자리 방문 처리
                visited.append((nx, ny))
                ## 만약 다음 자리에 사과가 있었다면
                if (nx, ny) in apples_set:
                    ## 사과 좌표를 제거하고 꼬리 삭제 안함
                    apples_set.discard((nx, ny))
                ## 만약 사과가 없었다면
                else:
                    ## 꼬리 제거
                    visited.popleft()
                
                ## 현재 위치 갱신
                cur_x, cur_y = nx, ny
                ## 시간 추가
                time += 1
            
            ## 게임이 끝났다면
            else:
                ## 시간 추가하고 return
                return time+1

        ## 해당 방향으로 다 진행을 했다면
        else:
            ## 다음 방향 설정
            if dir == "D":
                direction = (direction + 1) % 4
            elif dir == "L":
                direction = (direction - 1) % 4


n = int(input())
apple_cnt = int(input())
## 사과 좌표는 set으로 받음
apples_set = {tuple(map(int, input().split())) for _ in range(apple_cnt)}
change_dir_cnt = int(input())
## 방향 정보를 받을 때, 임의의 마지막 값을 하나로 추가
change_dir_arr = []
for _ in range(change_dir_cnt):
    sec, dir = input().split()
    change_dir_arr.append((int(sec), dir))
else:
    ## 임의의 값 추가
    change_dir_arr.append((-1, -1))

print(uu(apples_set, change_dir_arr))
