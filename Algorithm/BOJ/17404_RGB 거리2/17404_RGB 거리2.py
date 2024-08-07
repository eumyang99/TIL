import sys
input = sys.stdin.readline

## 발상 참고함
## 현재 집에서 칠하는 색깔은 이전 집에서 칠한 다른 두 색깔의 비용과 더해진다.
## 따라서 현재 집에서 빨간색을 칠한다면
## 이전 집에서 칠한 파란색 비용과 녹색 비용 중 작은 값과 더해진다.
## 그 더해진 값을 현재 빨간색 비용으로 저장한다.
## 파란색, 녹색도 마찬가지로 저장한다.

## 그런데 이 문제는 첫 집과 마지막 집의 색이 달라야 하기 때문에
## 첫집일 빨간색, 파란색, 녹색일 때 3번을 확인해봐야 한다.
## 따라서 첫집이 빨간색일 경우
## (첫집 빨간색 비용, inf, inf)로 하면
## 두번째 집에서 파란색을 칠할 때 녹색은 inf이기 때문에 무조건 빨간색 집을 선택하게 된다.
## 두번째 집에서 빨간색을 칠하는 비용은 파란색, 녹색 즉 inf와 더해지기 때문에 의미가 없어진다.
## 다음 집으로 넘어갈 수록 inf는 점점 사라진다.

## 그리렇게 나온 마지막 집의 빨간색, 파란색, 녹색 비용 중 작은 것을 택하면 되는데
## 다만 첫 집의 색과 다른 나머지 두 집의 비용만 확인하면 된다.

n = int(input())
lst = list(tuple(map(int, input().split())) for _ in range(n))

res = 1000001
for p in range(3):
    dp = [[1001, 1001, 1001]]
    dp[0][p] = lst[0][p]
    for i in range(1, n):
        a = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
        b = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
        c = lst[i][2] + min(dp[i-1][0], dp[i-1][1])
        dp.append((a, b, c))

    for able in range(3):
        if able != p:
            res = min(res, dp[-1][able])


print(res)