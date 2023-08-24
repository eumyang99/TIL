import sys
input = sys.stdin.readline

## 발상
## i번째 숫자가 들어왔을 때 기존에 작성된 dp를 전부 확인하며
## i번째 숫자보다 작으면서 dp값이 가장 큰 값(maxi)을 저장하고
## dp[i]에 maxi + ㅑ번째 숫자 를 기록한다.
## max(dp)를 출력한다.

n = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]] + [0]*(n-1)
for i in range(1, n):
    left = i-1
    maxi = 0
    while left >= 0:
        if lst[i] > lst[left] and maxi < dp[left]:
            maxi = dp[left]
        left -= 1
    else:
        dp[i] = maxi + lst[i]

print(max(dp))

