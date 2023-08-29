import sys
input = sys.stdin.readline

## DP + DFS 문제이다
## 현재 위치에 다음 위치의 값을 추가한다

## DP 초기화를 꼭 음수로 해야 하는데
## 이유는 0으로 초기화할 경우
## 다음 위치의 값(도착지점까지의 경우의 수)이 0일 때
## 또 방문하게 된다.
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def is_able(nx, ny,x,y):
    if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] < lst[x][y]:
        return True

def dfs(x, y):
    ## 이 값이 0일 때 또 방문한다.
    ## 가도 도착할 수 없음에도 불구하고.
    ## 즉 도착할 수 없는 경우와 아직 방문하지 않은 경우를 구분하지 못한다.
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if is_able(nx, ny, x, y):
            ## 이 부분! DP 사용이다.
            cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]
dp[-1][-1] = 1
print(dfs(0,0))
