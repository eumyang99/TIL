import sys
sys.stdin = open('input.txt')


# 보이어 무어 활용
T = int(input())
for case in range(T):
    A, B = input().split()
 
    cnt = 0
    j = len(B) - 1
    
    # j인덱스가 A의 길이를 넘으면 그만
    while j <= len(A)-1:
        i = len(B) - 1
        saved_j = j
        while True:
            # 뒤에부터 비교했을 때 계속 같아져서
            if A[j] == B[i]:
                j -= 1
                i -= 1
                # i가 0보다 작아졌을 때
                # 패턴을 발견 cnt +1 하고
                # j인덱스를 패턴 다음으로 조정
                if i < 0:
                    cnt += 1
                    j = saved_j + len(B)
                    break
                     
            # 다른 부분이 발견되었다면         
            else:
                # 가정 처음 비교했던 j의 인덱스 글자가
                j = saved_j
                # 패턴 안에 몇번째 있는지 찾고
                # 그만큼 j인덱스를 조정
                for idx in range(len(B)-2, -1, -1):
                    if A[j] == B[idx]:
                        j += len(B)-1-idx
                        break
                # 패턴 안에 글자가 없다면
                # j인덱스를 패턴의 글자수 만큼 조정
                else:
                    j = saved_j + len(B)
                    break
                break
     
    result = len(A) + (1-len(B))*cnt
    print(f'#{case+1} {result}')


#     # 스플릿 활용
# T = int(input())
# for case in range(T):
#     A, B = input().split()
 
#     lst = A.split(B)
#     remain = 0
 
#     for i in lst:
#         remain += len(i)
 
#     fast = (len(A) - remain) // len(B)
#     print(f'#{case+1} {fast+remain}')