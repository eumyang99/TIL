# 정사각형의 범위 안에 들어오는 값들을 모두 더하는 힘수
# arg는 정사각형의 왼쪽위 꼭지점 좌표(L, U)와 정사각형의 사이즈
def square_sum(L, U, size):
    result = 0
    for h in range(size):
        for v in range(size):
            result += lst[L+h][U+v]
    return result
 
T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(N)]
    
    # 정사각형 내부 숫자의 합의 최대값 max
    max = 0
    # 5x5 사각형의 3x3망치라면
    # 망치의 왼쪽위 꼭지점의 x좌표가 될 수 있는 것은
    # 0 1 2 = range(5-3+1)
    for x in range(N-M+1):
        for y in range(N-M+1):
            temp = square_sum(x, y, M)
            if temp > max:
                max = temp
 
    print(f'#{case+1} {max}')