import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
start = list(map(int, input().split()))


res = 0
for store in lst:
    if start[0] == store[0]:                                        # 같은 변에 있을 때
        res += abs(start[1] - store[1])
    elif start[0] + store[0] == 3 or start[0] + store[0] == 7:      # 마주보고 있을 때
        if start[0] == 1 or start[0] == 2:  # 시작이 북or남 일 때
            if start[1] + store[1] == x:
                res += (x + y)
            elif start[1] + store[1] < x:
                res += (start[1] + store[1]) + y
            else:
                res += x*2 - (start[1] + store[1]) + y
        else:                               # 시작이 동or서 일 때
            if start[1] + store[1] == y:
                res += (x + y)
            elif start[1] + store[1] < y:
                res += (start[1] + store[1] + x)    
            else:
                res += y*2 - (start[1] + store[1])            
    else:                                                           # 옆에 있을 때
        if start[0] == 1:
            if store[0] == 3:
                res += start[1] + store[1] 
            elif store[0] == 4:
                res += (x - start[1]) + store[1] 

        elif start[0] == 2:
            if store[0] == 3:
                res += start[1] + (y - store[1])
            elif store[0] == 4:
                res += (x - start[1]) + (y - store[1])

        elif start[0] == 3:
            if store[0] == 1:
                res += start[1] + store[1]
            elif store[0] == 2:
                res += (y - start[1]) + store[1]

        elif start[0] == 4:
            if store[0] == 1:
                res += start[1] + (x - store[1])
            elif store[0] == 2:
                res += (y - start[1]) + (x - store[1])

print(res)
