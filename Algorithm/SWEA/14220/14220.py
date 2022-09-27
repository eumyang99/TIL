import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    if len(lst) <= 1:                               # 계속 절반씩 분할하다가 길이가 1이 되면
        return lst                                  # 해당 리스트 반환

    m = len(lst) // 2                               # m(중간 idx)은 리스트 길이의 // 2

    L, R = merge_sort(lst[:m]), merge_sort(lst[m:]) # L은 절반 왼쪽 리스트를 merge_sort에 넣은 값
                                                    # R은 절반 오른쪽 리스트를 merge_sort에 넣은 값   
    # merge_sort의 return 값은 merge의 리턴값이다
    # merge의 리턴값은 리스트이므로 merge_sort의 리턴값도 리스트이다
    # 따라서 L, R도 리스트이다

    return merge(L, R)                              # 리스트 L과 리스트 R을 merge에 넣음

def merge(L, R):                    
    global cnt                                      
    if L[-1] > R[-1]:                               # 왼쪽의 마지막 값과 오른쪽의 마지막 값을 비교해서
        cnt += 1                                    # cnt +1
    
    res = []                                        # 리턴할 빈 리스트
    LP, RP = 0, 0                                   # 인덱스 포인트

    while LP < len(L) and RP < len(R):              # 두 인덱스 포인트가 L과 R의 길이보다 작다면
        if L[LP] < R[RP]:                           # 왼쪽의 해당 인덱스의 항목과 오른쪽의 해당 인덱스 항목을 비교
            res.append(L[LP])                       # res에 추가하고
            LP += 1                                 # idx 조정
        else:
            res.append(R[RP])
            RP += 1
    
    res.extend(L[LP:])                              # 왼쪽과 오른쪽 중 모든 숫자를 사용했다면
    res.extend(R[RP:])                              # 남은 녀석을 res에 추가
                                                    # 이미 정렬된 상태로 주어지기 때문에 그냥 붙여도 됨

    return res                                      # 정렬된 res 리턴

T = int(input())
for case in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    cnt = 0                                         # 왼쪽 파트의 마지막 값이 
                                                    # 왼쪽 파트의 마지막 값보다 크면 cnt +1

    sorted_lst = merge_sort(lst)                    # 리스트를 merge_sort하고
    print(f'#{case+1} {sorted_lst[n//2]} {cnt}')    # 값 출력