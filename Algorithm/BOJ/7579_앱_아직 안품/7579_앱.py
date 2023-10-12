import sys
input = sys.stdin.readline

## 풀이 참고
## 배낭 문제 개념 활용
## 배낭의 크기를 메모리가 아니라 비용으로 잡고 해야 한다

## 본질 1
## 앱을 순회하며
## 현재 순회한 앱까지 확인해 봤을 때,
## dp의 idx에 해당하는 비용으로 확보할 수 있는 가장 큰 메모리를 할당

## 핵심 로직
## 만약 현재 앱의 비용이 4이고 메모리가 10이면
## 비용 10의 dp값 = (비용 6인 dp값 + 현재 앱의 메모리 10) 과 (비용 10의 dp값 중 큰 것)으로 갱신해 나감

n, m = map(int, input().split())
memory_arr = list(map(int, input().split())) 
cost_arr = list(map(int, input().split()))

## 배낭 생성
dp_len = sum(cost_arr) + 1
dp = [0] * dp_len

## 첫번째 앱부터 마지막 앱까지 순회하며
for i in range(n):
    memory = memory_arr[i]
    cost = cost_arr[i]

    ## dp의 마지막 idx부터 갱신해 나감
    ## 작은 dp값부터 갱신하면 뒤의 값을 갱신할 때 이전 앱의 결과를 참고할 수 없음
    ## 현재 앱이 반영된 값으로 갱신된 값을 참고하게 되기 때문에
    ## 따라서 마지막 idx 갱신하면서 이전 값의 오염을 방지함 
    for cost_dp in range(dp_len-1, cost-1, -1):
        ## 현재 앱의 비용보다 dp idx가 작으면 현재 앱은 영향을 미칠 수 없기 때문에
        ## 이전 값을 바꾸지 않음
        if cost_dp < cost:
            continue

        ## 현재 앱의 비용보다 dp idx가 큰 경우
        ## (기존 dp값) 과 (dp[cost_dp - cost] + 현재 앱의 메모리) 중 큰 값으로 갱신
        ## 위의 핵심 로직 참고
        else:
            dp[cost_dp] = max(dp[cost_dp - cost] + memory, dp[cost_dp])


## 처음으로 필요한 메모리를 확보한 idx(비용)를 출력
## dp 최대 길이가 10000이라서 두 방법 다 속도 차이는 안남 
## 이분탐색으로 찾기
left, right = 0, dp_len-1
while left <= right:
    mid = (left + right) // 2
    if dp[mid] < m:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(left)

## 그냥 for문으로 찾기
# for i in range(dp_len):
#     if dp[i] >= m:
#         print(i)
#         break
