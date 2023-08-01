import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        p = find(parent[x])
        parent[x] = p
        return p
    return x

def union(x, y):
    px = find(x)
    py = find(y)
    if px < py:
        parent[y] = px
    else:
        parent[x] = py

n, m = map(int, input().split())
lst = [0] + [list(map(int, input().split())) for _ in range(n)]
already = [list(map(int, input().split())) for _ in range(m)]


parent = [i for i in range(n+1)]
distance = []
for x in range(1, n):
    for y in range(x+1, n+1):
        dist = ((lst[x][0] - lst[y][0])**2 + (lst[x][1] - lst[y][1])**2)**(1/2)
        distance.append([x,y,dist])

distance.sort(key = lambda x: x[2])

for edge in already:
    union(edge[0], edge[1])

res = 0
cnt = n - 1 - m
for edge in distance:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        res += edge[2]
        cnt -= 1

print(round(res, 2))
print(f'{res:.2f}')
