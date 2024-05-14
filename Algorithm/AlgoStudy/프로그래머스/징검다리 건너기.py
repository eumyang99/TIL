## 배열의 길이가 k인 모든 구간의 최대값들을 비교해서 그 중 가장 작은 값을 찾는 문제

## 모든 구간에서 매번 최대값을 구하는 것은 실패할 방법
## stack으로 접근하다가 갈피가 잡히지 않아 우선순위 큐로 변경

## 핵심은 PQ에서 들고 있는 최대값이 현재 구간에 유효한 최대값인지 확인 후 
## 유효하지 않다면 pop하고 다음 최대값을 확인 후 같은 작업을 반복
## 유효한 최대값이면 answer와 비교해서 값을 갱신 

## 한 구간의 최대값을 찾으면 그 최대값의 다음 index부터 k개의 구간을 확인하면 됨
## 그러나 PQ에서 최대값의 index보다 작은 값들을 제거할 방법이 없음
## 따라서 이전의 모든 값들을 들고 있다가 PQ의 최대값이 유효한 구간의 최대값이 될 때까지 pop하면서 걸러냄

import heapq

def solution(stones, k):
    pq = []
    for i in range(k):
        ## 최대값을 찾기 위해 -를 붙임
        heapq.heappush(pq, (-stones[i], i))
    answer = pq[0][0]
    
    for i in range(k, len(stones)):
        ## 하나씩 값을 추가하면서
        heapq.heappush(pq, (-stones[i], i))
        ## i(현재 구간의 마지막 idx)를 기준으로 PQ의 최대값이 현재 구간 안에 있는지 확인
        ## 밖에 있다면 pop 반복
        while pq[0][1] <= i - k:
            heapq.heappop(pq)
        ## 유요한 최대값과 answer를 비교해서 값을 갱신
        answer = max(answer, pq[0][0])
        
    return -answer