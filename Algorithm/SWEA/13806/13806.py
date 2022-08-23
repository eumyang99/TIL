import sys
sys.stdin = open('input.txt')

def facto(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * facto(n-1)

def combi(n, r):
    temp = 1
    for i in range(n, n-r, -1):
        temp *= i
    res = temp // facto(r)
    return res



T  = int(input())
for case in range(T):
    size = int(input())

    res = 0
    for i in range(1, (size//20)+1):
        res += combi(size//10-i, i) * 2**i

    print(f'#{case+1} {res+1}')