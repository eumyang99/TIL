from collections import defaultdict
import sys
input = sys.stdin.readline

## 발상
## 메모이제이션, 위상정렬
## 기본적으로 위상정렬 문제이다.
## 하지만 최대 소요시간을 찾아야 하기 때문에
## A노드에 도착한 현재 소요시간과 과거에 도착한 A노드의 소요시간 중 최대값으로 갱신해 나간다. 

def uu():
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    dic = defaultdict(list)
    barrier = [0]*(n+1)
    ## 소요시간, 부모 노드, 자식 노드의 정보가 담긴 간선을 dic에 저장
    ## 자식 노드의 진입차수 += 1
    for _ in range(k):
        s, e = map(int, input().split())
        w = cost[s]
        dic[s].append((w, s, e))
        barrier[e] += 1
    goal = int(input())

    ## 만약 시작 노드와 목표 노드가 같다면 목표 노드의 소요 시간 출력 후 종료
    if not barrier[goal]:
        return print(cost[goal])

    ## dp 0으로 초기화
    dp = [0] * (n+1)
    ## 진입차수가 0인 노드(시작점)를 que에 추가
    que = []
    for i in range(1, n+1):
        if not barrier[i]:
            que.append(i)

    ## 부모 노드를 pop하고
    ## pop한 부모 노드에서 갈 수 있는 자식 노드들을 순회
    ## 자식 노드의 dp값에 기 저장된 자식노드의 소요시간과 현재 시작노드 소요시간 + 간선의 가중치를 더해서 큰 값을 저장한다
    ## 만약 목표 노드의 진입차수가 0이 되었다면 목표노드까지의 도착 시간 + 목표 노드의 소요시간을 출력 후 종료 
    while que:
        s = que.pop()
        for w, s, e in dic[s]:
            dp[e] = max(dp[e], dp[s] + w)
            barrier[e] -= 1
            if not barrier[e]:
                if e == goal:
                    print(dp[goal] + cost[goal])
                    return
                que.append(e)


t = int(input())
for i in range(t):
    uu()



