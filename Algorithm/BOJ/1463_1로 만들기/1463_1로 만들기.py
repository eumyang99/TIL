from collections import deque
import sys
input = sys.stdin.readline

## DP를 활용해서 푼다

def DP(n):
    if n in memo:
        return memo[n]
    if n % 6 == 0:
        memo[n] = min(DP(n//3)+1, DP(n//2)+1)
    elif n % 3 == 0:
        memo[n] = min(DP(n//3)+1, DP(n-1)+1)
    elif n % 2 == 0:
        memo[n] = min(DP(n//2)+1, DP(n-1)+1)
    else:
        memo[n] = DP(n-1)+1
    return memo[n]
n = int(input())
memo = {1:0, 2:1}
print(DP(n))



## 이 방법은 DP를 전혀 사용하지 않은 BFS 방법이다

# n = int(input())
# cnt = 1
# if n == 1:
#     print(0)
# elif n > 3:
#     que = deque()
#     if n % 3 == 0:
#         que.append((cnt, n // 3))
#     if n % 2 == 0:
#         que.append((cnt, n // 2))
#     que.append((cnt, n - 1))

#     while que:
#         cnt, num = que.popleft()
#         if num <= 3:
#             print(cnt+1)
#             break
#         else:
#             if num % 3 == 0:
#                 que.append((cnt+1, num // 3))
#             if num % 2 == 0:
#                 que.append((cnt+1, num // 2))
#             que.append((cnt+1, num - 1))
# else:
#     print(1)
