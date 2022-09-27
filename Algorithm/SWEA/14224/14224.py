import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    info = list(map(int, input().split()))
    n = info[0]
    lst = info[1:]

    cnt = 0                         # 출력할 cnt
    end = n-1                       # 최종 목적지 end
    while end > 0:                  # 최종 목적지가 범위 안에 있을 때
        for i in range(end):        # 처음부터 목적지 전까지 순회하면서
            if i + lst[i] >= end:   # 목적지 도착이 가능한 지점을 최초로 발견하면
                end = i             # 목적지를 그곳으로 갱신하고 for문 종료
        cnt += 1                    # 충전 +1
    
    
    print(f'#{case+1} {cnt-1}')
