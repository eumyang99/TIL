import sys
input = sys.stdin.readline

## https://wooono.tistory.com/605

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

for x in range(1, m):
    dp[0][x] += dp[0][x-1]

for x in range(1, n):
    left_direction = dp[x][:]
    right_direction = dp[x][:]

    left_direction[0] += dp[x-1][0]
    right_direction[-1] += dp[x-1][-1]
    
    for y in range(1, m):
        left_direction[y] += max(dp[x-1][y], left_direction[y-1])
    
    for y in range(m-2, -1, -1):
        right_direction[y] += max(dp[x-1][y], right_direction[y+1])


    for y in range(m):
        dp[x][y] = max(left_direction[y], right_direction[y])

print(dp[-1][-1])
