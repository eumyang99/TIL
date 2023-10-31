import sys
input = sys.stdin.readline

## 발상
## 전제 1.
## 첫 전시회관부터 마지막 전시회관까지 이동하는 거리는 출입구가 어디인지 상관이 없이 같기 때문에,
## 첫 전시회관과 마지막 전시회관의 위치만 사용하면 됨

## 전제 2.
## 출입구에서 첫 전시관으로 갔다가 마지막 전시관으로 간 후 다시 출입구로 돌아오는 거리와
## 출입구에서 마지막 전시관으로 갔다가 첫 전시관으로 간 후 다시 출입구로 돌아오는 거리가 같기 때문에
## 첫 전시관과 마지막 전시관 중 작은 것을 첫 전시관으로 하고 큰 것을 마지막 전시관으로 해도 상관이 없다

## 접근 1.
## 모든 고양이의 첫 전시관(start)와 마지막 전시관(end)를 수직선 상에 서로 다른 행에 직선으로 긋는다

## 접근 2. *핵심
## 출발점을 1부터 하나씩 키워나갈 때
## 출발점이 특정 직선에 아직 닿기 전이라면 해당 고양이의 이동거리는 줄어든다
## 출발점이 특정 직선 안에서 이동한다면 이동 거리는 변함이 없다
## 출발점이 특정 직선을 지나 닿지 않게 된다면 이동거리는 다시 늘어난다

## 결론.
## 따라서 이미 지나간 직선의 개수(출발점을 키워나갈 때 이동거리가 늘어남)와
## 아직 출발점과 닿지 않은 직선의 개수(출발점을 키워나갈 때 이동거리가 줄어듬)를
## 비교해서 이미 지나간 직선의 개수가 아직 닿지 않은 직선의 개수보다 크거나 같아질 때 멈춘다
## 이러한 상황이라면 출발점을 키워나가도 이동거리가 줄어드는 양보다 늘어나는 양이 같거나 크기 때문

## 최종 코드
## enter_lst : 시작점으로 등장하는 모든 숫자를 카운팅함
## exit_lst : 마지막 점으로 등장하는 모든 숫자를 카운팅함

## not_yet_cnt = n : 아직 닿지 않은 직선
## exit_cnt = 0 : 이미 지난 직선

## 1부터 m까지 순회를 하며
## enter_lst의 해당하는 값을 not_yet_cnt에서 감소시킴
## exit_lst의 해당하는 값을 exit_cnt에서 증가시킴
## not_yet_cnt <= exit_cnt 이면 해당 위치를 출력 

n, m = map(int, input().split())
## 리스트 초기화
enter_lst, exit_lst = [0] * (m+1), [0] * (m+1)

## 카운팅
for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[1] < temp[-1]:
        enter_lst[temp[1]] += 1
        exit_lst[temp[-1]] += 1
    else:
        enter_lst[temp[-1]] += 1
        exit_lst[temp[1]] += 1

## not_yet_cnt, exit_cnt 초기화
not_yet_cnt = n
exit_cnt = 0
## 순회 및 비교
for door in range(1, m+1):
    not_yet_cnt -= enter_lst[door]
    exit_cnt += exit_lst[door]
    if not_yet_cnt <= exit_cnt:
        print(door)
        break



## dictionary에 등장하는 전시회관의 번호에 등장 횟수를 담아 푼 코드
## 등장하는 출입문만 순회한다
## 시간이 더 오래 걸렸음 
# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# total_door_set = set()
# enter_dic, exit_dic = defaultdict(int), defaultdict(int)

# for _ in range(n):
#     temp = list(map(int, input().split()))
#     if temp[1] < temp[-1]:
#         enter_dic[temp[1]] += 1
#         exit_dic[temp[-1]] += 1
#     else:
#         enter_dic[temp[-1]] += 1
#         exit_dic[temp[1]] += 1
#     total_door_set.add(temp[-1])
#     total_door_set.add(temp[1])

# total_door = sorted(list(total_door_set))

# not_yet_cnt = n
# exit_cnt = 0
# for door in total_door:
#     not_yet_cnt -= enter_dic[door]
#     exit_cnt += exit_dic[door]
#     if not_yet_cnt <= exit_cnt:
#         print(door)
#         break


## 고양이의 수 만큼만 순회
## 출입문과 닿은 직선의 큰 값을 heap에 담고
## 출입문을 지나갈 때 heap에서 빼내며
## 지나간 직선의 개수를 세는 방법
## 시간이 오래 걸리는 풀이법
# def uu(arr, n):
#     pq = [arr[0][1]]
#     not_yet_cnt = n - 1
#     already_out_cnt = 0

#     for i in range(1, n):
#         start, end = arr[i][0], arr[i][1]
#         before_start = arr[i-1][0]

#         if start == before_start:
#             heapq.heappush(pq, end)
#             not_yet_cnt -= 1
#             if not_yet_cnt <= already_out_cnt:
#                 return print(start)
#             continue
        
#         while pq and pq[0] <= start:
#             door = heapq.heappop(pq)
#             already_out_cnt += 1
#             if not_yet_cnt <= already_out_cnt:
#                 return print(door)
        
#         heapq.heappush(pq, end)
#         not_yet_cnt -= 1
#         if not_yet_cnt <= already_out_cnt:
#             return print(start)
        
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     arr.append((min(temp[1], temp[-1]), max(temp[1], temp[-1])))
# arr.sort()
# uu(arr, n)



## 위와 같은 방식이나
## 시작점이 가작 작은 고양이의 시작점 + 1부터 m까지 순회
## 함수를 쓰지 않음
# import heapq
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     mini = min(temp[1], temp[-1])
#     maxi = max(temp[1], temp[-1])
#     arr.append((mini, maxi))

# arr.sort()

# pq = []
# start = arr[0][0]
# next_idx = 0
# for i in range(n):
#     if arr[i][0] == start:
#         heapq.heappush(pq, arr[i][1])
#     else:
#         next_idx = i
#         break 

# not_yet_cnt = n - len(pq)
# already_out_cnt = 0

# for i in range(start+1, m+2):
#     while pq and pq[0] < i:
#         heapq.heappop(pq)
#         already_out_cnt += 1

#     if not_yet_cnt <= already_out_cnt:
#         print(i-1)
#         break

#     while next_idx < n and arr[next_idx][0] == i:
#         heapq.heappush(pq, arr[next_idx][1])
#         next_idx += 1
#         not_yet_cnt -= 1

