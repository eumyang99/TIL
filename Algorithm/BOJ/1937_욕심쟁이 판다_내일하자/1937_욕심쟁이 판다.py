import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

## 내 코드이다.
## 발상
## 이미 가서 탐색해본 경로라면 다시 탐색할 필요가 없다.
## 탐색을 할 때 현재 위치에서 최대한 멀리갈 수 있는 거리를 2차원 dp에 저장한다.
## 다시 그 지점을 방문할 때 이미 탐색완료한 노드라면 해당 노드에 저장된 것을 가져온다.


dx, dy = (-1,0,1,0), (0,1,0,-1)

def uu(x, y):
    ## 현재 위치의 초기값
    maxi = 0
    ## 사방을 방문하며
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        ## 방문 가능한 곳일 때
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] > lst[x][y]:
            ## 이미 방문했던 곳이라면
            if dp[nx][ny] != 0:
                ## 그곳에서 갈 수 있는 경로와 현재 갈 수 있는 경로 중 더 긴 경로를 maxi에 임시저장한다.
                maxi = max(maxi, dp[nx][ny])
                ## 그리고 그 뒤로 더 방문할 필요가 없으니 다음 방향으로 continue
                continue
            ## 방문하지 않았다면 그 지점으로 들어간다
            ## 그것이 리턴하는 값을 저장하고
            ## 다른 방향에서 탐색한 가능한 거리와 비교하여 다시 maxi에 최대값을 저장한다.
            temp = uu(nx, ny)
            maxi = max(maxi, temp)
    
    ## 사방 탐색이 끝났다면 현재 노드에서 갈 수 있는 거리는 maxi + 1이다
    ## maxi는 현재 노드에서 갈 수 있는 다음 녀석이 갈 수 있는 거리이기 때문
    ## 그 값을 현재 위치 dp에 저장하고
    ## 그 값을 리턴한다.
    ## 리턴 받은 녀석은 그 위치의 maxi를 갱신할 것이다.
    dp[x][y] = maxi+1
    return dp[x][y]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
for p in range(n):
    for q in range(n):
        if not dp[p][q]:
            uu(p, q)

res = 0
for row in dp:
    res = max(res, max(row))
print(res)



## 같은 로직의 다른 사람 코드이다.
## 시간은 내 코드보다 오래 걸리지만 보다 깔끔한 코드이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx, dy = (-1,0,1,0), (0,1,0,-1)

def uu(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] > lst[x][y]:
            dp[x][y] = max(dp[x][y], uu(nx, ny) + 1)

    return dp[x][y]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
res = 0
for p in range(n):
    for q in range(n):
        if not dp[p][q]:
            res = max(res, uu(p, q))
print(res)