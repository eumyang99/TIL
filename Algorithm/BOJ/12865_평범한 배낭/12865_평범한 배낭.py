import sys
input = sys.stdin.readline

## 노션에 DP - Knapsack 설명에 있음 

n, k = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = lst[i-1][0], lst[i-1][1]
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[-1][-1])

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# lst = [tuple(map(int, input().split())) for _ in range(n)]

# dp = [0]*(k+1)
# for item in lst:
#     w, v = item
#     for i in range(k, w-1, -1):
#         dp[i] = max(dp[i], dp[i-w]+v)

# print(dp[-1])