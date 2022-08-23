import sys
sys.stdin = open("input.txt")

t = 10
for i in range(t):
    lst_all = []
    case = int(input())
    for i in range(100):
        lst_all.append(list(map(int, input().split())))
        # 뒤에 while문의 예외사항을 없애려고 맨 왼쪽과 맨 오른쪽에 0으로 이루어진 벽을 세움
        lst_all[i].insert(0,0) # 리스트 첫번째 요소에 0을 추가
        lst_all[i].append(0) # 리스트 마지막 요소에 0을 추가



    spot_line = 0 # 현재 위치하는 사다리의 줄
    start_num_lst = [] # 시작될 수 있는 지점 리스트
    for i in range(len(lst_all)+2):
        if lst_all[0][i] == 1:
            start_num_lst.append(i)

    min_cnt = 10000 # 뒤에 for문에서 최소값을 찾기 위해 임의로 큰 숫자를 할당
    start_num = 0 # 정답일 될 시작 지점
    for i in range(len(start_num_lst)):
        # 시작될 수 있는 위치 및 현재 위치
        spot = [spot_line, start_num_lst[i]]
        # 움직일 때마다 +1할 카운트
        cnt = 0
        while spot[0] < 99: # 현재 위치하는 사다리 줄이 99가 되면 사다리 타기가 끝난 것
            if lst_all[spot[0]][spot[1]+1] == 1: # 만약 현재 위치의 오른쪽에 1이 있다면
                while lst_all[spot[0]][spot[1]+1] == 1: # 오른쪽 위치에 1이 없을 때까지
                    spot = [spot[0], spot[1]+1] # 오른쪽으로 이동
                    cnt += 1
                else:
                    spot = [spot[0]+1, spot[1]] # 다 이동했다면 아래 줄로 이동
                    cnt += 1

            elif lst_all[spot[0]][spot[1]-1] == 1: # 만약 현재 위치의 왼쪽에 1이 있다면
                while lst_all[spot[0]][spot[1]-1] == 1: # 왼쪽 위치에 1이 없을 때까지
                    spot = [spot[0], spot[1]-1] # 왼쪽으로 이동
                    cnt += 1
                else:
                    spot = [spot[0]+1, spot[1]] # 다 이동했다면 아래 줄로 이동
                    cnt += 1
                
            else:
                spot = [spot[0]+1, spot[1]] # 현재 위치의 양쪽에 1이 없다면 아래 줄로 이동
                cnt += 1
        # 만약 카운트가 min_cnt보다 작다면
        # 그것을 새로운 min_cnt로 하고
        # start_num에 시작 지점 할당
        if min_cnt > cnt:
            min_cnt = cnt
            start_num = start_num_lst[i]
    print(f'#{case} {start_num-1}') # 맨 왼쪽에 세운 벽을 감안해서 -1을 함

