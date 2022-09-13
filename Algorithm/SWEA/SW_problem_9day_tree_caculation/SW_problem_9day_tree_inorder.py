# 중위 탐색

import sys
sys.stdin = open('input.txt')


def func(node):
    if len(node) == 2:
        return(int(node[1]))
    elif len(node) == 4:
        L = int(node[2])
        R = int(node[3])
        if node[1] == '+':
            return func(lst[L]) + func(lst[R])
        elif node[1] == '-':
            return func(lst[L]) - func(lst[R])
        elif node[1] == '*':
            return func(lst[L]) * func(lst[R])       
        elif node[1] == '/':
            return func(lst[L]) // func(lst[R]) 
    


T = 10
for case in range(10):
    n = int(input())
    lst = [0]
    for _ in range(n):
        lst.append(input().split())

    print(f'#{case+1} {func(lst[1])}')

    

