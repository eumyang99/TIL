from collections import deque


def solution(n, weak, dist):
    # 원형이기 때문에 배열 확장
    ext_weak = weak + [w + n for w in weak]
    # 큰 거리를 담당하는 사람이 먼저 쓰이는 것이 맞으니 내림차순 정렬
    dist.sort(reverse=True)

    # 바로 다음 수리 지점을 찾기 위한 함수
    # 현재 커버하고 있는 범위(s ~ e)를 인자로 받음

    def next_weak(s, e):
        # 모든 취약 지점을 순회하며
        for w in ext_weak:
            # 다음 지점을 찾아야 하니 e보다 작으면 continue
            if w <= e:
                continue
            # 점검해야할 다음 지점이 초기 시작점이면 모든 곳을 수리한 것, -1 반환
            # 시작지점으로 돌아왔다는 것은 한 바퀴를 돌았다는 것이기 때문에 무조건 w가 n보다 크거나 같을 때임
            if n <= w and s == w - n:
                break
            # 위 조건에 걸리지 않았다면 다음 수리 지점임
            return w
        return -1

    # que = [(커버할 수 있는 시작 지점, 마지막 지점, [사용된 사람들 인덱스])]
    # 모든 취약 지점에서 가장 긴 거리를 수리할 수 있는 사람을 배치하는 것으로 초기화
    que = deque(list(map(lambda x: (x, x + dist[0], [0]), weak)))
    while que:
        s, e, used = que.popleft()
        # 다음 수리 지점 확인
        n_weak = next_weak(s, e)
        # 모든 수리가 완료되었으면 현재 수리하고 있는 인원 수를 반환
        if n_weak == -1:
            return len(used)

        # 다음 수리할 지점에 배치할 사람 탐색
        # 모든 사람을 탐색하며
        for i in range(len(dist)):
            # 현재 수리 중인 사람은 continue
            if i in used:
                continue
            # 남아 있는 사람이면 배치 후 que에 추가
            # s = 시작 지점과 동일
            # e = 다음 수리할 지점 + 배치할 사람이 커버할 수 있는 거리
            # used = 수리 중인 사람에 배치할 사람의 인덱스 추가
            que.append((s, n_weak + dist[i], used + [i]))

    # while문에서 return이 없었다면 불가능한 경우
    return -1
