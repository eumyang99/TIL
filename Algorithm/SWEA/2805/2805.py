from pprint import pprint

import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    size = int(input())
    lst = [list(map(int, input())) for i in range(size)]

    res = 0
    for i in range(size//2):                                    # 0행부터 중간 가로줄 전까지 합
        res += sum(lst[i][(size//2)-i:(size//2)+i+1])

    res += sum(lst[size//2])                                    # 중간 가로줄 총합

    for i in range(size//2):
        res += sum(lst[-1-i][(size//2)-i:(size//2)+i+1])        # 마지막 행부터 중간 가로줄 다음 행까지 합

    print(f'#{case+1} {res}')
