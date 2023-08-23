import sys
input = sys.stdin.readline

s = int(input())

num = 2
while 1:
    s -= num
    if s <= 0:
        print(num-1)
        break
    num += 1

