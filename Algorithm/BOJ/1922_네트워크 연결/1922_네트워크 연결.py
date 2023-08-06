import sys
input = sys.stdin.readline

## 크루스칼 알고리즘의 정석

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(px, py):
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

n = int(input())
m = int(input())
lst = [tuple(map(int, input().split())) for _ in range(m)]

lst.sort(key= lambda x: x[2])
parent = [i for i in range(n+1)]

cnt = 0
res = 0

for s, e, w in lst:
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        if cnt == n-1:
            break

print(res)


