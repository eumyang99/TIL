import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    for i in range(n):
        if not m & (1<<i):
            print(f'#{case+1} OFF')
            break
    else:
        print(f'#{case+1} ON')

        

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    for i in range(n):
        if m % 2 == 0:
            print(f'#{case+1} OFF')
            break
        else:
            m //= 2
    else:
        print(f'#{case+1} ON')