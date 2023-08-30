import sys
input = sys.stdin.readline

## 이상한 문제
## 같은 로직이어도 시간초과 나는게 있고 안나는게 있다.
## 짜증나서 나의 로직과 같지만 되는 코드를 찾아서 가져옴!

dx, dy = (-1,0,1,0), (0,1,0,-1)

def dfs(x, y, cnt):
    global maxi
    maxi = max(maxi, cnt)
    if cnt == 26:
         return 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[lst[nx][ny]]:
                visited[lst[nx][ny]] = 1
                dfs(nx, ny, cnt+1)
                if maxi == 26:
                     return
                visited[lst[nx][ny]] = 0

n, m = map(int, input().split())
lst = [list(map(lambda a : ord(a)-65,input())) for _ in range(n)]

maxi = 1
visited = [0] * 26
visited[lst[0][0]] = 1
dfs(0,0,1)
print(maxi)
