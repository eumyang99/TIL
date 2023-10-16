import sys
input = sys.stdin.readline

## 풀이 참조
## 비트마스크를 이용한 dp

import sys
input = sys.stdin.readline

def uu(x, visited):
    if visited == (1 << n) - 1:
        if arr[x][0]:
            return arr[x][0]
        else:
            return float("inf")
    
    if dp[x][visited] != -1:
        print(x, "0"*(5 - (len(str(bin(visited)))-2)) + str(bin(visited))[2:])
        return dp[x][visited]
    
    mini = float("inf")
    for i in range(1, n):
        if not arr[x][i]:
            continue
        
        if visited & (1 << i):
            continue

        mini = min(mini, uu(i, visited | (1 << i)) + arr[x][i])
        dp[x][visited] = mini
    return mini

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]
print(uu(0, 1))
