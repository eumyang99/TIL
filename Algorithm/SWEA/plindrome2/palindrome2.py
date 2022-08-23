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

    # 가장 길이가 긴 회문 길이
    max_value = 0

    # 회문 검사할 구간 크기 100 99 98 97 ...
    for len in range(size, 1, -1):
        # 각 행or열 번호
        for x in range(size):
            # 한 행에서 반복할 횟수(구간크기 len이 100이면 1, 99이면 2...)
            for num in range(size-len+1):
                # 왼쪽 끝 인덱스, 오른쪽 끝 인덱스
                L_idx = num
                R_idx = len-1+num
                # 만약 행에서 회문이 찾아지면 회문길이 저장하고 끝냄
                if palindrome_x(x, L_idx, R_idx) == True:
                    max_value = len
                    break
                # 만약 열에서 회문이 찾아지면 회문길이 저장하고 끝냄
                if palindrome_y(x, L_idx, R_idx) == True:
                    max_value = len
                    break
            # 저장된 회문 길이가 0보다 크면 끝
            if max_value > 0:
                break
        # 저장된 회문 길이가 0보다 크면 끝
        if max_value > 0:
            break

    print(f'#{case} {max_value}')


 

#================================================================================================



    # # 각 행or열의 번호
    # for x in range(size):
    #     # 회문 검사할 구간 크기 100 99 98 97 ...
    #     for y in range(size, 1, -1):
    #         # 만약 저장된 회문 길이야 앞으로 검사할 회문 길이보다 짧다면
    #         if max_value < y:
    #             # 더 긴게 있나 계속 찾아보자
    #             for num in range(size-y+1):
    #                 L_idx = num
    #                 R_idx = y-1+num
    #                 if palindrome_x(x, L_idx, R_idx) == True:
    #                     max_value = y
    #                     break
    #                 if palindrome_y(x, L_idx, R_idx) == True:
    #                     max_value = y
    #                     break


    # print(f'#{case} {max_value}')
