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

    lst_all.reverse() # 도착 지점부터 시작 지점으로 거꾸로 타고 가려고 편의상 리스트 역배열
    start_num = lst_all[0].index(2) # 시작지점이 된 '2'의 인덱스
    spot_line = 0 # 현재 위치하는 사다리의 가로줄
    spot = [spot_line, start_num] # 현재 위치
   
    while spot[0] < 99: # 현재 위치하는 사다리 줄이 99가 되면 사다리 타기가 끝난 것
        if lst_all[spot[0]][spot[1]+1] == 1: # 만약 현재 위치의 오른쪽에 1이 있다면
            while lst_all[spot[0]][spot[1]+1] == 1: # 오른쪽 위치에 1이 없을 때까지
                spot = [spot[0], spot[1]+1] # 오른쪽으로 이동
            else:
                spot = [spot[0]+1, spot[1]] # 다 이동했다면 아래 줄로 이동

        elif lst_all[spot[0]][spot[1]-1] == 1: # 만약 현재 위치의 왼쪽에 1이 있다면
            while lst_all[spot[0]][spot[1]-1] == 1: # 왼쪽 위치에 1이 없을 때까지
                spot = [spot[0], spot[1]-1] # 왼쪽으로 이동
            else:
                spot = [spot[0]+1, spot[1]] # 다 이동했다면 아래 줄로 이동
            
        else:
            spot = [spot[0]+1, spot[1]] # 현재 위치의 양쪽에 1이 없다면 아래 줄로 이동

    print(f'#{case} {spot[1]-1}') # 맨 왼쪽에 세운 벽을 감안해서 -1을 함