# 투포인터 활용
# l, r = 0, 0
# arr[r] - arr[i] 가 타겟보다 작으면 r 증가
# arr[r] - arr[i] 가 타겟보다 크면 l 증가, res와 비교해서 갱신
# 같으면 타겟 출력


import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

res = INF
left, right = 0, 0
while right < n:
    gap = arr[right] - arr[left]
    if gap == m:
        res = m
        break

    if gap < m:
        right += 1
        continue

    if gap > m:
        res = min(res, gap)
        left += 1
        continue

print(res)
