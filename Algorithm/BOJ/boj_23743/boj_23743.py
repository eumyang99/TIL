import sys
input = sys.stdin.readline
from collections import defaultdict

def findset(x):                 # 대표 노드 찾기                     
    while x != parent[x]:
        x = parent[x]
    return x

def union(a, b):
    if rank[a] > rank[b]:       # 랭킹을 비교하며 흡수하는 집단과 흡수되는 집단을 나누며 병합
        parent[b] = a           # 흡수되는 집단의 출구 비용이 흡수하는 집단의 출구 비용보다 적을 경우
        if exit[a] > exit[b]:   # 적은 출구 비용을 흡수하는 집단의 대표노드에 갱신
            exit[a] = exit[b]
    elif rank[a] < rank[b]:
        parent[a] = b
        if exit[b] > exit[a]:
            exit[b] = exit[a]
    else:
        parent[b] = a
        rank[a] += 1
        if exit[a] > exit[b]:
            exit[a] = exit[b]


v, e = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(e)]
exit = [0] + list(map(int, input().split()))
lst.sort(key=lambda x: x[2])                # 크루스칼 이용이기 때문에 가충치 오름차순 정렬

parent = [i for i in range(v+1)]            # 대표 노드 관계 리스트
rank = [0]*(v+1)                            # 대표 노드의 랭크 리스트
res = 0                                     # 출력할 결과

for s, e, w in lst:                         # 리스트 처음부터 순회하며
    ps, pe = findset(s), findset(e)         # 시작과 도착의 대표 노드를 찾고
    if ps != pe:                                # 두 대표 노드가 다르면서
        if max(exit[ps], exit[pe]) > w:             # 출구 설치와 가중치를 비교해서 포탈을 만들어야 한다면
            union(ps, pe)                           # 두 노드 집단을 합침
            res += w                                # 가충치 누적
        else:                                   # 포탈을 만드는 게 손해라면
            continue                                # 다음 간선으로
    else:                                   # 대표노드가 같다면 연결할 필요가 없으니
        continue                                # 다음 간선으로

p = set()
for i in range(v+1):                        # 모든 정점의 대표 노드를 찾아서
    rep = findset(i)                
    if rep not in p:                        # p에 들어있지 않다면
        p.add(rep)                          # 해당 대표 노드를 저장하고
                                            # 위의 union 함수에서 대표노드를 연결할 때 흡수하는 대표 노드에 두 집단 중 작은 출구 비용을 갱신
        res += exit[rep]                    # 해당 노드 집단 중 가장 소모 작은 출구를 설치
print(res)

