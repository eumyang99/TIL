import sys
input = sys.stdin.readline

def uu(cnt, idx, accu): ## 비용, 자리수, 누적값
    global res
    
    limit_idx = int(n[idx]) # 누적값과 n을 비교하여 초과하지 않는 limit_idx 까지만 탐색
    start_idx = int(x[idx]) # num_change[start_idx] 변경 비용을 탐색
    able_num_size = int(n) // (10**(k-idx)) # 앞자리의 수부터 가능한 숫자

    if idx == k-1: ## base case, 1의 자리에 도착했을 때
        ## (10 if accu < able_num_size else limit_idx + 1) 이 부분은 아래 주석 참고
        for i in range(10 if accu < able_num_size else limit_idx + 1):
            ## accu가 0일 때는 앞의 모든 숫자가 0이다
            ## 따라서 이런 경우 결과가 항상 1보다 커야하니 마지막 숫자가 0이면 안된다.
            if accu == 0 and i == 0:
                continue
            ## i를 마지막 숫자로 추가할 수 있는 비용이 있다면 가능한 경우의 수이기 때문에 res에 1을 추가한다
            if num_change[start_idx][i] <= cnt:
                res += 1
        
        ## base case에 도달했으니 return
        return

    ## 누적값이 가능한 숫자보다 작다면
    ## ex) accu = 31, able_num_size = 33 일 때 33x에서 x에는 모든 숫자가 들어갈 수 있다.
    ## 하지만 accu == 31, able_num_size == 31일 때 33x에 올 숫자는 n의 해당 자리수 보다 크면 안된다.
    ## 따라서 이런 경우 해당 자리 숫자인 limit_idx 까지만 탐색해야 한다.
    for i in range(10 if accu < able_num_size else limit_idx + 1):
        ## 만약 start_idx에서 i로 숫자를 변경할 때 드는 비용이 현재 남은 cnt보다 작다면
        if num_change[start_idx][i] <= cnt:
            ## next_accu로 누적값을 갱신하고
            next_accu = accu*10 + i
            ## cnt를 변경 비용만큼 차감, idx + 1, next_accu를 인자로 재귀를 돌린다.
            uu(cnt - num_change[start_idx][i], idx + 1, next_accu)


## n = 가능한 최대값
## k = 자리수
## p = 사용가능한 비용
## x = 시작값
n, k, p, x = map(int, input().split())
## num_change[a][b]는 a 숫자에서 b 숫자로 변경할 때 드는 비용
num_change = [
                [0,4,3,3,4,3,2,3,1,2], [4,0,5,3,2,5,6,1,5,4], [3,5,0,2,5,4,3,4,2,3], \
                [3,3,2,0,3,2,3,2,2,1], [4,2,5,3,0,3,4,3,3,2], [3,5,4,2,3,0,1,4,2,1], \
                [2,6,3,3,4,1,0,5,1,2], [3,1,4,2,3,4,5,0,4,3], [1,5,2,2,3,2,1,4,0,1], \
                [2,4,3,1,2,1,2,3,1,0]
              ]

## k 자리수에 맞게 0을 포함한 숫자
n, x = str(n), str(x)
n, x = '0'*(k-len(n)) + n, '0'*(k-len(x)) + x
res = 0
uu(p, 0, 0)

print(res - 1)
