import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m, k = map(int, input().split())
    situation = dict()
    for i in range(k):
        x, y, size, direction = map(int, input().split())       # 현재 분포 상황을 기록하는 situation은
        situation[(x, y)] = [[size, direction]]                 # (x,y)를 key로, 규모와 방향을 value로 저장한다

# 상 하 좌 우
# 1  2  3  4

    cnt = 0                                                     # cnt는 시간을 기록
    while cnt < m:                                              # 주어진 시간 동안
        next_situation = dict()                                 # 다음 상황을 기록하는 next_situation
        for location, info in situation.items():                # 현재 상황의 key와 value를 꺼내서

            if info[0][1] == 1:                                 # 해당 군집의 방향이 1(상)이면
                next_location = (location[0]-1, location[1])    # 해당 군집의 다음 위치를 next_location에 저장
                if location[0]-1 == 0:                          # 벽에 닿았다면
                    info[0][0] //= 2                            # 군집 규모를 절반으로, 방향을 반대로 설정
                    info[0][1] = 2
                if next_location not in next_situation:         # next_situation에 해당 위치에 군집이 기록되어 있지 않으면
                    next_situation[next_location] = info        # 기록
                else:                                                                           # 해당 위치에 군집이 있으면
                    next_situation[next_location] =  next_situation[next_location] + info       # value값에 추가
            
            elif info[0][1] == 2:                               # 상동
                next_location = (location[0]+1, location[1])
                if location[0]+1 == n-1:
                    info[0][0] //= 2  
                    info[0][1] = 1              
                if next_location not in next_situation:
                    next_situation[next_location] = info
                else:
                    next_situation[next_location] =  next_situation[next_location] + info           
            
            elif info[0][1] == 3:                               # 상동
                next_location = (location[0], location[1]-1)
                if location[1]-1 == 0:
                    info[0][0] //= 2
                    info[0][1] = 4
                if next_location not in next_situation:
                    next_situation[next_location] = info
                else:
                    next_situation[next_location] =  next_situation[next_location] + info
            
            elif info[0][1] == 4:                               # 상동
                next_location = (location[0], location[1]+1)
                if location[1]+1 == n-1:
                    info[0][0] //= 2
                    info[0][1] = 3
                if next_location not in next_situation:
                    next_situation[next_location] = info
                else:
                    next_situation[next_location] =  next_situation[next_location] + info


        for location, infos in next_situation.items():              # 각 위치의 군집을 꺼내서
            if len(infos) > 1:                                      # 군집이 1개 이상이라면
                total_size = 0
                biggest_size = infos[0][0]
                direction = infos[0][1]
                for value in infos:                                     
                    total_size += value[0]
                    if biggest_size < value[0]:
                        biggest_size = value[0]
                        direction = value[1]
                next_situation[location] = [[total_size, direction]]    # 군집의 규모를 합치고
                                                                        # 방향은 가장 규모가 큰 녀석으로 저장
        situation = next_situation              # 현재 상황을 갱신 situation에
        cnt += 1                                # 시간 누적

    res = 0                             
    for size in situation.values():             # 남아있는 모든 군집의 규모를 합쳐서
        res += size[0][0]
    print(f'#{case+1} {res}')                   # 출력
    





