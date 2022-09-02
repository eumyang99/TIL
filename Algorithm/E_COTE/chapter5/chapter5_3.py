from collections import deque
import sys
sys.stdin = open("input_5_3.txt")

# 가로 세로
n, m = map(int, input().split())
# 더미 데이터 1 쌓음
lst = [[1]*(m+2)] + [[1] + list(map(int, input())) + [1] for _ in range(n)] + [[1]*(m+2)]

# 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS
que = deque()                           # 큐 생성
res = 0                                 

for x in range(1, n+2):                         # 리스트를 전부 돌면서
    for y in range(1, m+2):
        if lst[x][y] == 0:                      # 0이면 1로 바꾸고    
            lst[x][y] = 1
            que.append((x, y))                  # que에 추가

            while que:                          # 큐가 다 없어질 때까지
                p, q = que.popleft()            # 큐를 pop하고
                for i in range(4):              # 그 녀석에 대한 델타 탐색
                    nx = p + dx[i]
                    ny = q + dy[i]
                    if lst[nx][ny] == 0:        # 델타 탐색 중에 0이 있으면
                        lst[nx][ny] = 1         # 1로 바꾸고
                        que.append((nx, ny))    # 큐에 append
            else:                               # 큐가 다 닳아서 비었으면 res +1
                res += 1
print(res)



# # DFS
# stack = []
# res = 0

# for x in range(1, n+2):
#     for y in range(1, m+2):
#         if lst[x][y] == 0:
#             lst[x][y] = 1
#             stack.append((x, y))
#             while stack:
#                 p, q = stack.pop()
#                 for i in range(4):
#                     nx = p + dx[i]
#                     ny = q + dy[i]
#                     if lst[nx][ny] == 0:
#                         lst[nx][ny] = 1
#                         stack.append((nx, ny))
#             else:
#                 res += 1
# print(res)