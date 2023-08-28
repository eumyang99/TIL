from collections import deque
import sys
input = sys.stdin.readline

## 발상
## 상근이가 갈 곳이 있을 때,
## 불을 먼저 번지게 하고 불 자리를 방문처리한다.
## 그리고 나서 상근이의 사방탐색을 한다.
## 탈출하면 결과 출력
## 상근이의 큐가 비어있게 되면 불가능 출력

## 한꺼풀씩 bfs를 탐색할 때
## 지금 bfs를 돌 때 한꺼풀 갈 수 있을 때 마다 res += 1 해줘야 하기 때문에
## 큐를 한번 소진시키면서 임시 리스트에 다음 갈 곳을 담은 뒤
## 큐가 비워지면 반복을 끝내면서 담아 놓은 임시 리스트를 큐에 다시 할당한다.

## 아래는 for문으로 bfs
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def uu(me_x, me_y, fire_que, lst):
    res = 0
    me_que = [(me_x, me_y)]

    while me_que:
        new_fire_que = []
        for fx, fy in fire_que:
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0 <= nfx < h and 0 <= nfy < w and lst[nfx][nfy] == ".":
                    lst[nfx][nfy] = 1
                    new_fire_que.append((nfx, nfy))
        else:
            fire_que = new_fire_que
        
        new_me_que = []
        for x, y in me_que:
            if x == 0 or x == h-1 or y == 0 or y == w-1:
                return print(res+1)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == ".":
                    lst[nx][ny] = 1
                    new_me_que.append((nx, ny))
        else:
            me_que = new_me_que
        
        res += 1
    else:
        print("IMPOSSIBLE")



## 아래는 while로 bfs
t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    lst = [list(input().rstrip()) for _ in range(h)]

    fire_que = []
    for x in range(h):
        for y in range(w):
            if lst[x][y] == "@":
                me_x, me_y = x, y
                lst[me_x][me_y] = 1
            if lst[x][y] == "*":
                lst[x][y] = 1
                fire_que.append((x, y))

    uu(me_x, me_y, fire_que, lst)


# from collections import deque
# import sys
# input = sys.stdin.readline


# dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

# def uu(me_x, me_y, fire, lst):
#     res = 0
#     fire_que = fire
#     me_que = deque()
#     me_que.append((me_x, me_y))

#     while me_que:
#         new_fire_que = deque()
#         while fire_que:
#             fx, fy = fire_que.popleft()
#             for i in range(4):
#                 nfx, nfy = fx + dx[i], fy + dy[i]
#                 if 0 <= nfx < h and 0 <= nfy < w and lst[nfx][nfy] == ".":
#                     lst[nfx][nfy] = 1
#                     new_fire_que.append((nfx, nfy))
#         else:
#             fire_que = new_fire_que
        
#         new_me_que = deque()
#         while me_que:
#             x, y = me_que.popleft()
#             if x == 0 or x == h-1 or y == 0 or y == w-1:
#                 return print(res+1)

#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == ".":
#                     lst[nx][ny] = 1
#                     new_me_que.append((nx, ny))
#         else:
#             me_que = new_me_que
        
#         res += 1
#     else:
#         print("IMPOSSIBLE")




# t = int(input())
# for _ in range(t):
#     w, h = map(int, input().split())
#     lst = [list(input().rstrip()) for _ in range(h)]

#     fire = deque()
#     for x in range(h):
#         for y in range(w):
#             if lst[x][y] == "@":
#                 me_x, me_y = x, y
#                 lst[me_x][me_y] = 1
#             if lst[x][y] == "*":
#                 lst[x][y] = 1
#                 fire.append((x, y))

#     uu(me_x, me_y, fire, lst)
