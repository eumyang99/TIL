import sys
input = sys.stdin.readline

## DP문제이다.
## 어떤 반복되는 과정이 얽혀있다는 것은 알겠으나 그것을 수식화하는 것이 어렵다.
## 이걸 찾아 내는 것이 핵심인가 보다.

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.reverse()
dp = [[lst[0], lst[0]]]
for _ in range(n-1):
    dp.append([0, 0])
if n < 3 :
    print(sum(lst))
elif n < 4:
    print(sum(lst)-min(lst[1:]))
else:
    for i in range(n-2):
        if dp[i][0]:
            dp[i+2][1] = dp[i][0] + lst[i+2]
        if dp[i][1]:
            dp[i+1][0] = dp[i][1] + lst[i+1]
            dp[i+2][1] = max(dp[i+2][1], dp[i][1] + lst[i+2])
    else:
        dp[-1][0] = dp[-2][1] + lst[-1]
    print(dp)

    print(max(max(dp[-1]), max(dp[-2])))
