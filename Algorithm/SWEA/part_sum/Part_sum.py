import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_lst = [0]*(len(lst)-(m-1))
    for i in range(len(lst)-(m-1)):
        for x in range(m):
            sum_lst[i] += lst[i+x]


    for i in range(len(sum_lst)-1,0,-1):
        for x in range(0, i):
            if sum_lst[x] > sum_lst[x+1]:
                sum_lst[x], sum_lst[x+1] = sum_lst[x+1], sum_lst[x]


    print(f'#{case+1} {sum_lst[-1]-sum_lst[0]}')