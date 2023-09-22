import sys
input = sys.stdin.readline

## 에라토네스의 체 : 소수만 거르는 체
## 방법은 간단하다.
## 숫자를 나열하고 소수 가능성이 있는 가작 작은 수를 소수에 추가한다
## 그리고 추가한 수의 배수의 소수 가능성을 모두 없앤다
## [2], 4, 6, 8 ...
## [3], 6, 9, 12 ...

## 그리고 투포인터를 사용해서 구간합 검사
def uu(prime_nums, n):
    if n == 1:
        return print(0)
    
    res = 0
    start_idx, end_idx = 0, 0
    prime_sum = 2
    prime_cnt = len(prime_nums)
    while 1:
        if prime_sum <= n:
            if prime_sum == n:
                res += 1
            end_idx += 1
            if end_idx == prime_cnt:
                break
            prime_sum += prime_nums[end_idx]
        else:
            prime_sum -= prime_nums[start_idx]
            start_idx += 1
    print(res)

n = int(input())
prime_nums = []
nums = [False] + [True for _ in range(n)]
for this_num in range(2, n+1):
    if nums[this_num] == True:
        prime_nums.append(this_num)
        for i in range(this_num, n+1, this_num):
            if nums[i] == True:
                nums[i] = False

uu(prime_nums, n)


## 나의 첫 발상(시간 초과, 소수 판별에 시간이 걸리는 듯)
## 소수 판별은 기존 소수를 순회하며 기존 소수로 해당 숫자를 나누었을 때 나누어 떨어지는지 확인한다.
## 나누어 떨어지면 소수 아님
## 모두 나누어 떨어지지 않았다면 소수

## 해당 숫자를 소수 리스트에 추가하고
## 현재까지 더한 숫자에 추가로 더해준다
## 더해진 sum 값이 타겟보다 크다면 앞에서부터 숫자를 빼준다.(여기서는 누적값을 DP로 저장해서 뺏음)
## 차감된 값이 타겟이면 res += 1, dp에 추가
## 차감된 값이 타겟보다 작으면 그냥 dp에 추가
# n = int(input())
# if n == 1:
#     print(0)
# else:
#     dp = [2]
#     prime_nums = [2]
#     prime_sum = 2
#     start_idx = 0
#     res = 0
#     for num in range(3, n+1, 2):
#         is_prime = False
#         for prime_num in prime_nums[1:]:
#             if prime_num <= num // 2:
#                 if not num % prime_num:
#                     break
#             else:
#                 is_prime = True
#                 break
#         else:
#             is_prime = True

#         if is_prime:
#             prime_nums.append(num)
#             temp_dp = dp[-1] + num
#             if temp_dp > n:
#                 for idx in range(start_idx, len(dp)):
#                     if temp_dp - dp[idx] <= n:
#                         start_idx = idx + 1
#                         temp_dp -= dp[idx]
#                         break
#             if temp_dp == n:
#                 res += 1
#             dp.append(temp_dp)
            
#     print(res)

