import sys
input = sys.stdin.readline

## 타겟 a가 홀수의 경우
    ## a-1, a+1 의 가중치 중 작은 것 + 1
## 짝수인 경우
    ## a-1의 가중치 + 1, a // 2 의 가중치 중 작은 것

n, k = map(int, input().split())

if k <= n:
    print(n-k)
else:
    lst = [0] * (k+2)
    for i in range(k+1):
        if i <= n:
            lst[i] = n-i
        else:
            if i % 2: # 홀수
                lst[i] = min(lst[i-1], lst[i+1]) + 1
            else: # 짝수
                lst[i] = min(lst[i-1] + 1, lst[i // 2])
        if i*2 <= k+1:
            lst[i*2] = lst[i]

    print(lst[k])