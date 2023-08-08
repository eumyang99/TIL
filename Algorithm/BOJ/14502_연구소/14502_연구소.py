from collections import deque
import sys
input = sys.stdin.readline

def counting(zero_cnt):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    for a in range(n*m-2):
        if lst[a//m][a%m] == 0:
            for b in range(a, n*m-1):
                if lst[b//m][b%m] == 0:
                    for c in range(b, n*m):
                        if lst[c//m][c%m] == 0:
                            stack = deque(virus_1)
                            temp = [lst[i][:] for i in range(n)]
                            temp[a//m][a%m] = 1
                            temp[b//m][b%m] = 1
                            temp[c//m][c%m] = 1
                            
                            cnt = 0
                            while stack:
                                x, y = stack.popleft()
                                for i in range(4):
                                    nx, ny = x+dx[i], y+dy[i]
                                    if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                                        temp[nx][ny] = 2
                                        stack.append((nx, ny))
                                        cnt += 1

                            if zero_cnt - cnt > res:
                                res = zero_cnt - cnt
    
    return res
                            



                    





n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

virus_1 = []
zero_cnt = 0
for x in range(n):
    for y in range(m):
        if lst[x][y] == 0:
            zero_cnt += 1
        elif lst[x][y] == 2:
            virus_1.append((x,y))

print(counting(zero_cnt)-3)


            