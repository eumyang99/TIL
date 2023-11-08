import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
memo = [0] * (n+1)
arr = [0] + [int(input()) for _ in range(n)]
accu_arr = [0] + [arr[1]]
for i in range(2, n+1):
    accu_arr.append(accu_arr[-1] + arr[i])

for i in range(m+k):
    norm, x, y = map(int, input().split())
    if norm == 1:
        memo[x] = y - (memo[x] + arr[x])
    else:
        print(accu_arr[y] - accu_arr[x-1] + sum(memo[x:y]))
