import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    N, Q = map(int, input().split())
    oper_info = [list(map(int, input().split())) for _ in range(Q)]

    # 빈 리스트를 만들고
    lst = [f'{0}']*N

    for i in range(Q):
        # 주어진 정보를 토대로 작업할 인덱스 범위내의 값을
        # 해당 회차의 str(i)값으로 변경
        lst[oper_info[i][0]-1:oper_info[i][1]] \
            = f'{i+1}'*(oper_info[i][1]-oper_info[i][0]+1)
    print(f'#{case+1}', end=" ")
    print(" ".join(lst))

        # TIL
        # 16번 코드줄
        # 리스트를 슬라이싱 후 그 값을 일괄 변경하려면
        # 변경할 값도 슬라이싱 개수만큼 제공해줘야 함!! ex) 슬라이싱이 [a:b]라면 b-a개


