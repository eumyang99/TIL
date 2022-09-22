import sys
sys.stdin = open('input.txt')

T = int(input())
def func():
    for x in range(len(n_2)-1, -1, -1):         # 2진수의 마지막 숫자부터 바꿈
        copy_val_2 = val_2                      # 인풋 받은 2진수의 카피본
        if n_2[x] == '0':                           # 해당 숫자가 0이면
            copy_val_2 += 2**(len(n_2)-1-x)             # 1로 바꿔서 값을 높이고
        else:                                       # 해당 숫자가 1이면
            copy_val_2 -= 2**(len(n_2)-1-x)             # 0으로 바꿔서 값을 낮춤

        for y in range(len(n_3)-1, -1, -1):         # 3진수도 차례대로 같은 방법을 함
            copy_val_3 = val_3
            target = int(n_3[y])                    # 바꿔야할 숫자
            for i in range(3):                      # 3진수니까 0, 1, 2로 바뀜
                if target != i:                     # 바꿔야할 숫자와 i가 같다면 넘기고 다르다면
                    # target이 i보다 작을 때
                    if target - i < 0:
                        # 적절한 값을 더해서 copy_val_2와 비교
                        # 같다면 출력하고 종료
                        if copy_val_3 + 3**(len(n_3)-1-y) * (i - target) == copy_val_2:
                            print(f'#{case+1} {copy_val_2}')
                            return
                    # target이 i보다 클 때        
                    else:
                        # 적절한 값을 더해서 copy_val_2와 비교
                        # 같다면 출력하고 종료
                        if copy_val_3 - 3**(len(n_3)-1-y) * (target - i) == copy_val_2:
                            print(f'#{case+1} {copy_val_2}')
                            return
for case in range(T):
    n_2 = input()
    n_3 = input()

    val_2 = 0                                   # 인풋 받은 2진수의 10진수값
    for i in range(len(n_2)-1, -1, -1):
        if n_2[i] == '1':
            val_2 += 2**(len(n_2)-1-i)
    val_3 = 0                                   # 인풋 받은 3진수의 10진수값
    for i in range(len(n_3)-1, -1, -1):
        if n_3[i] == '1':
            val_3 += 3**(len(n_3)-1-i)
        elif n_3[i] == '2':
            val_3 += 3**(len(n_3)-1-i) * 2

    func()



# T = int(input())
# for case in range(T):
#     n_2 = input()
#     n_3 = input()

#     val_2 = 0
#     for i in range(len(n_2)-1, -1, -1):
#         if n_2[i] == '1':
#             val_2 += 2**(len(n_2)-1-i)
#     val_3 = 0
#     for i in range(len(n_3)-1, -1, -1):
#         if n_3[i] == '1':
#             val_3 += 3**(len(n_3)-1-i)
#         elif n_3[i] == '2':
#             val_3 += 3**(len(n_3)-1-i) * 2

#     flag = False
#     for x in range(len(n_2)-1, -1, -1):
#         copy_val_2 = val_2
#         if n_2[x] == '0':
#             copy_val_2 += 2**(len(n_2)-1-x)
#         else:
#             copy_val_2 -= 2**(len(n_2)-1-x)

#         for y in range(len(n_3)-1, -1, -1):
#             copy_val_3 = val_3
#             target = int(n_3[y])
#             for i in range(3):
#                 if target != i:
#                     if target - i < 0:
#                         if copy_val_3 + 3**(len(n_3)-1-y) * (i - target) == copy_val_2:
#                             print(f'#{case+1} {copy_val_2}')
#                             flag = True
#                             break
                                    
#                     else:
#                         if copy_val_3 - 3**(len(n_3)-1-y) * (target - i) == copy_val_2:
#                             print(f'#{case+1} {copy_val_2}')
#                             flag = True
#                             break
#             if flag == True:
#                 break
#         if flag == True:
#             break



