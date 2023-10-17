from collections import deque
import sys
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def uu(n, m, arr, key): # (int, int, list, set)
    ## 출력값
    res = 0

    ## 방문 처리
    visited = [[0] * m for _ in range(n)]

    ## 열지 못한 문의 좌표(idx : 알파벳)
    closed_door = [[] for _ in range(26)]

    ## 출입구 찾기
    entrance = []
    ## arr 전체를 순회하면서 
    for x in range(n):
        for y in range(m):
            ## arr의 테두리만 탐색
            if (x != 0 and x != n-1) and (y != 0 and y != m-1):
                continue
            ## 벽이 아니면서
            if arr[x][y] != '*':
                ## 빈 공간일 때
                ## 방문처리, 입구 추가
                if arr[x][y] == '.':
                    visited[x][y] = 1
                    entrance.append((x, y))
                ## 서류일 때
                ## res 추가, 방문처리, 입구 추가
                elif arr[x][y] == '$':
                    res += 1
                    visited[x][y] = 1
                    entrance.append((x,y))
                ## 소문자일 때
                ## 열쇠 추가, 방문처리, 입구 추가
                elif 97 <= ord(arr[x][y]) <= 122:
                    key.add(arr[x][y])
                    visited[x][y] = 1
                    entrance.append((x,y))
                ## 대문자일 때
                else:
                    ## 열쇠가 있으면
                    ## 방문처리, 입구 추가
                    if arr[x][y].lower() in key:
                        visited[x][y] = 1
                        entrance.append((x, y))
                    ## 열쇠가 없으면
                    ## closed_door 추가
                    else:
                        closed_door[ord(arr[x][y]) - 65].append((x, y))

    ## 초기 탐색
    ## 1. 열지 못하는 문을 만나는 좌표 저장
    ## 2. 초기 열쇠 수집
    que = deque(entrance)
    while que:
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    ## '*' 이면 방문처리만
                    if arr[nx][ny] == '*':
                        visited[nx][ny] = 1
                        continue
                    ## '$' 이면 res 추가
                    if arr[nx][ny] == '$':
                        que.append((nx, ny))
                        visited[nx][ny] = 1
                        res += 1
                    ## '.' 이면 que 추가
                    elif arr[nx][ny] == '.':
                        que.append((nx, ny))
                        visited[nx][ny] = 1
                    ## 알파벳이면
                    else:
                        ## 대문자일 때
                        if arr[nx][ny].isupper():
                            ## 열리는 문이면 que 추가
                            if arr[nx][ny].lower() in key:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
                            ## 못여는 문이면 closed_door에 추가
                            else:
                                closed_door[ord(arr[nx][ny]) - 65].append((nx, ny))
                        ## 소문자일 때, 열쇠에 추가
                        else:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
                            key.add(arr[nx][ny])
        else:
            ## 모든 알파벳을 돌며
            for i in range(26):
                ## 특정 문에 대한 열쇠를 가지고 있으면서
                ## 그 문을 열지 못한 곳이 있으면
                if chr(i + 97) in key and closed_door[i]:
                    ## 그 문들의 좌표를 큐에 담고
                    que = deque(closed_door[i])
                    ## 그 문들을 bfs할 것이기 때문에
                    ## 빈 배열로 초기화하고
                    closed_door[i] = []
                    ## 미리 방문처리 해놓는다
                    for x, y in closed_door[i]:
                        visited[x][y] = 1
                    ## 반복문 탈출!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    ## 이 부분에 break를 안달아서 2시간 버림...
                    break

    return print(res)
    
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    key = set(input().rstrip())
    uu(n, m, arr, key)



