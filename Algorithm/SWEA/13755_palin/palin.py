import sys
sys.stdin = open("input.txt")

def palindrome_x(x, L_idx, R_idx):
    if lst[x][L_idx] == lst[x][R_idx]:
        L_idx += 1
        R_idx -= 1
        if R_idx - L_idx <= 0:
            return True
        return palindrome_x(x, L_idx, R_idx)
    else:
        return False


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

    lst = [0]*size
    for x in range(size):
        lst[x] = list(input())

    for x in range(size):
        for i in range(size-lenth+1):
            L_idx = i
            R_idx = lenth-1+i
            if palindrome_x(x, L_idx, R_idx) == True:
                print(f'#{case+1}', end=" ")
                for p in range(L_idx, R_idx+1):
                    print(lst[x][p], end="")

            if palindrome_y(x, L_idx, R_idx) == True:
                print(f'#{case+1}', end=" ")
                for p in range(L_idx, R_idx+1):
                    print(lst[p][x], end="")
    print()

