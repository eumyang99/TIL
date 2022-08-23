import sys
sys.stdin = open("input.txt")

T = int(input())
for case in range(T):
    # 버스 노선 정보 리스트
    N = int(input()) # 노선 개수
    line = [list(map(int, input().split())) for _ in range(N)]

    # 정류장에 대한 정보 리스트
    P = int(input()) # 정류장 개수
    bus_stop = [int(input()) for _ in range(P)]

    # 노선에 겹치는 부분이 생기면 해당 노선에 얼만큼 겹쳤는지 dic으로 저장
    dic = {}
    for i in line:
        for x in range(i[0], i[1]+1):
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
    print(f'#{case+1}', end=" ")
    for bs in bus_stop:
        if bs in dic:
            print(dic[bs], end=" ")
        else:
            print(0, end=" ")
    print()



# 그리디
#     print(f'#{case+1}', end=" ")
#     # 버스 정류장을 하나씩 꺼내서
#     for bs in bus_stop:
#         cnt = 0
#         # 그 정류장이 해당 노선에 포함되면 cnt+1
#         for idx in range(N):
#              if line[idx][0] <= bs <= line[idx][1]:
#                 cnt += 1
#         print(cnt, end=" ")
#     print()




