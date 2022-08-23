from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = 10
for case in range(T):
    size = int(input())
    lst = [list(input().split()) for i in range(size)]

# 전치 행렬
    for x in range(size):
        for y in range(x+1, size):
            lst[x][y], lst[y][x] = lst[y][x], lst[x][y]
# 교착상태 수
    res = 0

# 0은 신경쓰지 않음
# 스택이 비어있을 때만 1을 stack에 추가
# 스택에 1이 있을 때 2가 오면 pop하면서 res += 1
# 스택이 비어있을 때 2가 오면 pass
    for x in range(size):
        stack = []
        for y in range(size):
            if lst[x][y] == '1':
                if not stack:
                    stack.append(lst[x][y])
            elif lst[x][y] == '2':
                if not stack:
                    continue
                elif stack[-1] == '1':
                    stack.pop()
                    res += 1

    print(f'#{case+1} {res}')



