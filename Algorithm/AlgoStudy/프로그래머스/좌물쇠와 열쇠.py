# 좌물쇠 board의 테두리에 key의 값을 고려하여 확장
# 좌물쇠를 윈도우 슬라이싱하며 구멍과 일치하는지 확인
# 2차원 배열을 사용하지 않고 돌기와 구멍의 좌표만으로 확인했음

# key의 돌기 좌표를 시계 방향으로 회전시키는 함수
def rotate(arr, key_size):
    for i in range(len(arr)):
        rx, ry = arr[i][1], key_size - arr[i][0] - 1
        arr[i][0], arr[i][1] = rx, ry


# 좌물쇠가 열리는지 확인하는 함수
def check(i, j, spine, hole, key_size, lock_size):
    # 채워야할 구멍의 개수
    cnt = len(hole)
    # 돌기의 좌표를 순회하며
    for sx, sy in spine:
        # 윈도우 슬라이싱한 값 만큼 돌기의 좌표를 조정
        adj_sx, adj_sy = sx + i, sy + j
        # 해당 돌기가 좌물쇠 범위 밖이면 continue
        if adj_sx < key_size - 1 or key_size + lock_size - 1 <= adj_sx:
            continue
        if adj_sy < key_size - 1 or key_size + lock_size - 1 <= adj_sy:
            continue
        # 해당 돌기가 좌물쇠 범위 안에 있는데
        # 구멍의 좌표와 일치하는 것이 없다면 돌기가 충돌하기 때문에 불가능한 경우
        if (adj_sx, adj_sy) not in hole:
            break
        # 위 조건에 걸리지 않았다면 구멍과 돌기가 일치
        # 채워야할 구멍 개수 감소
        cnt -= 1

    # 모든 구멍이 채워졌다면 True, 그렇지 않다면 False 반환
    return False if cnt else True


def solution(key, lock):
    key_size, lock_size = len(key), len(lock)

    # 확장된 lock board 만큼 구멍의 좌표를 조정 후 저장
    hole = set()
    for x in range(lock_size):
        for y in range(lock_size):
            if lock[x][y]:
                continue
            hx, hy = x + key_size - 1, y + key_size - 1
            hole.add((hx, hy))

    # 돌기의 좌표를 저장
    spine = []
    for x in range(key_size):
        for y in range(key_size):
            if not key[x][y]:
                continue
            spine.append([x, y])

    # 구멍의 개수보다 돌기가 작다면 애초에 불가능
    if len(spine) < len(hole):
        return False

    # 4방향을 탐색
    for t in range(4):
        # key의 위치를 조정(윈도우 슬라이싱)
        for i in range(key_size + lock_size):
            for j in range(key_size + lock_size):
                # i, j : 윈도우 슬라이싱 값
                # 좌물쇠가 열리면 True return
                if check(i, j, spine, hole, key_size, lock_size):
                    return True

        # 마지막 방향을 탐색했다면 key를 rotate 하지 않고 break
        if t == 3:
            break
        # key를 시계방향으로 회전
        rotate(spine, key_size)

    # 위 check에서 True 반환이 되지 않았다면
    # 모든 경우에서 불가능하기에 False return
    return False
