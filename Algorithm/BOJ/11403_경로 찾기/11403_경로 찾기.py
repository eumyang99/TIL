import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dic = defaultdict(list)
lst = [list(map(int, input().split())) for _ in range(n)]
for x in range(n):
    for y in range(n):
        if lst[x][y] == 1:
            dic[x].append(y)

res = [[0]*n for _ in range(n)]
for x in range(n):
    stack = []
    visited = []
    stack.append(x)
    while stack:
        start = stack.pop()
        for end in dic[start]:
            if end not in visited:
                visited.append(end)
                stack.append(end)
                res[x][end] = 1

for row in res:
    print(*row)

