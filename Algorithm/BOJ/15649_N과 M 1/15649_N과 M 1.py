import sys
input = sys.stdin.readline

## 재귀를 이용한 순열 함수이다.

def permu(arr, cnt):
    if cnt == m:
        return print(*arr)
    

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            permu(arr, cnt+1)
            arr.pop()

n, m = map(int, input().split())
permu([], 0)
