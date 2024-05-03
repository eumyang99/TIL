from collections import deque

dx, dy = [0,1,0,-1], [1,0,-1,0]

def in_board(x, y, n):
    if 0 <= x and x < n and 0 <= y and y < n: return True
    return False
    

def solution(board):
    n = len(board)
    LIMIT = n * n * 6
    ## board : 벽은 0, 빈 공간은 [가로 진입 최소값, 세로 진입 최소값]
    for x in range(n):
        for y in range(n):
            if board[x][y]: board[x][y] = 0
            else: board[x][y] = [LIMIT, LIMIT]
    board[0][0] = 0

    ## que : (x, y, 진입 방향)
    ## 진입 방향 : 수평 = 0, 수직 = 1
    que = deque()
    ## 출발점에서 오른쪽, 왼쪽 확인 후 값 초기화
    if board[0][1]:
        board[0][1] = [1, 0]
        que.append((0,1,0))
    if board[1][0]:
        board[1][0] = [0, 1]
        que.append((1,0,1))
    
    while que:
        x, y, dir = que.popleft()
        ## 도착점이면 continue
        if x == n - 1 and y == n - 1: continue
        ## 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ## 범위 밖이거나 벽이면 continue
            if not in_board(nx, ny, n) or board[nx][ny] == 0: continue
            ## vh : 진입 방향
            vh = i % 2
            ## nx, ny에 도착했을 때의 최소값
            ## 현재 위치[방향] 값과 진입 방향이 같으면 +1, 다르면 +6
            new_cost = board[x][y][dir] + (1 if dir == vh else 6)
            ## new_cost가 최소값이 아니면 continue
            if board[nx][ny][vh] <= new_cost: continue
            ## 최소값 갱신 후 que에 추가
            board[nx][ny][vh] = new_cost
            que.append((nx, ny, vh))

    ## 도착점의 비용 * 100 출력
    return min(board[-1][-1]) * 100