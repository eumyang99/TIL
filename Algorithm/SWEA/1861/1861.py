import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    # 더미 데이터로 둘러 쌓아서 받음
    lst = [[-5]*(n+2)] + [[-5] + list(map(int, input().split())) + [-5] for _ in range(n)] + [[-5]*(n+2)]


    # 델타탐색
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    value = n**n                            # 가장 작은 숫자를 나타내는 value
    res = 0                                 # 연속된 숫자 길이
 
    stack = []                              # 스택 생성                     
    visited = set()                         # visited 생성
                                            # 만약 1씩 커지거나 작아지는 경우만 고려한다면 필요 없겠지만
                                            # +1, -1을 동시에 고려해서 visited가 필요

    for x in range(1, n+1):                 # 리스트 전체 순회를 돌면서
        for y in range(1, n+1):
            if (x, y) not in visited:       # 방문하지 않았다면
                temp_cnt = 0                    # 임시숫자길이를 0으로 초기화
                stack.append((x, y))            # 스택에 추가
                temp_min = lst[x][y]            # 숫자길이 중 가장 작은 temp_min을 임시시작점으로 설정
                while stack:                # 스택 돌면서
                    sx ,sy = stack.pop()
                    h = lst[sx][sy]         # 현재 위치
                    for i in range(4):      # 델타 탐색
                        nx = sx + dx[i]
                        ny = sy + dy[i]
                        next = lst[nx][ny]  # 다음 위치
                        # 방문하지 않았고 현재보다 다음이 +1 or -1 이면
                        if (nx, ny) not in visited and (next == h+1 or next == h-1):
                            visited.add((nx, ny))           # 다음 녀석 방문처리
                            stack.append((nx, ny))          # 다음 녀석 stack 추가
                            temp_cnt += 1                   # 숫자 길이 +1
                            if next < temp_min:             # 다음 숫자가 현재 가장 작은 숫자 보다 작다면
                                temp_min = next             # 임시 시작점 갱신
                                              
                                        # while 다 돌고 나서    
                if temp_cnt > res:          # 임시숫자길이가 기존 보다 크다면
                    res = temp_cnt              # 숫자길이 갱신
                    value = temp_min            # 시작점 갱신
                elif temp_cnt == res:       # 임시숫자길이가 기존과 같다면
                    if value > temp_min:        # 작은 시작점으로 갱신
                        value = temp_min

    print(f'#{case+1} {value} {res}')
