import heapq
import sys
input = sys.stdin.readline

## 벨만 포드 알고리즘
## 음수 가중치가 있는 경우의 최단거리를 찾아내는 알고리즘 문제이다.
## 벨만 포드 알고리즘 원리
## 1. 각 노드마다 inf로 가중치를 초기화한다.
## 2. 시작노드의 가중치를 0으로 갱신한다.
## 3. 모든 간선을 순회하며 시작 노드의 가중치가 inf가 아닌 경우
    ## (현재 노드의 가중치 + 간선의 비용 < 도착 노드의 가중치) 일 경우 도착 노드의 값을 갱신한다.
## 4. 이 과정을 (노드의 개수 - 1)번 반복한다.
    ## (노드의 개수 - 1)개의 간선만 이용했을 때의 값을 찾기 위해서(bfs 개념과 유사)
## 5. 그 이상 반복했을 때 여전히 최소값이 갱신되는 노드가 있다면 사이클이 존재하는 것
    ## a노드에서 b노드까지 연결할 때 최대 (노드의 개수 - 1)개의 간선만 필요하기 때문


## 나의 pq 풀이
## bfs로 진행되며 기준은 사용한 간선의 개수이다
## 사용한 간선의 개수가 작은 노드로부터 연결된 다른 노드들을 탐색하며 가중치를 갱신해 나간다
## 기존 경로보다 현재 경로가 더 작다면 가중치를 갱신하고 pq에 넣는다
## 사용된 간선이 (노드의 개수 - 1) 보다 크다면 사이클이 존재하는 것!

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    s, e ,w = map(int, input().split())
    edges[s].append((e, w))

weight = [float("inf")] * (n+1)
weight[1] = 0

que = [(0, 1)]
not_cycle = 1

while que:
    cnt, e = heapq.heappop(que)
    for ne, nw in edges[e]:
        if weight[e] + nw < weight[ne]:
            if ne == 1 or cnt == n:
                not_cycle = 0
                break
            weight[ne] = weight[e] + nw
            heapq.heappush(que, (cnt+1, ne))

if not_cycle:
    for i in range(2, n+1):
        if weight[i] == float("inf"):
            print(-1)
        else:
            print(weight[i])
else:
    print(-1)


## 왜 내 풀이가 정석 풀이보다 시간이 더 오래 걸릴까??
## 매번 모든 간선을 순회하는 것이 아니라 확인이 필요한 간선만 순회하는데...?


## 벨만포드 정석 풀이
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#벨만 포드 알고리즘 구현 함수 
def bf(start):
    #시작 노드에 대하여 초기화
    dist[start]=0
    #전체 n번의 라운드를 반복
    for i in range(n):
        #매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur]!=INF and dist[next_node]>dist[cur]+cost:
                dist[next_node] = dist[cur]+cost
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i==n-1:
                    return True
    return False
            
#노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
#모든 간선에 대한 정보를 담는 리스트
edges=[]
#최단 거리 테이블을 모두 무한으로 초기화
dist = [INF]*(n+1)

#모든 간선 정보를 입력받기
for i in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append([a,b,c])

#벨만 포드 알고리즘을 수행
negative_cycle = bf(1) #1번 노드가 시작 노드

if negative_cycle: #음수 순환이 존재하면
    print("-1")
else:
    for i in range(2,n+1):
        #도달할 수 없는 경우 -1출력
        if dist[i]==INF:
            print("-1")
        #도달할 수 있는 경우 거리 출력  
        else:
            print(dist[i])