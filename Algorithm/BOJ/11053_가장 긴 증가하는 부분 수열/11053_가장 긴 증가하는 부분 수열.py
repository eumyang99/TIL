import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = [1]
cnt = 1
for i in range(1, n):
    temp = 0
    for p in range(i-1, -1, -1):
        if lst[i] > lst[p] and res[p] + 1 > temp:
            temp = res[p] + 1
    else:
        if temp == 0:
            res.append(1)
        else:
            res.append(temp)
print(max(res))
