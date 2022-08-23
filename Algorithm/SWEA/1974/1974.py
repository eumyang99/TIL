from pprint import pprint
import sys
sys.stdin = open('input.txt')

# 3*3 1~9 검사
def square(LU_x, LU_y):
    temp = []
    for x in range(LU_x, LU_x+3):
        for y in range(LU_y, LU_y+3):
            temp.append(lst[x][y])
    for num in range(1, 10):
        if num not in temp:
            return False

T = int(input())
for case in range(T):
    lst = [list(map(int, input().split())) for i in range(9)]

    res = True

    def test(lst):
    # square 검사
        for x in range(3):
            for y in range(3):
                if square(3*x, 3*y) == False:
                    return False

    # 가로 검사
        for i in range(9):
            for num in range(1, 10):
                if num not in lst[i]:
                    return False
    # 전치 행렬
        for x in range(9):
            for y in range(x+1, 9):
                lst[x][y], lst[y][x] = lst[y][x], lst[x][y]
    # 다시 한번 가로 검사
        for i in range(9):
            for num in range(1, 10):
                if num not in lst[i]:
                    return False

    res = test(lst)
    if res == False:
        print(f'#{case + 1} 0')
    else:
        print(f'#{case + 1} 1')


