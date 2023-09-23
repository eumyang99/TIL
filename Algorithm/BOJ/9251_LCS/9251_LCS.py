import sys
input = sys.stdin.readline

## 발상 : LCS(최장 공통 부분 수열)의 기본 알고리즘을 스스로 떠올렸음!
## LCS 방법
## https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

## 사용하는 DP 2차원 배열의 의미
## a_word = ACAYKP
## b_word = CAPCAK
## 두 문자를 예시로,
## DP[5][3]의 의미는 "ACAYK"(p) 와 "CAP"(CAK) 문자열의 LCS를 나타낸다.

a_word = "0" + input().rstrip()
b_word = "0" + input().rstrip()

len_a, len_b = len(a_word), len(b_word)
## dp배열을 2차원으로 만들고
## (단, 이런 dp문제는 한 행을 그릴 때, 바로 앞의 행만 참고하면 되기 때문에 1차원 배열로 하는 것이 효율적이다)
memo = [[0]*(len_b) for _ in range(len_a)]

for x in range(1, len_a):
    max_v = 0
    for y in range(1, len_b):
        ## 문자열 하나씩 비교하면서
        ## 두 문자가 다르다면
        if a_word[x] != b_word[y]:
            ## 바로 윗 행의 숫자와 앞의 숫자 중 큰 것을 넣는다
            memo[x][y] = max(memo[x][y-1], memo[x - 1][y])
        ## 두 문자가 같다면
        else:
            ## 바로 앞 행의 바로 앞 열(왼쪽 대각선)의 숫자 + 1을 넣는다.
            memo[x][y] = memo[x - 1][y - 1] + 1

## 배열의 마지막 값을 출력한다
print(memo[-1][-1])