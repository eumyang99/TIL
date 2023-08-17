import sys
input = sys.stdin.readline

def uu(n):
    if n not in dp:
        dp[n] = uu(n-1) + uu(n-2)
    return dp[n]

n = int(input())
dp = {1:1, 2:2}
print(uu(n) % 10007)