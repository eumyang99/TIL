import sys
sys.stdin= open("input.txt")

# 스플릿 활용
T = int(input())
for case in range(T):
    A, B = input().split()

    lst = A.split(B)
    print(lst)

    remain = 0
    for i in lst:
        remain += len(i)
    print(remain)

    fast = (len(A) - remain) // len(B)
    print(f'#{case+1} {fast+remain}')

    print()


# 보이어-무어 활용 풀이
    # cnt = 0
    # j = len(B) - 1

    # while j <= len(A)-1:
    #     i = len(B) - 1
    #     saved_j = j
    #     while True:
    #         if A[j] == B[i]:
    #             j -= 1
    #             i -= 1
    #             if i < 0:
    #                 cnt += 1
    #                 j = saved_j + len(B)
    #                 break
                    
                    
    #         else:
    #             j = saved_j
    #             for idx in range(len(B)-2, -1, -1):
    #                 if A[j] == B[idx]:
    #                     j += len(B)-1-idx
    #                     break
    #             else:
    #                 j = saved_j + len(B)
    #                 break
    #             break
    
    # result = len(A) + (1-len(B))*cnt
    # print(f'#{case+1} {result}')