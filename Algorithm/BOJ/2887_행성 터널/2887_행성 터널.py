import heapq
import sys
input = sys.stdin.readline

## 크루스칼로 풀어봤다
## 너무 어렵다....................
## 이중 for문으로 모든 간선을 들고 시작하면 벌써 틀린다.
## 사용할 간선들만 추려서 해야 한다.
## 사용할 간선을 추리는 아이디어가 핵심이다.

## x좌표를 기준으로 정렬, y좌표를 기준으로 정렬, z좌표를 기준으로 정렬한다.
## a노드의 x가 1이고 b노드의 x가 3이고 c노드의 x가 6이면 우리는 a와 c노드의 거리를 기억할 필요가 없다.(핵심)
## a와 b노드의 거리만 기억하면 된다.
## 따라서 x, y, z로 정렬된 간선 정보 리스트는 바로 인접한 (i일 경우 i-1과 i+1) 노드만 거리를 재서 heap에 담는다.
## 그러면 x, y, z 리스트에서 각각 n-1개의 간선 정보만 추릴 수 있고 heap에는 3(n-1)개만 저장된다.
## 여기서 크루스칼을 돌린다.



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

x.sort()
y.sort()
z.sort()

pq = []
for i in range(n-1):
    heapq.heappush(pq, (abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    heapq.heappush(pq, (abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    heapq.heappush(pq, (abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))


parent = [i for i in range(n)]
res = 0
cnt = 0
for i in range(n*3):
    w, s, e = heapq.heappop(pq)
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        if cnt == n-1:
            break
print(res)