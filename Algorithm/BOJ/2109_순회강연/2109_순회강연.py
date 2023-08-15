from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

## 이건 heap으로!

n = int(input())
if n == 0:
    print(0)
else:
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: x[1])
    able = []

    res = 0
    latest = lst[-1][1]
    for day in range(latest, 0, -1):
        while lst and lst[-1][1] >= day:
            p, d = lst.pop()
            heapq.heappush(able, -p)
        if able:
            res -= heapq.heappop(able)

    print(res)


## 딕셔너리에 담아서 마지막 날부터 가능한 강의 찾아서 풀이
# n = int(input())
# dic = defaultdict(list)
# latest = 0
# for _ in range(n):
#     p, d = map(int, input().split())
#     heapq.heappush(dic[d], -p)
#     latest = max(d, latest)
# days = list(dic.keys())
# days.sort(reverse=True)
# dic[latest+1].append(0)

# res = 0
# for today in range(latest, 0, -1):
#     max_day = latest+1
#     for day in days:
#         if today <= day:
#             if dic[day] and dic[max_day][0] > dic[day][0]:
#                 max_day = day 
#         else:
#             break
#     if dic[max_day][0] != 0:
#         res -= heapq.heappop(dic[max_day])
# print(res)

