from collections import deque
import sys
input = sys.stdin.readline

## 단순한 BFS 탐색 문제이다.
## 조건을 걸어서 BFS를 두번 돌리면 된다.

## RGB에 따라 BFS que에 담는 조건이 필요하다.
## 예를 들어 R일 때 사방향 탐색한 곳이 R or G 이면 que에 담는다고 할 때,
## R = {R, G} 라는 집합(set)를 활용하여
## lst[nx][ny] in R 이라는 코드로 사용할 수 있다. 

dx, dy = (-1,0,1,0), (0,1,0,-1)

def bfs(is_obstacle):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = 1
                color = lst[x][y]
                que = deque()
                que.append((x, y))
                if is_obstacle:
                    if color == "B":
                        while que:
                            px, py = que.popleft()
                            for i in range(4):
                                nx, ny = px + dx[i], py + dy[i]
                                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lst[nx][ny] == color:
                                    visited[nx][ny] = 1
                                    que.append((nx, ny))
                        else:
                            cnt += 1
                    else:
                        while que:
                            px, py = que.popleft()
                            for i in range(4):
                                nx, ny = px + dx[i], py + dy[i]
                                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (lst[nx][ny] == "R" or lst[nx][ny] == "G"):
                                    visited[nx][ny] = 1
                                    que.append((nx, ny))
                        else:
                            cnt += 1

                else:
                    while que:
                        px, py = que.popleft()
                        for i in range(4):
                            nx, ny = px + dx[i], py + dy[i]
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lst[nx][ny] == color:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
                    else:
                        cnt += 1

    return print(cnt)

n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]

bfs(False)
bfs(True)
