import sys
input = sys.stdin.readline

## DP로 푼다.
## 규칙을 찾아 점화식을 생각하고 재귀함수로 구현했다.
## 점화식을 찾는 게 핵심이구나?

def recur(n):
    if dp[n] == 0:
        dp[n] = recur(n-1) + recur(n-2) +recur(n-3)
    return dp[n]

# 테스트 케이스 수 입력
T = int(input())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    print(recur(n))
