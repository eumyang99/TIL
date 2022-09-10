from collections import deque
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


T = int(input())
for case in range(T):
    x, y, n = map(int, input().split())
    lst = [list(map(int, (input().split()))) for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    que = deque()
    visited = set()
    cnt = 0
    for cab in lst:                             # 리스트에서 배추 좌표 하나씩 꺼내서
        if (cab[0], cab[1]) not in visited:     # 그것이 visited에 없으면
            que.append(cab)                     # que에 append
            while que:                          # que가 비어있지 않다면
                p, q = que.popleft()            # que를 팝해서 델타 탐색
                for i in range(4):          
                    nx = p + dx[i]
                    ny = q + dy[i]
                     # 델타 탐색한 좌표가 리슽에 있고 방문하지 않았다면
                    if [nx, ny] in lst and (nx, ny) not in visited:
                        que.append([nx, ny])    # que에 append
                        visited.add((nx, ny))   # 방문처리

            cnt += 1                            # 큐가 다 소진되어 비었다면 cnt +1
    print(cnt)


        


