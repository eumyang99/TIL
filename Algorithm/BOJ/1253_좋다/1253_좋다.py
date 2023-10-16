import sys
input = sys.stdin.readline

## 정석 발상
## for문을 활용한 투포인터

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0
res_set = set()
for i in range(n-1, -1, -1):
    if arr[i] in res_set:
        res += 1
        continue
    left = 0
    right = n-1
    while left < right:
        if arr[left] + arr[right] == arr[i]:
            if left != i and right != i:
                res += 1
                res_set.add(arr[i])
                break
            elif right == i:
                right -=1
            else:
                left += 1

        elif arr[left] + arr[right] < arr[i]:
            left += 1

        else:
            right -= 1

print(res)

# ## 나의 발상
# ## 1. 수열에서 두 개를 더해 만들 수 있는 수 x가 수열에 포함되어 있으면 car_set에 담음
#     ## 단, 두 숫자는 모두 0이 아니어야 함
# ## 2. car_set과 arr를 비교하며 같은 숫자가 있으면 res += 1
# ## 3. 만약 arr_set에 0이 있다면 arr를 순회하면서 해당 숫자가 car_set에 없는 경우에 
#     ## 0과 자기 자신을 더해서 있다고 판단하는 상황을 제외한 경우를 res에 더한다
#     ## ex) 0 1 1 1 의 경우 1은 모두 좋은 숫자
#     ## 그러나 0 1 2 4 의 경우 1, 2, 4는 좋은 숫자가 아니다
#     ## 따라서 같은 숫자가 여러개 있는 경우에만 0과 만나 좋은 숫자가 될 수 있다
#     ## 단, 0이 아닌 숫자들로 0을 만들 수 없는 경우, 0은 3개 이상 있어야 좋은 숫자가 될 수 있다
#     ## 이 경우 0 0 0은 0이 모두 좋은 숫자가 되지만, 0 0만 있을 경우 좋은 숫자가 될 수 없다 

# def uu():
#     n = int(input())
#     if n < 3:
#         return 0
#     arr = list(map(int, input().split()))
#     arr.sort()
#     arr_set = set(arr)

#     cal_set = set()
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if arr[i] != 0 and arr[j] != 0:
#                 if (arr[i] + arr[j]) in arr_set:
#                     cal_set.add(arr[i] + arr[j])

#     cal_lst = list(cal_set)
#     cal_lst.sort()
#     res = 0

#     pointer = 0
#     for i in range(len(cal_lst)):
#         for j in range(pointer, n):
#             if cal_lst[i] == arr[j]:
#                 res += 1
#                 continue
#             if cal_lst[i] < arr[j]:
#                 pointer = j
#                 break

#     if 0 in arr_set:
#         same_num_cnt = 0
#         for i in range(n-1):
#             if arr[i] in cal_set:
#                 continue
#             if arr[i] == arr[i+1]:
#                 same_num_cnt += 1
#             else:
#                 if same_num_cnt != 0:
#                     if arr[i] == 0 and same_num_cnt == 1:
#                         same_num_cnt = 0
#                         continue
#                     res += same_num_cnt + 1
#                     same_num_cnt = 0
#         else:
#             if same_num_cnt:
#                 res += same_num_cnt + 1

#     return res
# print(uu())