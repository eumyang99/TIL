import sys
sys.stdin = open('input.txt')

def six_way(start_x, start_y, temp, len):
    global bowl

    if len == 7:                            # temp 길이가 7이면
        way = tuple(temp)                   # 튜플 way에 temp를 튜플형으로 담음
        bowl.add(way)                       # bowl에 경로 추가 후 종료
        return              

    for i in range(4):                      # 시작점에 대해서 델타 탐색을 하면서
        nx = start_x + dx[i]
        ny = start_y + dy[i]
        if 0 <= nx <4 and 0 <= ny <4:       # 리스트 인덱스 안에 있으면
            temp.append(lst[nx][ny])        # temp에 해당 값 추가
            six_way(nx, ny, temp, len+1)    # 이후 temp길이만 +1하고 다시 함수로
            temp.pop()                      # 앞서 temp가 꽉차서 내려온 것이기 때문에 마지막 녀석을 pop해주고 
                                            # 다음 델타탐색 대상이 들어올 수 있도록 함

T = int(input())
for case in range(T):                                               
    lst  = [list(map(int, input().split())) for _ in range(4)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    bowl = set()                        # 중복 제거를 위한 set
    for start_x in range(4):            # 리스트 전체를 순회하면서
        for start_y  in range(4):
            # 경로 탐색하는 함수에 넣음
            # 시작점x, 시작점y, temp 리스트에 출발점 값, temp 리스트의 길이 
            six_way(start_x, start_y, [lst[start_x][start_y]], 1)

    print(f'#{case+1} {len(bowl)}')



