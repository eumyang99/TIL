import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    
    for i in range(len(lst)-1, 0, -1):
        for x in range(i):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]

    print(f'#{case+1} {lst[-1]-lst[0]}')
