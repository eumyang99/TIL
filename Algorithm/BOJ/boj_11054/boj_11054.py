import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))


# 해당 인덱스 기준으로 좌우에 몇개씩 있는지
left = [0 for _ in range(n)]
right = [0 for _ in range(n)]

# 해당 인덱스 기준으로 가능한 부분수열의 크기
total = [1 for _ in range(n)]

for x in range(n):
    for y in range(x):
        if lst[x] > lst[y]:
            left[x] = max(left[x], left[y]+1)
    total[x] += left[x]

for x in range(n-1, -1, -1):
    for z in range(n-1, x-1, -1):
        if lst[x] > lst[z]:
            right[x] = max(right[x], right[z]+1)
    total[x] += right[x]

print(max(total))


