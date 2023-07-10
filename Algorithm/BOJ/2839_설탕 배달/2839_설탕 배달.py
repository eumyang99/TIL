import sys
input = sys.stdin.readline

n = int(input())
res = 0 

while n >= 0:
    if n % 5 == 0:
        res += (n // 5)
        n = 0
        break
    n -= 3
    res += 1

if n == 0:
    print(res)
else:
    print(-1)
