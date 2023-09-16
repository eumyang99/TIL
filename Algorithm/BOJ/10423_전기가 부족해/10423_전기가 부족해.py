import heapq
import sys
input = sys.stdin.readline

## 발상
## 기본적으로 크루스칼로 접근
## 그러나 양쪽 그룹의 부모가 모두 발전기이면 연결하지 않는다.
## 또한 필요한 간선의 개수는 n - k
## 따라서 간선 n - k개를 연결하는 동안 부모가 모두 발전기이면 연결하지 않는다.
## union에서 부모는 무조건 발전기로 지정한다.

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(ps, pe):
    if ps in elec:
        parent[pe] = ps
    else:
        parent[ps] = pe

n, m, k = map(int, input().split())
elec = set(map(int, input().split()))
edges = []
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(edges, (w, s, e))

parent  = [i for i in range(n+1)]
cnt = 0
res = 0
while cnt != n - k:
    w, s, e = heapq.heappop(edges)
    ps, pe = find(s), find(e)
    if ps != pe:
        ## 두 그룹이 연결되어 있지 않지만
        ## 두 그룹 모두 발전기에 연결되어 있다면 연결하지 않는다.
        if ps in elec and pe in elec:
            continue
        res += w
        cnt += 1
        union(ps, pe)
print(res)

