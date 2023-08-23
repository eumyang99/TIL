import sys
input = sys.stdin.readline
n = int(input())
dp = [1,1,1,1,1,1,1,1,1,1]
for i in range(1, n):
    for x in range(1, 10):
        dp[x] += dp[x-1]
print(sum(dp)%10007)
