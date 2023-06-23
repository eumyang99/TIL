import sys
import heapq
input = sys.stdin.readline

## 발상
## 만약 1,3,5의 센서를 묶는 기지국이 있을 때, 기지국의 위치는 1,2,3,4,5 중 어디에 있어도 괜찮다.
## 따라서 중요한 것은 '센서들을 어떻게 묶을 것이냐' 이다.
## 센서를 묶는 기준은 정렬된 센서 리스트에서 i와 i+1번 째 센서의 간격이다.
## 간격이 큰 순서대로 그룹을 나누면 된다.
## 따라서 첫번째 센서와 마지막 센서의 길이(센서 전체 길이)에서 k-1개의 가장 큰 간격의 길이를 빼면 된다.

n = int(input())
k = int(input())
lst = list(map(int,input().split()))
lst.sort()

## sort 정렬로 최대값 찾기
gap = []
for i in range(n-1):
    gap.append(lst[i+1]-lst[i])
gap.sort(reverse=True)

res = lst[-1] - lst[0] - sum(gap[:k-1])
print(res)


## heap정렬로 최대값 찾기
# gap = []
# for i in range(n-1):
#     heapq.heappush(gap, -(lst[i+1]-lst[i]))

# delete = 0
# if gap:
#     for i in range(k-1):
#         delete -= heapq.heappop(gap)
# res = lst[-1] - lst[0] - delete
# print(res)

