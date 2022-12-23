import sys
sys.stdin = open('input.txt')

# 제자리, 상 우 하 좌
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

T = int(input())
for case in range(T):
    m, a = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(a)]
    ap.sort(key= lambda x: -x[3])       # 충전을 많이 할 수 있는 순서대로 나열

    res = 0
    Ax, Ay = 1, 1 
    Bx, By = 10, 10 

    for t in range(m+1):
        Ax += dx[A[t]]      # A와 B의 위치를 계속 갱신
        Ay += dy[A[t]]
        Bx += dx[B[t]]
        By += dy[B[t]]
        A_temp = []         # 충전가능한 충전기의 인덱스를 저장
        B_temp = []
        for i in range(a):
            cx, cy, crange = ap[i][0], ap[i][1], ap[i][2]
            if abs(Ax - cx) + abs(Ay - cy) <= crange:
                A_temp.append(i)
            if abs(Bx - cx) + abs(By - cy) <= crange:
                B_temp.append(i)

        if A_temp and B_temp:                               # 둘 다 충전 가능한 경우
            if len(A_temp) == 1 and len(B_temp) == 1:           # 둘 다 하나씩만 충전가능할 경우
                if A_temp[0] == B_temp[0]:                          # 둘의 충전기가 같을 경우
                    res += ap[A_temp[0]][3]                             # 절반씩 충전
                else:                                               # 둘의 충전기가 다를 경우
                    res += ap[A_temp[0]][3]                             # 각자 충전
                    res += ap[B_temp[0]][3]
            else:                                               # 각자 1개 이상씩 충전 가능할 경우
                if A_temp[0] != B_temp[0]:                          # 가장 많이 충전할 수 있는 경우가 다를 경우
                    res += ap[A_temp[0]][3]                             # 각자 충전
                    res += ap[B_temp[0]][3]
                else:                                               # 가장 많이 충전할 수 있는 경우가 같은 경우
                    if len(A_temp) == 1:                                # A는 그곳밖에 충전할 수 없다면
                        res += ap[A_temp[0]][3]                             # A에게 가장 많은 충전을 하도록 하고
                        res += ap[B_temp[1]][3]                             # B에게 두번째로 많이 충전할 수 있는 것을 충전
                    elif len(B_temp) == 1:                              # B도 마찬가지
                        res += ap[B_temp[0]][3]
                        res += ap[A_temp[1]][3]
                    else:                                               # A, B 둘다 여러개씩 충전가능할 경우
                        if A_temp[1] <= B_temp[1]:                          # 둘의 차선책을 비교해서 차선책이 큰 쪽이 차선책을 충전
                            res += ap[B_temp[0]][3]                         # 차선책이 작은 쪽이 가장 많은 것을 충전
                            res += ap[A_temp[1]][3]
                        else:
                            res += ap[A_temp[0]][3]
                            res += ap[B_temp[1]][3]

        elif A_temp:                                            # A만 충전가능할 경우 
            res += ap[A_temp[0]][3]                             # 가장 많은 것을 충전

        elif B_temp:                                            # B만 충전가능할 경우
            res += ap[B_temp[0]][3]                             # 가장 많은 것을 충전
        

    print(f'#{case+1} {res}')

