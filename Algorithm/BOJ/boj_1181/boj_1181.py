import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().rstrip())

print(lst)
lst = list(set(lst))
lst.sort(key=lambda x : len(x))
print(lst)

