import sys
input = sys.stdin.readline


n, m = map(int, input().split())
lst = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

sqr = [list(map(int, input().split())) for _ in range(m)]

for x in range(1, n+1):
    for y in range(1, n+1):
        lst[x][y] = lst[x][y] + lst[x][y-1]

for x in range(1, n+1):
    for y in range(1, n+1):
        lst[x][y] = lst[x][y] + lst[x-1][y]

for a,b,x,y in sqr:
    rdx, rdy = max(a, x), max(b, y)
    lux, luy = min(a, x), min(b, y)
    
    print(lst[rdx][rdy] - lst[rdx][luy-1] - lst[lux-1][rdy] + lst[lux-1][luy-1])
    