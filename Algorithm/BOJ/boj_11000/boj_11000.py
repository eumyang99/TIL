import heapq 
import sys
input = sys.stdin.readline

# 가장 먼저 강의 시작 시간을 기준으로 정렬
# 각 강의실의 강의 종료시간 중 가장 빠른 것을 계속 추적해야 함

# 가장 빠른 강의 종료 시간 보다 다음 강의 시작 시간이 같거나 이후일 경우
    ## 두 강의는 같은 강의실에서 진행할 수 있음
    ## 따라서 이 강의실의 종료 시간을 갱신해줌
# 가장 빠른 강의 종료 시간 보다 다음 강의 시작 시간이 빠른 경우
    ## 두 강의는 같은 강의실에서 진행될 수 없기 때문에
    ## 새로운 강의실을 잡고 이 강의실의 종료 시간을 기록 해둠
# 각 강의실의 종료시간을 모아서 정렬하고 종료 시간이 가장 빠른 강의실과 다음 강의실을 계속 비교하면 됨
# 강의 종료시간을 계속 정렬하고 갱신해야 하기 때문에 heapq로 리스트를 관리함


n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append([s, e])

lst.sort(key= lambda x: x[0])

room = [lst[0][1]]
for i in range(1, n):
    if lst[i][0] < room[0]:
        heapq.heappush(room, lst[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lst[i][1])

print(len(room))