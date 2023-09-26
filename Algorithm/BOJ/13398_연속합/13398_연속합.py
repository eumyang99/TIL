import sys
input = sys.stdin.readline

## 이중 DP list가 필요

## DP의 첫번째 행은 숫자를 삭제하지 않은 행
    ## 누적값을 계산해 나간다
    ## 누적값이 0보다 작으면 0을 입력한다
    ## 따라서 항상 0 이상의 값이다
    ## 누적값이 0보다 작으면 그곳을 기점으로 다음 숫자부터 새롭게 더해나간다
    ## EX) 2 3 1 -7 4 5 6  -9
    ##     2 5 6  0 4 9 15  6
    ## 이런 식으로 하면 어디서부터 누적을 시작하면 되는지 알 수 있다.
    ## 위 같은 경우 15가 연속된 합 중 가장 큰 값이다.

## 두번재 행은 숫자를 삭제한 행
    ## 이 경우 두가지를 비교한다
    ## 현재 숫자를 삭제하고 숫자를 삭제하지 않은(첫번째 행) 이전 누적값 - 이번 숫자 삭제된 상황
    ## 숫자를 삭제한(두번째 행) 이전 값에 현재 숫자를 더한 값          - 과거 숫자 삭제된 상황
    ## 두 값 중 큰 값을 입력한다.

n = int(input())
lst = list(map(int, input().split()))

dp = [[0]*n for _ in range(2)]

if lst[0] > 0:
    dp[0][0] = lst[0]
    dp[1][0] = lst[0]

for i in range(1, n):
    ## 첫번째 행
    ## 이전 값과 더했을 때, 음수면 0, 양수면 더한 값을 입력
    dp[0][i] = lst[i] + dp[0][i-1] if lst[i] + dp[0][i-1] > 0 else 0

    ## 두번째 행
    ## 첫번째 행의 이전 값과 : 현재 숫자 삭제한다는 뜻
    ## 두번째 행의 이전 값 + 현재 값 : 과거 숫자 삭제를 받아들인다는 뜻
    ## 두 값 중 큰 값을 입력
    dp[1][i] = max(dp[0][i-1] , dp[1][i-1] + lst[i])

## dp에서 가장 큰 값을 찾아서 출력
## 만약 가장 큰 값이 0이라면 lst에 0 이하의 숫자 밖에 없다는 뜻이니까
## lst에서 가장 큰 값 출력
up_max = max(dp[0])
down_max = max(dp[1])
res = max(up_max, down_max)
if res == 0:
    print(max(lst))
else:
    print(res)