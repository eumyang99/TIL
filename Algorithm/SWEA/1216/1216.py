import sys
sys.stdin = open('input.txt')

def palindrome_x(x, L_idx, R_idx):
    if lst[x][L_idx] == lst[x][R_idx]:
        L_idx += 1
        R_idx -= 1
        if R_idx - L_idx <= 0:
            return True
        return palindrome_x(x, L_idx, R_idx)
    else :
        return False
 
def palindrome_y(y, L_idx, R_idx):
    if lst[L_idx][y] == lst[R_idx][y]:
        L_idx += 1
        R_idx -= 1
        if R_idx - L_idx <= 0:
            return True
        return palindrome_y(y, L_idx, R_idx)
    else :
        return False
  
  
t = 10
for _ in range(t):
    case = int(input())
    size = 100
    lst = []
    for _ in range(size):
        lst.append(input())
  
    max_value = 0
  
  
  
    for len in range(size, 1, -1):
        for x in range(size):
            for num in range(size-len+1):
                L_idx = num
                R_idx = len-1+num
                if palindrome_x(x, L_idx, R_idx) == True:
                    max_value = len
                    break
                if palindrome_y(x, L_idx, R_idx) == True:
                    max_value = len
                    break
            if max_value > 0:
                break
        if max_value > 0:
            break
    
    # 회문이 없을 경우 가장 긴 회문의 길이는 1이다
    if max_value == 0:
        max_value = 1


    print(f'#{case} {max_value}')