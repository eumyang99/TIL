import sys
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def uu(x, y):
    global res

    for i in range(4):
        ## 사이클이면 종료
        if dp[0][0] == -2:
            return

        ## nx, ny 설정
        nx, ny = x + dx[i]*arr[x][y], y + dy[i]*arr[x][y]

        ## 배열 내에 있을 때
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0:
            ## 방문한 곳이면 사이클 처리하고 리턴
            if visited[nx][ny]:
                dp[0][0] = -2
                return 
            
            ## dp에 기록된 곳이면 dp기록을 사용하고 더 순회하지 않음
            if dp[nx][ny] != 0:
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
                continue
            
            ## 백트래킹 dfs
            visited[nx][ny] = 1
            uu(nx, ny)
            visited[nx][ny] = 0

            ## 사이클이 형성 안되었으면
            if dp[0][0] != -2:
                ## 기존 dp와 바로 뒤에 방문한 녀석의 dp값 + 1 중 큰 값을 할당
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

            ## 사이클 형성이면 리턴
            else:
                return

        ## 배열 밖에 있을 때
        else:
            ## 사이클 형성 아니라면
            if dp[0][0] != -2:
                ## dp값에 0이나 기존 dp값을 할당
                dp[x][y] = max(dp[x][y], 0)

            


n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(input().rstrip())
    for i in range(m):
        if temp[i] == "H":
            temp[i] = 0
        else:
            temp[i] = int(temp[i])
    arr.append(temp[:])

res = 0
visited = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
visited[0][0] = 1
uu(0, 0)

print(dp[0][0] + 1)
