import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    total = 0
    for coin, cnt in arr:
        total += coin * cnt
    
    if total % 2:
        return 0
    
    target = total // 2
    memo = [0] * (target+1)
    memo[0] = 1
    for coin, cnt in arr:
        for val in range(target, -1, -1):
            if memo[val]:
                for i in range(1, cnt+1):
                    new_val = val + coin * i
                    if new_val <= target:
                        memo[new_val] = 1
                    else:
                        break
                    
        if memo[target]:
            return 1
    return 0
    

CASE = 3
for _ in range(CASE):
    print(solution())