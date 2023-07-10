import sys
input = sys.stdin.readline

## 발상
## 음수, 0, 1, 양수 각각의 list를 만들어서 저장 후 정렬
## 양수의 개수가 짝수일 때 모두 곱해서 더하고 홀수인 경우 가장 작은 수를 마지막에 더함
## 음수의 개수가 짝수일 때 모두 곱해서 더하고 홀수인 경우 절대값이 가장 큰 음수와 0을 곱해서 0으로 처리함
## 0이 없으면 어쩔 수 없이 그 움수를 더함
## 1은 모두 더함(1이 아닌 양수와 곱했을 때 오히려 더해지는 값이 1만큼 작아지기 때문)

n = int(input())
negative = []
zero = []
one = []
positive = []

for _ in range(n):
    num = int(input())
    if num == 0:
        zero.append(num)
    elif num == 1:
        one.append(num)
    elif num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

positive.sort()
negative.sort(reverse=True)

res = 0

## 1 처리
res += sum(one)

## 양수, 음수 처리
for arr in [positive, negative]:
    if arr:                                 # arr가 있을 때
        idx = len(arr)-1                    # idx를 마지막 원소로 잡고
        while idx > 0:                      # 최대한 많은 짝수개 만큼 묶어서 곱하고 res에 더함
            res += arr[idx] * arr[idx-1]
            idx -= 2                        # idx를 2만큼 줄여줌
                                            # 만약 arr의 개수가 짝수개였으면 위 과정에서 끝나지만
    if len(arr) % 2 == 1:                   # 홀수개 였다면
        if arr[idx] < 0 and zero:           # 음수일 경우 0과 곱한 뒤 0을 하나 지우고
            zero.pop()                      
        else:                               # 양수일 경우와 음수인데 0이 없는 경우는 res에 더함
            res += arr[idx] 

print(res)




####### 쉬운 코드 #######

# ## 양수, 음수 처리
# for arr in [positive, negative]:
#     if len(arr) > 0 and len(arr) % 2 == 0:        # 개수가 짝수일 때
#         idx = len(arr)-1
#         while idx > 0:
#             res += arr[idx] * arr[idx-1]
#             idx -= 2
#     elif len(arr) > 0 and len(arr) % 2 == 1:      # 개수가 홀수일 때
#         idx = len(arr)-1
#         while idx > 0:
#             res += arr[idx] * arr[idx-1]
#             idx -= 2
#         if arr[idx] < 0 and zero:                 # 현재 음수를 처리하는 과정이면서 음수가 한 개 남았고 남은 0이 있다면 해당 음수를 0과 곱해서 처리
#             zero.pop()
#         else:                                     # 그게 아니라면(음수 한 개가 남지 않았거나 현재 양수를 처리하는 경우)
#             res += arr[idx]                       # 그냥 더해준다

# print(res)