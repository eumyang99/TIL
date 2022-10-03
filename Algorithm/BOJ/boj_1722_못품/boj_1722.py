import sys
input = sys.stdin.readline

def permu_1(idx, n, temp):
    global cnt
    if idx == n:
        cnt += 1
        if cnt == tg:
            return print(*temp)
    
    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            permu_1(idx+1, n, temp)
            temp.pop()

def permu_2(idx, n, temp):
    global cnt
    if idx == n:
        cnt += 1
        if temp == tg:
            return print(cnt)
    
    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            permu_2(idx+1, n, temp)
            temp.pop()



n = int(input())
lst = list(map(int, input().split()))
cnt = 0
if lst[0] == 1:
    tg = lst[1]
    permu_1(0, n, [])
else:
    tg = lst[1:]
    permu_2(0, n, [])