import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    # 버스 노선 정보 리스트
    N = int(input()) # 노선 개수
    line = [list(map(int, input().split())) for _ in range(N)]
 
    # 정류장에 대한 정보 리스트
    P = int(input()) # 정류장 개수
    bus_stop = [int(input()) for _ in range(P)]
 
    print(f'#{case+1}', end=" ")
    # 버스 정류장이 
    for bs in bus_stop:
        cnt = 0
        # 해당 노선들 범위 안에 있을 때마다
        # cnt +1 하고 모든 노선을 다 확인해본 뒤
        # cnt값을 출력
        for idx in range(N):
             if line[idx][0] <= bs <= line[idx][1]:
                cnt += 1
        print(cnt, end=" ")
    print()