def func(cnt, x, y, k):
    if x*y < k:                              ### 1)
            return print(0)                     # 불가능 할 때는 0을 출력

    s = 1                                       # 가장 바깥 껍데기의 첫번째 숫자
    e = x*y - (x-2)*(y-2)                       # 껍데기의 마지막 숫자
    while 1:
        cnt += 1                                # 몇 번째 껍데기인지 카운트 
        if s <= k <= e:                         # 좌석이 해당 껍데기 안에 있으면 반복문 종료
            break
        s = e + 1                               # 다음 껍데기의 시작은 이전 껍데기 마지막 숫자+1
        e = x*y - (x-2*(cnt+1))*(y-2*(cnt+1))   # 다음 껍데기의 마지막 숫자

    if s == e:                              ### 2)
        return print(cnt , cnt)                 # 만약 시작과 끝이 같다면 cnt, cnt 출력

                                            ### 3)
    distance = k - s                            # 해당 껍데기의 출발점과 좌석 사이의 거리
    p, q = cnt, cnt                             # 출력할 p, q는 cnt, cnt부터 시작
    nx , ny = x - 2*(cnt-1), y - 2*(cnt-1)      # 해당 껍데기의 가로, 세로 크기

    if distance <= ny-1:                        # 좌변에 있을 경우
        q += distance
    elif distance <= nx+ny-2:                   # 상변에 있을 경우
        p += distance-(ny-1)
        q += ny-1
    elif distance <= ny+nx+ny-3:                # 우변에 있을 경우
        p += nx-1
        q += ny-1 - (distance-(nx+ny-2))
    else:                                       # 하변에 있을 경우
        p += nx-1 - (distance-(ny+nx+ny-3))
    return print(p, q)                          # p, q 출력

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for case in range(T):
    x ,y =  map(int, input().split())
    k = int(input())

    func(0, x, y, k)

    


