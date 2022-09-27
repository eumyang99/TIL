import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    print(n)
    print(lst)
    print(f'#{case+1} {lst[n//2]}')
    print()