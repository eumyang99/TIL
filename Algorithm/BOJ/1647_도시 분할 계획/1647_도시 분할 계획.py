from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

# 1
## 크루스칼로도 풀어봄

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(px, py):
    parent[py] = px

n, m = map(int, input().split())
pq = []
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(pq, (w, s, e))

parent = [i for i in range(n+1)]
res = 0
cnt = 0
for i in range(m):
    if cnt == n-2:
        break
    w, s, e = heapq.heappop(pq)
    ps, pe = find(s), find(e)
    if ps != pe:
        res += w
        union(ps, pe)
        cnt += 1

print(res)



# 2
## heapq 프림으로 풀어봤다.
## start를 처음 pq에 넣는다(weight, 연결할 node)
## pq를 pop해서 연결할 노드가 연결되어 있지 않다면
## res에 가중치를 더해주고 v-1개의 간선만 필요하니 cnt로 while문을 관리한다.
## 그리고 연결할 노드를 방문처리한다.
## 지금 막 연결된 노드에서 갈 수 있는 간선들 중 방문하지 않은 노드간선을 다시 pq에 다 넣어준다.
## 이를 반복한다.

# def prim(start):
#     res = 0
#     max_weight = 0
#     cnt = 0
#     visited = [0] * (n+1)
#     pq = []
#     pq.append((0, start))

#     while pq:
#         weight, node = heapq.heappop(pq)
#         if visited[node] == 0:
#             res += weight
#             visited[node] = 1
#             cnt += 1 
#             if weight > max_weight:
#                 max_weight = weight
#             if cnt == n:
#                 break
#            
#             for next_weight, next_node in dic[node]:
#                 if visited[next_node] == 0:
#                     heapq.heappush(pq, (next_weight, next_node))
        
#     return res - max_weight


# n, m = map(int, input().split())
# dic = defaultdict(list)

# for _ in range(m):
#     s, e, w = map(int, input().split())
#     dic[s].append((w, e))
#     dic[e].append((w, s))
# else:
#     start = s

# print(prim(start))









# 3
## SSAFY 1학기 때 배운 방법으로는 시간초과가 난다.
## 어차피 매번 최소값을 찾아야 하니까 heapq를 써야 시간초과가 안난다.

# def prim(start):
#     ## 리스트 초기화
#     visited = [0] * (n+1)
#     weight = [float("inf")] * (n+1)

#     ## 시작점 지정
#     visited[start] = 1
#     weight[start] = 0


#     ## 초기 start에서 연결 가능한 노드,간선 값 할당
#     for info in dic[start]:
#         # if weight[info[0]] > info[1]:
#         weight[info[0]] = info[1]


#     ## 현재 연결할 수 있는 노드 중에 가중치가 가작 작은 노드 연결
#     for _ in range(n-1):
#         min_val = float("inf")
#         for i in range(n+1):
#             if visited[i] == 0 and weight[i] < min_val:
#                 idx = i
#                 min_val = weight[i]

#         visited[idx] = 1

#         ## 위에서 새롭게 추가된 노드로부터 갈 수 있는 노드들의 가중치를 비교해서
#         ## 최저 비용의 간선들만 사용하도록 기록
#         for info in dic[idx]:
#             if visited[info[0]] == 0 and info[1] < weight[info[0]]:
#                 weight[info[0]] = info[1]

#     return weight[1:]



# n, m = map(int, input().split())
# dic = defaultdict(list)

# for _ in range(m):
#     s, e, w = map(int, input().split())
#     dic[s].append((e, w))
#     dic[e].append((s, w))
# else:
#     start = s

# weight_lst = prim(start)
# print(sum(weight_lst) - max(weight_lst))
