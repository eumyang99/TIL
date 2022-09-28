## 크루스칼 알고리즘

import sys
sys.stdin = open('input.txt')

def findset(x):                     # 대표 노드를 찾는 함수
    if x == tree[x]:
        return x
    else:
        return findset(tree[x])

def union(x, y):                    # 두 노드집단을 묶는 함수
    tree[y] = x
    rank[x] = rank[y] + 1           # 흡수하는 대표노드의 랭킹을 높임
    return

T = int(input())
for case in range(T):
    v, e = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(e)]
    lst.sort(key=lambda x: x[2])                                # 가중치가 작은 녀석들 순서로 정렬

    tree = [i for i in range(v+1)]                              # 노드집단을 표현하는 리스트
    rank = [0 for _ in range(v+1)]                              # 노드의 랭킹을 담는 리스트

    res = 0                                 # 출력할 결과
    cnt = 0                                 # 이어진 간선의 개수(노드 개수 -1개 까지만 반복)
    for info in lst:                        # 정렬된 간선 정보를 순회하면서
        if cnt < v:                         # 노드 개수가 다 차지 않았다면
            v1 = findset(info[0])               # 간선의 시작점의 대표 노드를 v1
            v2 = findset(info[1])               # 간선의 도착점의 대표 노드를 v2
            if v1 != v2:                        # 두 대표가 다르다면 이어주는데
                if rank[v1] >= rank[v2]:        # 랭킹이 높은 녀석에게 낮은 녀석을 흡수시킴
                    union(v1, v2)
                else:
                    union(v2, v1)
                res += info[2]                  # 이어진 간선의 가중치를 res에 추가
        else:                               # 노드 개수가 다 찼으면 종료
            break

    print(f'#{case+1} {res}')






























    # lst = [[50]*(v+1) for _ in range(v+1)]
    
    # for i in range(v+1):
    #     lst[i][i] = 0
    
    # for _ in range(e):
    #     s, e, w = map(int, input().split())
    #     lst[s][e] = w