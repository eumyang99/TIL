import sys
sys.stdin = open('input.txt')

# 가로 글자의 회문을 검증하는 함수
    # 리스트의 행과 비교할 양쪽 끝 인덱스를 입력했을 때
    # 만약 양쪽 끝의 글자가 같으면 왼쪽 인덱스 +1. 오른쪽 인덱스 -1을 하고 다시 함수로 입력
    # 양쪽 끝의 글자가 같지 않다면 False 반환
    # 함수를 반복했을 때 양쪽 끝의 인덱스가 같아지거나 역전될 경우 회문으로 판정하고 True 반환
def palindrome_x(x, L_idx, R_idx):
    if lst[x][L_idx] == lst[x][R_idx]:
        L_idx += 1
        R_idx -= 1
        if R_idx - L_idx <= 0:
            return True
        return palindrome_x(x, L_idx, R_idx)
    else :
        return False

# 세로 글자의 회문을 검증하는 함수
    # 가로 글자의 경우와 같은 원리
def palindrome_y(y, U_idx, D_idx):
    if lst[U_idx][y] == lst[D_idx][y]:
        U_idx += 1
        D_idx -= 1
        if D_idx - U_idx <= 0:
            return True
        return palindrome_y(y, U_idx, D_idx)
    else :
        return False

T = 10
for case in range(T):
    n = int(input())
    size = 8
    lst = []
    for _ in range(size):
        lst.append(input())

    # 회문이 맞을 경우 cnt+1
    cnt = 0
    # 주어지는 n에 따라 회문 판정할 범위를 설정
    # if문이 끝나면 양쪽 끝의 인덱스를 +1 해서 다시 검증 반복

    # 가로 글자 검증
    for x in range(size): 
        for y in range(8-n+1):
            L_idx = y
            R_idx = y+n-1
            if palindrome_x(x, L_idx, R_idx) == True:
                cnt += 1

    # 세로 글자 검증
    for y in range(size):
        for x in range(8-n+1):
            U_idx = x
            D_idx = x+n-1
            if palindrome_y(y, U_idx, D_idx) == True:
                cnt += 1

    print(f'#{case+1} {cnt}')

    
#==============================================================================================================


T = 10
for case in range(T):
    n = int(input())
    size = 8
    lst = []
    for _ in range(size):
        lst.append(input())


    cnt = 0
    # 가로 글자 검증
    for x in range(size): 
        for y in range(8-n+1):
            L_idx = y
            R_idx = y+n-1
            while True:
                if lst[x][L_idx] == lst[x][R_idx]:
                    L_idx += 1
                    R_idx -= 1
                else :
                    break
                if R_idx - L_idx <= 0:
                    cnt += 1
                    break

    # 세로 글자 검증
    for y in range(size):
        for x in range(8-n+1):
            U_idx = x
            D_idx = x+n-1
            while True:
                if lst[U_idx][y] == lst[D_idx][y]:
                    U_idx += 1
                    D_idx -= 1
                else : 
                    break
                if D_idx - U_idx <= 0:
                    cnt += 1
                    break

    print(f'#{case+1} {cnt}')
