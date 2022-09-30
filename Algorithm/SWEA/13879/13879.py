import sys
sys.stdin = open('input.txt')

def divide(lst):
    if len(lst) <= 1:           # 길이가 1 이하인 리스트는
        return lst              # 리스트 반환
    
    i = 1 - 1
    j = len(lst) - 1
    
    m = (i+j)//2 +1             # 중간 값

    L = divide(lst[:m])         # 왼쪽 리스트를 다시 divide에 넣고
    R = divide(lst[m:])         # 오른쪽 리스트를 다시 divide에 넣고

    return vs(L, R)             # 가위바위보 대결 함수로


def vs(L, R):
    # 1 = 가위
    # 2 = 바위
    # 3 = 보
    if L and not R:             # 왼쪽 리스트는 있고 오른쪽 리스트는 없으면
        return L                # L 부전승
    elif R and not L:           # 반대도 상동
        return R
    
    value = L[0][0] - R[0][0]       # value = 가위바위보 대결의 결과값
    if value == -1 or value == 2:   # value가 -1 이거나 2이면 R 승리
        winner = R
    elif value == 1 or value == -2: # value가 1 이거나 -2이면 L 승리
        winner = L
    elif value == 0:                # 비겼으면 L 승리
        winner = L  
    
    return winner                   # 승리자 반환

T = int(input())
for case in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(n):
        lst[i] = (lst[i], i+1)              # 리스트에 (가위바위보 값, 학생번호) 저장

    print(f'#{case+1} {divide(lst)[0][1]}') # 승자의 번호 출력




