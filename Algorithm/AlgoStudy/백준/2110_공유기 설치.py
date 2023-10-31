import sys
input = sys.stdin.readline

## 풀이 참고
## 최소 거리를 이분탐색으로 찾아내는 문제이다

## 최소 거리가 될 수 있는 범위를 초기에 (left:0, right:가장 먼 두 집의 거리)로 둔다
## 그 중간값을 탐색 거리로 두고
## 첫 집부터 탐색 거리보다 멀거나 같은 집이 있으면 cnt += 1
## 해당 집을 다시 비교할 집으로 갱신하고 이 집보다 멀거나 같은 집이 있는지 반복하여 확인한다.
## 만약 cnt가 원하는 공유기 개수보다 작다면 탐색 거리를 줄인다.
## 그렇지 않다면 출력할 최소거리(res)를 갱신하고 탐색 거리를 늘린다.

## 이분 탐색이 종료되면 res를 출력한다.

n, c = map(int, input().split())
## 이분 탐색을 위한 정렬
arr = sorted([int(input()) for _ in range(n)])

## 출력값
res = 0
## 이분 탐색의 (시작 값 : 0, 끝 값 : 가장 먼 두 집 간의 거리) 초기화
min_dist, max_dist = 0, arr[-1] - arr[0]

## 이분 탐색
while min_dist <= max_dist:
    ## 탐색 거리 distx
    dist = (min_dist + max_dist) // 2
    ## 비교할 집 초기화(첫 집)
    start = arr[0]
    ## 첫 집 공유기 설치
    cnt = 1
    ## res를 갱신할 temp_dist
    ##가능한 거리 중 작은 값을 찾아야 해서 inf로 초기화
    temp_dist = float("inf")
    ## 집 탐색
    for i in range(1, n):
        ## 공유기 설치 가능한 집이면
        if arr[i] - start >= dist:
            ## 카운트
            cnt += 1
            ## 가능한 집 간의 거리 중 가장 짧은 값으로 갱신
            temp_dist = min(temp_dist, arr[i] - start)
            ## 비교할 집 갱신
            start = arr[i]

    ## 공유기 설치가 덜 되었다면 거리 줄임
    if cnt < c:
        max_dist = dist - 1
    ## 공유기 설치가 충분히 되었다면
    ## res를 temp_dist로 갱신하고
    ## 거리 늘임
    else:
        res = max(res, temp_dist)
        min_dist = dist + 1

print(res)
