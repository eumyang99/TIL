import sys
input = sys.stdin.readline

## 재귀를 이용한 조합 함수이다.

def combi(start, arr, cnt):
    if cnt == m:
        return print(*arr)

    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            combi(i, arr, cnt+1)
            arr.pop()
    
n, m = map(int, input().split())
combi(1, [], 0)