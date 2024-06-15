# 모든 카드의 짝을 맞춰 뒤집을 때 조작 비용의 최소값을 구하는 문제

# 짝을 맞춰 뒤집을 캐릭터의 순서를 순열로 정리하고
# 해당 순서에 맞게 최소값으로 움직일 때 가장 작은 값을 출력했음

# a 지점에서 b 지점으로 이동하는 최소값 => BFS
# 한 순열의 전체 비용 => 재귀 + memo
# memo는 현재 위치와 앞으로 뒤집어야 할 캐릭터(순서 보장해야 함)를 key로 dict에 저장

import sys
from collections import defaultdict, deque
INF = sys.maxsize

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
char = defaultdict(list)

# 순열 생성 함수


def make_permu(arr):
    temp = []

    def permu(p, arr):
        if len(p) == len(arr):
            return temp.append(p[:])

        for i in range(len(arr)):
            if arr[i] in p:
                continue
            p.append(arr[i])
            permu(p, arr)
            p.pop()
    permu([], arr)
    return temp

# 범위 확인 함수


def in_board(x, y):
    if 0 <= x < 4 and 0 <= y < 4:
        return True
    return False

# crtl로 움직일 때, 해당 경로의 카드가 제거된 카드인지 확인하는 함수


def is_removed(x, y, removed):
    for char_num in removed:
        if (x, y) in char[char_num]:
            return True
    return False

# ctrl로 특정 방향으로 움직일 때 도착 지점을 구하는 함수


def ctrl_move(x, y, i, removed, board):
    while 1:
        nx, ny = x + dx[i], y + dy[i]
        # board 범위를 넘어가면 테두리 칸에 위치 반환
        if not in_board(nx, ny):
            return (x, y)
        # 제거되지 않은 카드를 만나면 해당 위치 반환
        if board[nx][ny] and not is_removed(nx, ny, removed):
            return (nx, ny)
        # 빈 곳이면 이동
        x, y = nx, ny

# start -> end 이동 비용 구하는 함수(BFS)


def cost(sx, sy, ex, ey, removed, board):
    que = deque([(sx, sy, 0)])
    visited = set((sx, sy))
    while que:
        x, y, c = que.popleft()
        if x == ex and y == ey:
            return c

        for i in range(4):
            nx, ny = ctrl_move(x, y, i, removed, board)
            if (nx, ny) in visited:
                continue
            que.append((nx, ny, c + 1))
            visited.add((nx, ny))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_board(nx, ny):
                continue
            if (nx, ny) in visited:
                continue
            que.append((nx, ny, c + 1))
            visited.add((nx, ny))

# 카드 제거 순열의 전체 비용구하는 함수


def total_cost(sx, sy, order, idx, memo, board):
    # memo된 것이 있으면 해당 값 사용
    memo_key = (sx, sy, *order[idx:])
    if memo[memo_key]:
        return memo[memo_key]

    if len(order) == idx:
        return 0

    # 쌍을 이루는 카드의 각 위치
    ax, ay = char[order[idx]][0]
    bx, by = char[order[idx]][1]

    # 제거된 카드
    removed = order[:idx]
    # 한 쌍이 A지점과 B지점에 위치할 때
    # A지점에서 B지점으로 이동하는 비용
    a_couple_cost = cost(ax, ay, bx, by, removed, board)
    # B지점에서 A지점으로 이동하는 비용
    b_couple_cost = cost(bx, by, ax, ay, removed, board)

    # 현재 위치에서 A지점으로 이동하는 비용 + A지점에서 B지점으로 이동하는 비용 + B지점에서 다음 캐릭터로 이동하는 비용
    a_cost = cost(sx, sy, ax, ay, removed, board) + a_couple_cost + \
        total_cost(bx, by, order, idx + 1, memo, board)
    # 현재 위치에서 B지점으로 이동하는 비용 + B지점에서 A지점으로 이동하는 비용 + A지점에서 다음 캐릭터로 이동하는 비용
    b_cost = cost(sx, sy, bx, by, removed, board) + b_couple_cost + \
        total_cost(ax, ay, order, idx + 1, memo, board)

    # 두 비용 중 최소값을 메모
    memo[memo_key] = min(a_cost, b_cost)

    # 최소값 반환
    return memo[memo_key]


def solution(board, r, c):
    # 카드 뒤집는 비용
    enter_cost = 0
    # 쌍을 이루는 카드의 위치 정보 기록
    for x in range(len(board)):
        for y in range(len(board)):
            if not board[x][y]:
                continue
            char[board[x][y]].append((x, y))
            # enter로 뒤집어야 하는 비용 누적
            enter_cost += 1

    # 순열 생성
    char_permu = char_permu = make_permu(list(char.keys()))
    # 메모 생성
    memo = defaultdict(int)

    # 순열의 각 경우에 따른 비용 갱신
    move_cost = INF
    for order in char_permu:
        move_cost = min(move_cost, total_cost(r, c, order, 0, memo, board))

    # 최소 이동 비용 + enter 비용 반환
    return move_cost + enter_cost
