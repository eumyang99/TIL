import sys
sys.stdin = open('input.txt')

def sample_search(y, start_x, start_y, limit_x, limit_y):
    global res
    temp = set()
    x = start_x
    while 1:
        if y + dy[0] < start_y:
            break
        nx = x + dx[0]
        ny = y + dy[0]
        value = lst[nx][ny]
        if value in temp:
            return
        temp.add(lst[nx][ny])
        x = nx
        y = ny

    while 1:
        if x + dx[1] > limit_x:
            break
        nx = x + dx[1]
        ny = y + dy[1]
        value = lst[nx][ny]            
        if value in temp:
            return            
        temp.add(lst[nx][ny])
        x = nx
        y = ny

    while 1:
        if y + dy[2] > limit_y:
            break
        nx = x + dx[2]
        ny = y + dy[2]
        value = lst[nx][ny]            
        if value in temp:
            return
        temp.add(lst[nx][ny])
        x = nx
        y = ny

    while 1:
        if x + dx[3] < start_x:
            break
        nx = x + dx[3]
        ny = y + dy[3]
        value = lst[nx][ny]            
        if value in temp:
            return
        temp.add(lst[nx][ny])
        x = nx
        y = ny

    res = len(temp)



def part_search(start_x, start_y, size):
    global res

    limit_x = start_x + size - 1
    limit_y = start_y + size - 1 
    for y in range(start_y+1, limit_y): # 규모에 따라 시작되는 y지점
        sample_search(y, start_x, start_y, limit_x, limit_y)
        if res != -1:
            return



T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

#   좌하, 우하, 우상, 좌상
    dx = [1, 1, -1, -1]
    dy = [-1, 1, 1, -1]

    res = -1
    def func():
        for size in range(n, 2, -1):
            for wx in range(0, n-size+1):
                for wy in range(0, n-size+1):
                    part_search(wx, wy, size)
                    if res != -1:
                        return

    func()
    print(f'#{case+1} {res}')

