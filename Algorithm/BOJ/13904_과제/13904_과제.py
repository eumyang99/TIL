import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

## 백준 순위에 드는 코드를 보면 더 효율적인 방법으로 푼다.
## 과제 점수를 기준으로 과제들을 내림차순 정렬한다(d, w).
## 이것을 순회하면서 해당 날짜(d)에 문제를 풀 수 있으면 푼다.
## 해당 날짜에 문제를 풀 수 없으면 d -= 1 하면서 풀 수 있는 경우에 푼다.
## 만약 d가 0이 된다면 이 문제는 풀 수 없는 문제이다.
## 이미 모든 자리에 이 문제보다 점수가 큰 과제들을 배치했다는 뜻이기 때문.

## 예시 코드
# import sys

# #sys.stdin = open("input5.txt",'r')
# input = sys.stdin.readline
# array = []
# # 문제에서 n<= 1000이기 때문
# visit = [False] * 1001

# # 갯수 받기
# n = int(input())

# for i in range(n):
#     d, s = map(int,input().split())
#     array.append((d,s))
# array.sort(key = lambda x : x[1], reverse =True)

# answer = 0

# for day, score in array:
#     # 각 점수마다 내림차순 했으므로 그 날짜 값에 해당 되는 값을 우선적으로 넣음
#     i = day
#     while i > 0 and visit[i]:
#         i -= 1
#     # 해당되는값 없으면 패스
#     if i == 0:
#         continue
#     else:
#         visit[i] = True
#         answer += score
# print(answer)

######################################################################
## 아래는 나의 풀이

## 발상
## 마지막 날부터 점수를 채워간다.
## 예를 들어 4일 째에는 마감일이 4일 보다 큰 과제들만 제출할 수 있다.
## 따라서 날짜별로 가중치를 heap 정렬하고 4일 보다 큰 과제들의 인덱스가 0번째인 녀석들만
## 크기를 비교해서 가장 가중치가 큰 녀석을 res에 더하면서 heappop을 한다.
## 그 다음 3일 째에도 이것을 반복한다.
## 즉 마지막 날부터 해결할 수 있는 가장 큰 점수의 문제를 해결해 나간다.


n = int(input())
dic = defaultdict(list)
dup = []

for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(dic[d], -w)
    if d not in dup:
        dup.append(d)

res = 0
dup.sort(reverse = True)
for day in range(dup[0], 0, -1):
    max_dw = [0,0]
    for d in dup:
        if d >= day:
            if len(dic[d]) != 0:
                if dic[d][0] < max_dw[1]:
                    max_dw = [d, dic[d][0]]
        else:
            break
    if max_dw[0] != 0:
        res -= heapq.heappop(dic[max_dw[0]])

print(res)
    
