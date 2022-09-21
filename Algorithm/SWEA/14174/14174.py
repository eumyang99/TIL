import sys
sys.stdin = open('input.txt')


def permu(idx , r, temp, accu):             # idx는 temp에 있는 요소 개수
    global res                              # r은 temp가 채워야할 개수 
                                            # temp는 경로를 담을 리스트
                                            # accu는 현재까지 도착한 경로의 누적합

    if idx == r:                            # temp가 꽉 찼으면
        last_arrive = temp[-1]                  # last_arrive는 마지막 관리구역
        go_office = lst[last_arrive-1][0]       # go_office는 사무실로 돌아오는 에너지

        accu += go_office                       # 마지막 관리구역에서 사무실로 돌아오는
                                                # 에너지를 누적된 에너지에 더함

        if accu < res:                          # 만약 누적값이 res보다 작다면
            res = accu                          # res 갱신

        accu -= go_office                   # 사무실로 돌아오는데 더했던 값을 다시 차감 후
        return                              # 리턴
    

    start = temp[-1]                        # start = 현재까지 도착한 지점
    for i in range(2, n+1):                 # 시작이 사무실이기 때문에 2부터 n까지 순회
        if i not in temp:                       # i가 temp에 없다면
            temp.append(i)                      # temp에 추가
            arrive = temp[-1]                   # arrive = 방금 도착한 지점
            energy = lst[start-1][arrive-1]     # energy = 방금 소모한 에너지
            accu += energy                      # 누적합에 energy 더함
            
            if accu > res:                          # 만약 temp를 채우기 전에 누적합이 res보다 크다면
                temp.pop()                          # 다시 pop하고
                accu -= energy                      # 누적합 차감 후
                continue                            # 대안 경로 모색

            permu(idx+1, r, temp, accu)         # 다음 관리구역 정하러 고고

            temp.pop()                          # temp가 다 꽉찼으니 pop하고
            accu -= energy                      # 마지막으로 더해진 누적값 차감



T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]


    res = 999999999999999

    permu(1, n, [1], 0)         # 1부터 시작이니 temp에 1을 담고 idx는 1개,
                                # 목표는 n개, 누적합은 0으로 시작
                                
    print(f'#{case+1} {res}')

