import sys
input = sys.stdin.readline
from collections import defaultdict

### 시작점 0부터 각 노드들까지 갈 수 있는 최단 거리를 기록하며
### 다음 노드를 기점으로(이미 이 노드까지 올 수 있는 최단 거리를 기록했음) 또 나아가면서 다다음 노드의 최단거리를 기록
### 이런 방법으로 나아가면서 마지막 도착 노드의 최단거리를 출력한다.



n, d = map(int, input().split())
dic = defaultdict(list)                         # 간선 정보를 담을 dic
distance = defaultdict(int)                     # 각 노드에 대한 거리정보를 담을 dic
for _ in range(n):
    s, e, dist = map(int, input().split())
    if e - s > dist and e <= d:                 # 사용할 수 없는 간선을 제외한 간선 정보 저장
        dic[s].append((e, dist))
        distance[s] = float("inf")              # 각 노드에 대해 거리를 무한으로 초기값 상정
        distance[e] = float("inf")


distance[d] = float("inf")                      # 도착 노드 거리 무한
distance[0] = 0                                 # 시작 노드인 0은 거리 0

nodelist = list(distance.keys())                # 노드들을 오름차순 정렬하고
nodelist.sort()
print(nodelist)
print(dic)
for start in nodelist:                          # 0부터 시작
    print(start)
    visited = []                                # 거리를 점검한 노드 체크
    for v in dic[start]:                                        # start노드로 시작되는 간선이 있다면
        visited.append(v[0])                                    # 도착노드를 방문처리하고
        if distance[v[0]] > distance[start] + v[1]:             # 도착노드 최소거리 갱신
            distance[v[0]] = distance[start] + v[1]
            print(distance)
    for end in nodelist:                                        # 간선이 없더라도 모든 노드로 갈 수 있기 때문에
        if end not in visited and end > start:                  # 방문하지 않은 노드이면서 현재 위치보다 뒤에 있는 노드에 대해
            if distance[end] > distance[start] + end - start:   # 최소거리 갱신
                distance[end] = distance[start] + end - start
                print(distance) 

print(distance[d])      # 도착 노드 거리 출력































# N, D = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(N)]
# dis = [i for i in range(D+1)]
# for i in range(D+1):
#     if i > 0:
#         dis[i] = min(dis[i], dis[i-1]+1)
#     for s, e, d in li:
#         if i == s and e <= D and dis[i]+d < dis[e]:
#             dis[e] = dis[i]+d
# print(dis[D])