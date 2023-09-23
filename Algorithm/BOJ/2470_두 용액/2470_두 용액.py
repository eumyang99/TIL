import sys
input = sys.stdin.readline

## 내 발상
## a, b, c, d, e, f 가 오름차순으로 정렬되어 있을 때,
## a, f 를 먼저 계산
## 그리고 a와 e, b와 f 중 절대값이 작은 녀석을 채택해서 left or right 값을 갱신
## 그러다가 left와 right가 만나면 그만
## 와중에 최소값과 비교해서 최소값이 갱신될 때 해당 녀석들의 인덱스를 저장
## 근데 이게 왜 되는지 모르겠다...?

## 정석적인 접근법
## a, f를 먼저 계산하고
## 이것이 0보다 크면 0과 가까워져야 하니까 right를 한 칸 왼쪽으로(큰 값을 줄임),
## 이것이 0보자 작으면 마찬가지로 0과 가까워져야 하니까 left를 한 칸 오른쪽으로(작은 값을 키움)
## 그러다가 left, right 만나면 그만
## 와중에 min값과 계속 비교하면서 인덱스 저장

## 내 풀이
# n = int(input())
# lst = list(map(int, input().split()))
# lst.sort()

# left, right = 0, n - 1
# res = abs(lst[left] + lst[right])
# res_left, res_right = left, right
# while right - left != 1:
#     x = abs(lst[left] + lst[right - 1])
#     y = abs(lst[left + 1] + lst[right])
#     if x <= y:
#         right -= 1
#         if x < res:
#             res_left, res_right = left, right
#             res = x
#     else:
#         left += 1
#         if y < res:
#             res_left, res_right = left, right
#             res = y

# print(lst[res_left], lst[res_right])


## 정석 풀이
n = int(input())
lst = list(map(int, input().split()))
lst.sort()

left, right = 0, n - 1
res = float("inf")
res_left, res_right = left, right
while left < right:
    temp = lst[left] + lst[right]
    if abs(temp) < res:
        res = abs(temp)
        res_left, res_right = left, right
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    else:
        break
print(lst[res_left], lst[res_right])
