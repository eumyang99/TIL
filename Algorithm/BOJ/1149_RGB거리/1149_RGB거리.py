import sys
input = sys.stdin.readline

## DP문제이다.
## 발상
## 현재 집에서 빨간색을 칠하는 경우, 녹색을 칠하는 경우, 파란색을 칠하는 경우 누적된 비용을 모두를 기록해 나간다.
## 빨간색을 칠하는 경우, 이전 집에서 파란색, 녹색을 칠한 누적값에 현재 빨간색을 칠하는 값을 더한 값을 기록
## 녹색을 칠하는 경우, 이전 집에서 빨간색, 파란색을 칠한 누적값에 현재 녹색을 칠하는 값을 더한 값을 기록
## 파란색을 칠하는 경우, 이전 집에서 빨간색, 녹색을 칠한 누적값에 현재 빨간색을 칠하는 값을 더한 값을 기록
## 마지막 집에서 빨, 녹, 파 중 가장 적은 비용을 출력한다.
## 헷갈릴 경우 for문 안에 DP를 찍어보자

n = int(input())
lst = list(tuple(map(int, input().split())) for _ in range(n))

dp = [lst[0]]
for i in range(1, n):
    a = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
    b = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
    c = lst[i][2] + min(dp[i-1][0], dp[i-1][1])
    dp.append((a, b, c))
    print(dp)
print(min(dp[-1]))