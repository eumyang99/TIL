from pprint import pp, pprint
import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    lst = [[0]*10 for _ in range(10)]
    N = int(input())

    # 빨간색(1)위에 파란색을 색칠하거나
    # 파란색(2)위에 빨간색이 색칠되는 경우
    # cnt += 1
    cnt = 0
    for i in range(N):

        # 주어지는 좌표 및 색깔 정보를 리스트로 받고
        info = list(map(int, input().split()))
        # 리스트에 마지막 원소가 1(빨간색)이면
        if info[-1] == 1:
            # 첫번째 행 좌표에서 두번째 행 좌표까지 반복
            for r in range(info[0], info[2]+1):
                # 위 r에 해당하는 행에 첫번째 열 좌표부터 두번째 열 좌표까지 색칠을 하는데
                for c in range(info[1], info[3]+1):
                    # 만약 그 자리에 이미 2(파란색)이 있으면
                    if lst[r][c] == 2:
                        # 3(보라색)을 칠하고
                        lst[r][c] = 3
                        # 보라색 카운트 +1
                        cnt += 1
                    # 그렇지 않고 0(비어있으면)
                    elif lst[r][c] == 0:
                        # 그 자리에 1(빨간색) 칠함
                        lst[r][c] = 1
        # 리스트에 마지막 원소가 2(파란색)이면               
        elif info[-1] == 2:
            # 첫번째 행 좌표에서 두번째 행 좌표까지 반복
            for r in range(info[0], info[2]+1):
                # 위 r에 해당하는 행에 첫번째 열 좌표부터 두번째 열 좌표까지 색칠을 하는데
                for c in range(info[1], info[3]+1):
                    # 만약 그 자리에 이미 1(빨간색)이 있으면
                    if lst[r][c] == 1:
                        # 3(보라색)을 칠하고
                        lst[r][c] = 3
                        # 보라색 카운트 +1
                        cnt += 1
                    # 그렇지 않고 0(비어있으면)
                    elif lst[r][c] == 0:
                        # 그 자리에 2(파란색) 칠함
                        lst[r][c] = 2

    print(f'#{case+1} {cnt}')


