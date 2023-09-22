import sys
input = sys.stdin.readline

## 노션 LIS

def binary_search(LIS, num):
    left, right = 0, len(LIS) - 1
    while left < right:
        mid = (left + right) // 2
        if LIS[mid] > num:
            right = mid
        else:
            left = mid + 1
    return right

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

lst = [arr[i][1] for i in range(n)]


LIS = [lst[0]]
dp = [0] * n
dp[0] = 1

for now_idx in range(1, n):
    if LIS[-1] < lst[now_idx]:
        LIS.append(lst[now_idx])
        dp[now_idx] = len(LIS)
    else:
        dp_idx = binary_search(LIS, lst[now_idx]) 
        LIS[dp_idx] = lst[now_idx]
        dp[now_idx] = dp_idx + 1
    

able_cnt = max(dp)
print(n - able_cnt)
res = []
for i in range(n-1, -1, -1):
    if dp[i] == able_cnt:
        able_cnt -= 1
    else:
        res.append(arr[i][0])

res.sort()
for x in res:
    print(x, end="\n")

