import heapq
import sys
input = sys.stdin.readline

## 크루스칼로 풀어봤다

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(ps, pe):
    parent[pe] = ps


n = int(input())
x, y, z = [], [], [] 

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort
y.sort
z.sort

pq = []
for i in range(n-1):
    heapq.heappush(pq, (abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    heapq.heappush(pq, (abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    heapq.heappush(pq, (abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))


parent = [i for i in range(n)]
print(pq)
res = 0
cnt = 0
for i in range(n*3):
    w, s, e = heapq.heappop(pq)
    print(w, s, e)
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        if cnt == n-1:
            break
print(res)