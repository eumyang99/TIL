import sys
input = sys.stdin.readline

## 노션 - DP - 동전 에 설명

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

dp = [1] + [0] * (k)
for i in range(1, k+1):
    if i % lst[0] == 0:
        dp[i] = 1

for coin in lst[1:]:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[-1])
