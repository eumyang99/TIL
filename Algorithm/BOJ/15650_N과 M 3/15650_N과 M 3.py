import sys
input = sys.stdin.readline

## 재귀를 이용한 중복순열 함수이다.

def permu_rep(arr, cnt):
    if cnt == m:
        return print(*arr)

    for i in range(1, n+1):
        arr.append(i)
        permu_rep(arr, cnt+1)
        arr.pop()

n, m = map(int, input().split())
permu_rep([], 0)