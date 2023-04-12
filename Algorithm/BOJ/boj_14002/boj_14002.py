import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
memo = [1 for _ in range(n)]


for x in range(n):
    for y in range(x):
        if lst[x] > lst[y]:
            memo[x] = max(memo[x], memo[y]+1)

size = max(memo)

print(size)
res = []

for i in range(n-1, -1, -1):
    if memo[i] == size & size:
        res.append(lst[i])
        size -= 1

for i in range(max(memo)-1,-1,-1):
    print(res[i],end=" ")