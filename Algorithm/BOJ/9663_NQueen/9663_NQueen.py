import sys
input = sys.stdin.readline

## 이 방법은 통과
## 2차원 배열에 방문처리해서 dfs 백트래킹을 함

def used_mark(map, x, y):
    used = [row[:] for row in map]
    x += 1
    l, r = y-1, y+1
    while x < n:
        # y축 처리
        used[x][y] = 1
        # 대각선 처리
        if l >= 0 :
            used[x][l] = 1
            l -= 1
        if r < n:
            used[x][r] = 1
            r += 1
        x += 1
    return used

def queen(used, x, cnt):
    global res
    if cnt == n:
        res += 1
        return
    for y in range(n):
        if used[x][y] == 0:
            new_used = used_mark(used, x, y)
            queen(new_used, x+1, cnt+1)
    else:
        return


## 이 방법은 시간 초과
## 일차원 배열에 queen을 놓은 좌표를 넣고 계산으로 가능성 파악

# def able(used, x, y):
#     for used_x, used_y in used:
#         if used_y == y or abs(used_x - x) == abs(used_y - y):
#             return False
#     return True

# def dfs(used, cnt):
#     global res
#     if cnt == n:
#         res += 1
#         return

#     new_x = used[-1][0] + 1
#     for new_y in range(n):
#         if able(used, new_x, new_y):
#             new_used = used + [(new_x, new_y)]
#             new_cnt = cnt + 1
#             dfs(new_used, new_cnt)
#     else:
#         return


    

n = int(input())
lst = [[0]*n for _ in range(n)]
res = 0
for y in range(n):
    map = [row[:] for row in lst]
    used = used_mark(map, 0, y)
    queen(used, 1, 1)
print(res)