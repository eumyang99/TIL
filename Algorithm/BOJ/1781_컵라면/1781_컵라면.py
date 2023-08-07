import heapq
import sys
input = sys.stdin.readline

n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort()

res = 0
pq = []

first_day = lst[-1][0]
idx = n-1
for today in range(first_day, 0, -1):
    while idx > -1 and lst[idx][0] == today:
        heapq.heappush(pq, lst[idx][1]*-1)
        idx -= 1
    if pq:
        res -= heapq.heappop(pq)

print(res)