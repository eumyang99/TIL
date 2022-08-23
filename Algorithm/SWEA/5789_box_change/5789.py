import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(T):
    N, Q = map(int, input().split())
    oper_info = [list(map(int, input().split())) for _ in range(Q)]
 
 
    lst = [f'{0}']*N
    print(lst)
 
    # for i in range(Q):
    #     lst[oper_info[i][0]-1:oper_info[i][1]] = [f'{i+1}']*(oper_info[i][1]-oper_info[i][0]+1)

    # 위 for문의 슬라이싱을 2중 for문으로 변경
    for i in range(Q):
        for idx in range(oper_info[i][1]-oper_info[i][0]+1):
            lst[idx] = f'{i+1}'
 
    print(f'#{case+1}', end=" ")
    print(" ".join(lst))