n, m = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)]

max = 0
for row in lst:         # 각 행의 최소값 중 가장 큰 것 출력
    temp = min(row)
    if temp > max:
        max = temp

print(max)