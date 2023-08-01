import sys
input = sys.stdin.readline


## 발상
## 이 문제는 크루스칼을 통해 mst를 찾는 문제이다.
## 이미 연결된 통료는 미리 union을 해주고
## 그 이후에 나머지 노드들을 연결해야 한다(기준은 거리가 짧은 순서대로)
## 밑에 풀이 코드에서 for문의 조건 중 cnt를 n-1-m 개로 제한을 하면 틀린다.(전체 노드 개수 - 1개가 mst 간선의 개수이니까)
## 이유는 이미 연결된 통로가 사이클을 이룰 경우 필요한 간선을 잇지 못한다.
## 이미 연결된 통로의 간선이 mst를 이루고 있을 것이라고 생각했기 때문에 틀렸었다.


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
        parent[py] = px
    else:
        parent[px] = py

n, m = map(int, input().split())

# 노드 정보를 받고
lst = [0] + [list(map(int, input().split())) for _ in range(n)]
# 연결된 통로 정보를 담는다
already = []
for _ in range(m):
    x, y = map(int, input().split())
    already.append([x, y])

# 부모 리스트를 만들고
parent = [i for i in range(n+1)]

# 주어진 노드들에 대해 모든 간선의 거리를 노드번호와 함께 담는다
distance = []
for x in range(1, n):
    for y in range(x+1, n+1):
        dist = ((lst[x][0] - lst[y][0])**2 + (lst[x][1] - lst[y][1])**2)**(1/2)
        distance.append([x,y,dist])
# 거리를 담은 리스트를 거리를 기준으로 정렬한다        
distance.sort(key = lambda x: x[2])

# 이미 연결된 통로들을 union해서 묶는다
for edge in already:
    union(edge[0], edge[1])


res = 0
# cnt = n - 1 - len(already)
### 모든 가능한 간선들에 대해 union-find를 실행한다
for edge in distance:
    # if cnt == 0:
    #     break
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        res += edge[2]
        # cnt -= 1

res = round(res, 2)
print(f'{res:.2f}')


