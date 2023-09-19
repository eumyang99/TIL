import sys
input = sys.stdin.readline

## 인덱스 문제 어려워 ㅠㅠㅠ
## 발상
## 부분합의 시작 인덱스를 기록하면서 끝 인덱스를 키워 나간다
## 만약 부분합이 목표보다 크다면
## 시작 인덱스의 값을 빼도 되는지 확인하고 가능하다면 뺀다.
## 그리고 시작 인덱스를 높인다.
## 부분합이 목표값 이상이 되는 조건 하에 최대한 시작 인덱스를 높인다.
## 이후 그 부분합의 길이를 계산한다.

def uu(n, s, arr):
    ## 부분합
    part_sum = 0
    ## 출력할 값
    res = 100001
    ## 시작 인덱스
    start_idx = 0
    ## arr전체를 순회하며
    for i in range(n):
        ## temp는 이전까지의 부분합 + 이번 숫자
        temp = part_sum + arr[i]
        ## 이번 숫자를 더했을 때 만약 시작 인덱스의 값을 빼도 목표값 이상이라면 최대한 뺀다.
        while temp - arr[start_idx] >= s:
            ## temp에서 시작 인덱스의 값을 빼고
            temp -= arr[start_idx]
            ## 시작 인덱스를 높인다.
            start_idx += 1
        ## 뺄 만큼 최대한 뺐을 때 부분합이 목표값 이상이라면 res를 갱신
        if temp >= s:
            res = min(res, i - start_idx + 1)
        ## 그리고 이번 숫자까지의 가능한 부분합을 기록한다.
        ## 가능하지 않다면 부분합에 점점 추가될 것이다.
        part_sum = temp
    ## 부분합이 한번도 목표값 이상인적이 없다면 여전히 100001일 것.
    ## 따라서 그런 경우 0을 출력한다.
    return print(0 if res == 100001 else res)

n, s = map(int, input().split())
arr = tuple(map(int, input().split()))
uu(n, s, arr)



