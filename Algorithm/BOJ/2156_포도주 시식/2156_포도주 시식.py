import sys
input = sys.stdin.readline

## 착오 1.
## 인덱스를 가지고 놀 때는 꼭 n이 1,2,3 일 때를 가정해보자

## 착오 2.
## 당연히 건너뛰는 칸의 최대가 한 칸이라고 생각했으나
## 100 100 1 1 100 100 일 경우 301이 나온다. (정답은 400)

n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
if n < 3:
    print(sum(lst))
else:
    dp = [0, lst[1], lst[1]+lst[2], max(lst[1]+lst[2], lst[3]+lst[2], lst[3]+lst[1])]
    for i in range(4, n+1):
        dp.append(max(lst[i-1]+dp[i-3], lst[i-1]+dp[i-4], dp[i-2]) + lst[i])
    print(max(dp))