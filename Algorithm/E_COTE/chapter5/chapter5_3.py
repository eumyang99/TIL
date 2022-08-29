from collections import deque

n, m = map(int, input().split())
lst = [[1]*(m+2)] + [[1] + list(map(int, input())) + [1] for _ in range(n)] + [[1]*(m+2)]
print(lst)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


