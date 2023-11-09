from collections import deque
import sys
input = sys.stdin.readline

## 발상
## (사용 가능한 거울과 빛의 방향)을 que에 담아 BFS로 탐색

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

## 특정 좌표에서 특정 방향에 있는 정보 탐색
def uu(x, y, dir):
    nx, ny = x + dx[dir], y + dy[dir]
    next_mirror = []
    while 0 <= nx < n and 0 <= ny < n:
        ## 벽이면 그만
        if arr[nx][ny] == "*":
            break
        ## 거울이면 next_mirror에 append
        elif arr[nx][ny] == "!":
            next_mirror.append((nx, ny))
        ## 도착문이면 문의 좌표 반환
        elif arr[nx][ny] == "#":
            if (nx, ny) == door[1]:
                return [(nx, ny)]
            
        nx += dx[dir]
        ny += dy[dir]

    ## 다음 거울들의 좌표 반환
    return next_mirror

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

## 문 위치 찾기
door = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == "#":
            door.append((x, y))

used = set()
## cnt, 방향, 위치
## 첫 번째 발견한 문을 시작문으로
## 모든 방향을 탐색하기 위해 que에 담음
que = deque([(0, door[0][0], door[0][1], dir) for dir in range(4)])
while que:
    cnt, x, y, dir = que.popleft()
    ## 해당 방향으로 탐색 후 mirror에 다음 거울 후보 저장
    mirror = uu(x, y, dir)
    ## 거울 후보가 있을 때
    if mirror:
        ## 만약 도착문에 도착했다면 cnt출력 후 탈출
        if mirror[0] == door[1]:
            print(cnt)
            break 

        ## 그게 아니라면
        else:
            ## 모든 거울 후보에 대해 현재 진입 방향에 따라 다음 탐색 방향 설정
            ## 각 거울에 대해 새로운 탐색 방향으로 이미 탐색을 한 경우라면 que에 담지 않음
            for nx, ny in mirror:
                if dir % 2:
                    ## 해당 거울에 해당 방향을 탐색한 적이 없다면
                    if (nx, ny, 0) not in used:
                        ## que에 넣고
                        que.append((cnt+1, nx, ny, 0))
                        ## 사용처리 함
                        used.add((nx, ny, 0))
                    if (nx, ny, 2) not in used:
                        que.append((cnt+1, nx, ny, 2))
                        used.add((nx, ny, 2))
                else:
                    if (nx, ny, 1) not in used:
                        que.append((cnt+1, nx, ny, 1))
                        used.add((nx, ny, 1))
                    if (nx, ny, 3) not in used:
                        que.append((cnt+1, nx, ny, 3))
                        used.add((nx, ny, 3))

