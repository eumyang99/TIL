import sys
input = sys.stdin.readline


n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()
res = 0

# 앞에거 두개 합치고 맨 첫번째꺼 pop하고 sort 반복

while len(lst) != 1:
    res += lst[0] + lst[1]
    lst[1] = lst[0] + lst[1]
    lst.pop(0)
    lst.sort()

print(res)