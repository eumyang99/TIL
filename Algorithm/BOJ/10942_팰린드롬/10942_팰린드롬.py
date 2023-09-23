import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)
def uu(left, right):
    if dp[left][right] == 1:
        return True
    if left > right:
        return True
    if arr[left] == arr[right]:
        if uu(left+1, right-1):
            dp[left][right] = 1
            return True
        else:
            return False
    else:
        return False



n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
check = [tuple(map(int, input().split())) for _ in range(m)]

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = 1

for left, right in check:
    if uu(left, right):
        print(1)
    else:
        print(0)

