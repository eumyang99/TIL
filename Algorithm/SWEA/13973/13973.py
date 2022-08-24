import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    fire, mass = map(int, input().split())
    lst = list(map(int, input().split()))
    print(lst)



