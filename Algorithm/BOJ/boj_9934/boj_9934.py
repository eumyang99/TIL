import sys
input = sys.stdin.readline

k = int(input())
lst = [0] + list(map(int, input().split()))

n = k-1
while n >= 0:                          
    print(*lst[2**n :  : 2**(n+1)])
    n -= 1













