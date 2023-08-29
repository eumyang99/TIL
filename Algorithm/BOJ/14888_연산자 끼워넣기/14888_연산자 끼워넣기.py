import sys
input = sys.stdin.readline

## 한참 공부해야 된다.. 진짜...
## dfs 백트래킹이다.

def cal(res, i, cnt):
    if i == 0: # +
        return res + arr[cnt]
    elif i == 1: # -
        return res - arr[cnt]
    elif i == 2: # * 
        return res * arr[cnt]
    else: # //
        temp = abs(res) // arr[cnt]
        return temp if res >= 0 else -temp

def dfs(cnt, res):
    global maxi, mini
    if cnt == n:
        maxi = max(res, maxi)
        mini = min(res, mini)
        return

    ## 부호는 4가지 이니까
    for i in range(4):
        ## 해당 부호가 여전히 남아있다면
        if operators[i]:
            ## 부호를 사용처리하고
            operators[i] -= 1
            ## 값을 계산한 뒤 다음 depth로 넘어간다
            dfs(cnt+1, cal(res, i, cnt))
            ## 사용을 다 했다면 다시 부호를 미사용 처리한다.
            operators[i] += 1

n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

maxi = -1000000001
mini = 1000000001

dfs(1, arr[0])
print(maxi)
print(mini)