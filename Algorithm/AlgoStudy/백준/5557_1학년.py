import sys
input = sys.stdin.readline

## 크게 배웠다.
## DP문제인데
## 처음에는 배낭문제처럼 넣는다 안넣는다를 가지고 풀려고 했다.
## 그런데 이 문제는 최대값이나 최소값으로 값을 갱신해 나가는 것이 아니기 때문에 불가능했다.
## 원재의 풀이를 들어보니 새로운 접근법이었다.
## DP를 2차원 배열로 초기화한다.
## 첫번째 인덱스는 나열된 숫자의 인덱스, 두번째 인덱스는 더하거나 뺀 결과 값이다.
## 해당 숫자를 더하거나 뺏을 때 나오는 경우의 수를 기록한다.

## 아래와 같다
##   4 4 4 4 8 일 경우
## 0   1   2
## 1
## 2
## 3
## 4 1   2
## 5   
## 6
## 7
## 8   1   2 <-출력값
## 9
## 10
## ...

## 배운 점
## 나올 수 있는 결과값들을 하나의 축으로 사용할 수 있다는 것을 배웠다.
## 물론 나올 수 있는 결과값이 한정적일 때!!


n = int(input())
lst = list(map(int, input().split()))
dp = [[0]*21 for _ in range(n)]

dp[0][lst[0]] = 1

for num_idx in range(n-2):
    for result in range(21):
        if dp[num_idx][result]:
            p_val = result + lst[num_idx+1] 
            m_val = result - lst[num_idx+1]
            if p_val <= 20:
                dp[num_idx+1][p_val] += dp[num_idx][result] 
            if m_val >= 0:
                dp[num_idx+1][m_val] += dp[num_idx][result] 

print(dp[n-2][lst[-1]])