import sys
sys.stdin = open('input.txt')


# 가로줄 회문을 검사하는 함수
def palindrome_x(x, L_idx, R_idx):
    if lst[x][L_idx] == lst[x][R_idx]:
        L_idx += 1
        R_idx -= 1
        if R_idx - L_idx <= 0:
            return True
        return palindrome_x(x, L_idx, R_idx)
    else:
        return False
 
# 세로줄 회문을 검사하는 함수
def palindrome_y(y, U_idx, D_idx):
    if lst[U_idx][y] == lst[D_idx][y]:
        U_idx += 1
        D_idx -= 1
        if D_idx - U_idx <= 0:
            return True
        return palindrome_y(y, U_idx, D_idx)
    else:
        return False
 
 
 
T = int(input())
for case in range(T):
    size, lenth = map(int, input().split())
 
    # 글자표를 리스트에 담음
    lst = [0]*size
    for x in range(size):
        lst[x] = list(input())
 
    result = ''
    # 0~99까지 하나씩 꺼내 x에 담고
    for x in range(size):
        # 한 줄에서 검사할 글자 크기에 따라 달라지는 검사회수
        # 검사할 글자의 가장 작은 인덱스를 담는 i
        for i in range(size-lenth+1):
            # 검사할 글자의 가장 작은 인덱스와 가장 큰 인덱스
            L_idx = i
            R_idx = lenth-1+i
            # 만약 가로줄에서 회문이 찾아졌다면
            if palindrome_x(x, L_idx, R_idx) == True:
                # result에 글자를 담고 그만
                for p in range(L_idx, R_idx+1):
                    result += lst[x][p]
                break
            # 세로줄에서 회문이 찾아졌다면
            elif palindrome_y(x, L_idx, R_idx) == True:
                # result에 글자를 담고 그만
                for p in range(L_idx, R_idx+1):
                    result += lst[p][x]
                break
        # 현재 result에 글자가 담겨있다면 그만
        if len(result) > 0:
            break
    print(f'#{case+1} {result}')