import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

x, y =  map(int, input().split())
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 0 ~ 끝을 포함한 잘리는 지점을 다 추가할 예정
garo = [0, y]
sero = [0, x]
for cut in lst:                 
    if cut[0] == 0:
        garo.append(cut[1])
    else:
        sero.append(cut[1])

# 오름차순 정렬
garo.sort()
sero.sort()

# 가장 큰 간격으로 잘리는 값을 저장
garo_max = 0
sero_max = 0
for i in range(len(garo)-1):
    if garo[i+1] - garo[i] > garo_max:
        garo_max = garo[i+1] - garo[i]
for i in range(len(sero)-1):
    if sero[i+1] - sero[i] > sero_max:
        sero_max = sero[i+1] - sero[i]

# 가로로 가장 큰 간격으로 잘린 거리와
# 세로로 가장 큰 간격으로 잘린 거리를 곱해서 출력
print(garo_max * sero_max)
