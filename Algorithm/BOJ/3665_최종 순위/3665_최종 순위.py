import sys
input = sys.stdin.readline

## 발상
## 이전 년도의 최종결과를 보고 -> -> -> -> 이런식으로 간선이 연결되어 있을 거라고 생각했다.
## 그러나 이렇게 되면 barrier가 모두 1이기 때문에 문제를 풀어나가기 힘들다.

## 따라서 a순위의 팀은 a순위 이후의 모든 팀으로 갈 수 있는 간선이 있다고 생각해야 한다.
## 그리고 진입차수가 적은 순서대로 순위가 결정된다.

## 그렇기 때문에 순위가 바뀐다는 정보를 두 팀 간의 간선 방향을 바꾼다고 생각하고
## 진입차수를 계산한다.
## 그 진입차수를 토대로 순위를 출력한다.
## 만약에 순위가 바뀌었을 때 모순되는 상황은 같은 진입차수를 가지고 있는 팀이 있을 때이다.
## 그러한 경우 사이클이 생긴다.

## 도대체 이걸 어떻게 떠올렸을까???? 천재가 많다....



## 아래는 매우 효율적으로 최적화된 코드
T = int(input())
def solution():
    N = int(input())
    arr = list(map(int, input().split(' ')))

    ## 진입차수
    in_degree = [0] * (N+1)

    ## enumerate를 사용해서 인덱스와 값을 동시에 가져온다.
    ## 이 문제에서 인덱스는 곧 진입차수의 의미를 갖기 때문에 초기 진입차수를 기록한다.
    for i,v in enumerate(arr):
        in_degree[v] = i

    original_arr = [*in_degree]
    I = int(input())
    for _ in range(I):
        t1, t2 = map(int, input().split(' '))
        front, back = 0, 0
        ## 순서가 바뀌는 팀을 받고
        ## 두 팀의 진입차수를 비교해서 어느 팀이 순위가 높은 팀인지 비교하고
        ## 순위가 높은 팀의 진입차수를 -1, 순위가 낮은 팀의 진입차수를 +1 한다.
        ## 이는 간선의 방향을 바꿨다는 의미와 연결된다.
        if original_arr[t1] < original_arr[t2]:
            front, back = t2, t1
        else:
            front, back = t1, t2
        in_degree[front] -= 1
        in_degree[back] += 1

    ## 출력할 리스트를 만든다.
    ## 이 리스트의 인덱스는 곧 순위이다.
    result = [0] * N
    ## 마찬가지로 enumerate를 사용해서 진입차수의 인덱스와 값을 받는다.
    for i, v in enumerate(in_degree):
        ## 진입차수(여기서는 i)는 팀명이고 값(여기서는 v)은 순위이다.
        ## 아직 순위가 정해지지 않은 자리에
        if not result[v]:
            ## 순위와 연결된 인덱스에 팀명을 넣는다
            result[v] = i
        ## 이미 순위가 정해진 자리에 또다른 팀을 넣어야 한다면 모순이기 때문에 impossible을 출력한다.
        else:
            return print('IMPOSSIBLE')
        
    ## result를 출력한다
    return print(*result, sep=" ")

for _ in range(T):
    solution()



## 아래는 비효율적인 나의 코드
t = int(input())
for _ in range(t):
    n = int(input())
    rank = [0] + list(map(int, input().split()))
    c = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(c)]
    
    edges = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for team in rank[1:i+1]:
            edges[rank[i+1]][team] = 1

    for a, b in lst:
        if edges[a][b]:
            edges[a][b] = 0
            edges[b][a] = 1
        else:
            edges[a][b] = 1
            edges[b][a] = 0

    barrier = [0] * (n+1)
    for i in range(1, n+1):
        barrier[i] = sum(edges[i])


    for i in range(1, n+1):
        if barrier[i] == 0:
            que = [i]

    if len(que) != 1:
        print("IMPOSSIBLE")
        continue
    
    res = []
    while que:
        team = que.pop()
        res.append(team)

        cnt = 0
        for i in range(1, n+1):
            if edges[team][i] == 0:
                barrier[i] -= 1
                if barrier[i] == 0:
                    cnt += 1
                    que.append(i)
        if cnt > 1:
            break

    if len(res) != n:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, res)))