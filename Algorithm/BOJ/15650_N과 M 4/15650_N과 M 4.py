import sys
input = sys.stdin.readline

## 재귀를 이용한 중복조합 함수이다.

def combi_rep(start, arr, cnt):
    if cnt == m:
        return print(*arr)

    for i in range(start, n+1):
        arr.append(i)
        combi_rep(i, arr, cnt+1)
        arr.pop()
    
n, m = map(int, input().split())
combi_rep(1, [], 0)