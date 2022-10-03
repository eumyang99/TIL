import sys
input = sys.stdin.readline

def combi(idx, n, r, temp, start):
    if idx == r:
        print(*temp)
    
    for i in range(start, n+1):
        temp.append(lst[i])
        combi(idx+1, n, r, temp, i+1)
        temp.pop()

while 1:
    lst = list(map(int, input().split()))
    if lst[0] != 0:
        combi(0, lst[0], 6, [], 1)
        print()
    else:
        break
