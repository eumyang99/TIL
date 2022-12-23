import sys
input = sys.stdin.readline

n = int(input())

if n < 10:
    n *= 10

cnt = 0
d = n
while 1:
    a = d//10
    b = d%10
    c = a+b

    d = b*10 + c%10
    cnt += 1
    if d == n:
        break

print(cnt)
