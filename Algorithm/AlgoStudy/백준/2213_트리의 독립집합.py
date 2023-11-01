from collections import defaultdict, deque
import sys
input = sys.stdin.readline

## 발상

##### 최대값 구하기
## 재귀 + dp
## dp 2차원 배열에 해당 node를 사용했을 때와 사용하지 않았을 때의 값을 저장한다
## 재귀를 돌며
## 현재 node를 사용한다면 (현재 node의 가중치) + (다음 node들의 사용하지 않는 값의 합)을 저장
## 현재 node를 사용하지 않는다면 다음 node들의 (사용한 값)과 (사용하지 않는 값) 중 큰 값들의 합을 저장
## 해당 node에 대한 계산이 dp에 저장되어 있다면 dp값 사용
## dp[시작node]에서 (사용한 값)과 (사용하지 않을 값) 중 큰 값을 출력

##### 경로 구하기
## bfs로 dp에 저장된 값을 사용
## que에 (현재 node, 전 node의 사용여부)를 저장
## 시작node부터 출발 : (시작node, 0)

## 1) 이전 node를 사용하지 않았을 경우 : (node, 0)
## 1-1) dp에 저장된 현재 node의 값 중 사용한 값이 크다면 node를 arr에 저장하고
## 다음 node들에 사용여부 1 넘김
## 1-2) 사용하지 않은 값이 크다면 arr에 저장하지 않고
## 다음 node들에 사용여부 0 넘김

## 2) 이전 node를 사용한 경우 (node, 1)
## 현재 node를 arr에 저장하지 않고
## 다음 node들에 사용여부 0 넘김

## 저장된 arr를 정렬하고 출력


def uu(node, is_use, before_node):
    ## before_node로 탐색이 역으로 진행되는 것을 막음
    ## cycle이 없는 tree 이기 때문에 가능

    ## is_use
    ## node 사용한다면 현재 node의 가중치를
    ## 사용하지 않는다면 0을 저장
    accu = weight[node] if is_use else 0

    ## node 사용
    if is_use:
        ## 다음 node를 탐색하며
        for next_node in dic[node]:
            ## 이전 node는 방문하지 않음
            if next_node == before_node:
                continue
            
            ## 현재 node를 사용하니 다음 node를 (사용하지 않는 값)을 accu에 추가
            ## 다음 node의 (사용하지 않는 값)이 dp에 있다면 사용
            if dp[next_node][0] != -1:
                accu += dp[next_node][0]
            ## dp에 없다면 재귀
            else:
                accu += uu(next_node, 0, node)

    ## node 미사용
    else:
        ## 다음 node를 탐색하며
        for next_node in dic[node]:
            ## 이전 node는 방문하지 않음
            if next_node == before_node:
                continue
            
            ## 현재 node를 사용하지 않으니
            ## 다음 node의 (사용한 값)과 (사용하지 않는 값) 중 큰 값을 accu에 추가

            ## 다음 node의 사용하지 않는 값 temp_1
            if dp[next_node][0] != -1:
                temp_1 = dp[next_node][0]
            else:
                temp_1 = uu(next_node, 0, node)

            ## 다음 node의 사용한 값 temp_2
            if dp[next_node][1] != -1:
                temp_2 = dp[next_node][1]
            else:
                temp_2 = uu(next_node, 1, node)

            ## temp_1과 temp_2 중 큰 값을 accu에 추가
            accu += max(temp_1, temp_2)

    ## dp[현재 node][사용여부] 값에 accu 할당
    dp[node][is_use] = accu
    ## accu 반환
    return accu


n = int(input())
weight = [0] + list(map(int, input().split()))
dic = defaultdict(list)
for _ in range(n-1):
    x, y = map(int, input().split())
    dic[x].append(y)
    dic[y].append(x)
else:
    node = x

dp = [[-1,-1] for _ in range(n+1)]

## 시작node의 사용여부에 따라 두 번 함수 실행
## 첫번째 함수에서 dp값을 저장하기 때문에
## 두번재 함수는 부담이 없을 것
uu(node, 0, node)
uu(node, 1, node)
print(max(dp[node]))

## 시작 node와 이전 node 사용여부를 que에 담음
## 시작 node는 independent에 담을 수도 있기 때문에 사용여부를 0으로 초기화
que = deque([(node, 0)])
independent = []
visited = [0] * (n+1)
visited[node] = 1

while que:
    node, is_used = que.popleft()
    ## flag : 다음 node에 넘길 현재 node의 사용여부
    used_flag = 0
    ## 만약 이전 node가 사용되지 않았고
    if is_used == 0:
        ## 현재 node의 dp값 중 사용한 값이 크다면
        if dp[node][1] > dp[node][0]:
            ## 현재 node는 independent에 추가
            independent.append(node)
            ## 현재 node를 사용했기 때문에 flag에 1 할당
            flag = 1
    
    ## 다음 node를 순회하며
    for next_node in dic[node]:
        if not visited[next_node]:
            ## 현재 node의 사용여부를 함께 que에 담음
            que.append((next_node, used_flag))
            visited[next_node] = 1

## 정렬 후 출력
independent.sort()
print(*independent)
