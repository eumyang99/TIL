import sys
input = sys.stdin.readline

## 중복조합 문제!

def facto(num, cnt, target):
    if cnt == target:
        return num
    if num == 1:
        return num
    
    return num * facto(num-1, cnt+1, target)

n, k = map(int, input().split())
a = n + k - 1
b = min(n, a - n)
if b == 0:
    print(1)
else:
    res = facto(a, 1, b) // facto(b, 1, b)
    print(res % 1000000000)
