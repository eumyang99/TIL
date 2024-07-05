from collections import deque


# 네 칸이 같은 카드인지 확인하는 함수
# 같은 카드라면 해당 카드의 좌표를 set으로 return
# 같지 않다면 False return
def check(board, i, j):
    sample = board[i][j]
    add_remove = set()
    for x in range(i, i + 2):
        for y in range(j, j + 2):
            if board[x][y] != sample:
                return False
            add_remove.add((x, y))
    return add_remove


# 제거할 카드의 좌표의 값을 0으로 만드는 함수
def remove(board, remove_set):
    for x, y in remove_set:
        board[x][y] = 0


# 제거된 카드만큼 카드를 아래로 내리는 함수
# 특정 열의  마지막 행부터 0을 만나면 que에 저장
# que가 있을 때 카드를 만나면 que의 bottom 좌표와 값을 교환, 이후 que에 카드행의 좌표를 que에 추가
def col_move(board, m, n):
    for y in range(n):
        empty_que = deque()
        for x in range(m - 1, -1, -1):
            if not board[x][y]:
                empty_que.append(x)
                continue

            if not empty_que:
                continue

            empty_x = empty_que.popleft()
            board[empty_x][y], board[x][y] = board[x][y], board[empty_x][y]
            empty_que.append(x)


def solution(m, n, board):
    answer = 0
    board = list(map(lambda x: list(x), board))
    while 1:
        # 제거할 좌표 set
        remove_set = set()
        # board를 순회하며
        for i in range(m - 1):
            for j in range(n - 1):
                # 카드가 비어있는 자리면 continue
                if not board[i][j]:
                    continue
                # 카드가 있을 경우 2*2 윈도우 탐색
                add_remove = check(board, i, j)
                # 2*2 윈도우를 제거할 수 없다면 continue
                if not add_remove:
                    continue
                # 제거할 윈도우라면 해당 좌표들을 remove_set에 저장
                remove_set.update(add_remove)

        # remove_set이 비어있으면 while문 break
        if not remove_set:
            break

        # remove_set에 있는 카드 좌표값을 0으로 만들고
        remove(board, remove_set)
        # 내릴 수 있는 카드는 내림
        col_move(board, m, n)
        # 제거한 카드 수를 answer에 누적
        answer += len(remove_set)

    return answer
