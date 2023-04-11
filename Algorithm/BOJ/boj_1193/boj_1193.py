import sys
input = sys.stdin.readline

a = int(input())

n = 1
while 1:
    if (n*(n+1) // 2) >= a:
        break
    n += 1

idx = (n*(n+1) // 2) - a +1

if n % 2:
    print(f'{idx}/{n+1-idx}')
else:
    print(f'{n+1-idx}/{idx}')
