import sys
sys.stdin = open('input.txt')

def findset(x):                     # 대표 노드 찾는 함수
    while x != tree[x]:
        x = tree[x]
    return x

def union(x, y):                    # 두 노드 집단 합치는 함수
    tree[y] = x
    rank[x] += 1

T = int(input())
for case in range(T):
    n, m = map(int, input().split())

    tree = [0] + [i for i in range(1, n+1)]     # 해당 노드의 대표 노드를 저장하는 리스트
    rank = [0]*(n+1)                            # 해당 노드의 자식 수를 저장하는 리스트

    lst = list(map(int, input().split()))   
    for i in range(m):
        v1 = findset(lst[i*2])                  # 시작 노드의 대표 노드 v1
        v2 = findset(lst[i*2+1])                # 도작 노드의 대표 노드 v2
        if v1 != v2:                            # v1, v2가 다르면 이어주는데
            if rank[v1] >= rank[v2]:            # 랭크가 높은 녀석이 작은 녀석을 흡수
                union(v1, v2)
            else:
                union(v2, v1)
    
    res = set()                                 
    for i in tree:                              # 대표 노드의 개수를 출력
        res.add(findset(i))
    print(f'#{case+1} {len(set(res))-1}')


