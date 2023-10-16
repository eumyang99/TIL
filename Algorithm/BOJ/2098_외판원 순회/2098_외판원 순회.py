import sys
input = sys.stdin.readline

## 풀이 참조
## 비트마스크를 이용한 dp

## 비트마스크
## 1이면 해당 위치에 있는 노드 방문
## 0이면 미방문

## dp[x][visited]
## x : 현재 위치한 노드
## visited : 이진수로 표현된 방문처리

## dp[3][01111] : 0, 1, 2를 방문하고 3까지 왔을 때, 이후 나머지를 방문하고 다시 0으로 돌아오는 가중치
## 만약 dp[3][01111] 이 기 방문한 루트라면 그 값을 가져옴
## ex)
## 0 -> 1 -> 2 -> 3 방문해서 dp[3][01111]을 기록했다면 
## 0 -> 2 -> 1 -> 3 으로 루트를 탐색할 때 에[3][01111]의 값을 가져다 쓰면 됨
## 두 루트 모두 0, 1, 2, 3을 방문했을 때, 이후 나머지를 방문하고 다시 0으로 돌아오는 가중치 라는 점에서 같기 때문


import sys
input = sys.stdin.readline

def uu(x, visited):
    ## n이 5일 때,
    ## visited : 11111
    ## (1 << 5) : 100000
    ## (1 << 5) - 1 : 11111
    ## 즉 모두 방문했을 때
    if visited == (1 << n) - 1:
        ## 해당 x노드에서 시작점 0으로 갈 수 있으면 
        if arr[x][0]:
            ## 그 가중치를 리턴
            return arr[x][0]
        ## 길이 없으면
        else:
            ## 무한을 리턴
            return float("inf")
    
    ## x노드까지 도착했고 방문해야 할 남은 루트의 가중치가 이미 계산되어 있다면
    if dp[x][visited] != -1:
        ## 계산된 값을 리턴
        return dp[x][visited]
    
    ## dp에 저장할 mini 변수를 무한으로 초기화
    mini = float("inf")
    for i in range(1, n):
        ## 길이 없다면 넘김
        if not arr[x][i]:
            continue
        
        ## 이미 방문했던 노드라면 넘김
        if visited & (1 << i):
            continue
        
        ## 방문하지 않은 노드에 대하여
        ## mini는 mini와 (i 노드를 방문했을 때 남은 루트의 가중치 + i 노드로 가는 가중치의 합) 중 작은 것으로 갱신
        ## ex)
        ## 현재 visited : 01001
        ## 가능한 i : 1, 2, 4
        ## 각각 01011, 01101, 11001
        ## dp[1][01011] 의 가중치 + x에서 1로 가는 가중치    
        ## dp[2][01101] 의 가중치 + x에서 2로 가는 가중치    
        ## dp[4][11001] 의 가중치 + x에서 4로 가는 가중치
        ## dp[x][01001]에 위 셋 중 작은 값을 저장
        ## 해당 값을 리턴    
        mini = min(mini, uu(i, visited | (1 << i)) + arr[x][i])
        dp[x][visited] = mini
    return mini

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]
print(uu(0, 1))
