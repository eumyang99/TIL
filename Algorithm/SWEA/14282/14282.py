from collections import deque
import sys
sys.stdin = open('input.txt')

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    visited = [[9999999999]*n for _ in range(n)]                # 최소 누적값 기록
    visited[0][0] = 0                                           # 첫출발은 누적값 0

    start = (0, 0, lst[0][0])                                   # 시작지점의 x, y좌표, 높이
    q = deque()
    q.append(start)                                             # 큐에 시작지점 넣기

    while q:
        x, y, h = q.popleft()                                   # x, y, 높이 추출
        for i in range(4):                                      # 델타 탐색하며
            over = 1                                            # 기본 에너지 소모 +1
            nx = x + dx[i]                                                  
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:                     # 델타 탐색이 범위 안에 있으면
                if h < lst[nx][ny]:                             # 높이 체크해서 차이 만큼 over에 추가
                    over += lst[nx][ny] - h
                # 델타 탐색한 지점이 이미 방문되어 있다면
                # 현재 지점에서 그곳으로 이동할 때의 누적값이 더 작다면
                # 갱신하고 큐에 추가
                if visited[x][y] + over < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + over
                    q.append((nx, ny, lst[nx][ny]))

    print(f'#{case+1} {visited[-1][-1]}')
            

