import sys
input  = sys.stdin.readline

a = int(input())
lst = list(map(int, (input().split())))
lst.sort()

if a%2 == 0: # 짝수
    print(lst[0]*lst[-1])
    
elif a%2 == 1: # 홀수
    print(lst[a//2]**2)

