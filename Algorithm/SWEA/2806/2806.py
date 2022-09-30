import sys
sys.stdin = open('input.txt')

# 순열로 풀어보자

def permu(idx, n, temp):
    global res
    if idx == n:
        res += 1

    for i in range(n):
        if i not in temp:
            temp.append(i)
            permu(idx + 1, n, temp)
            temp.




T = int(input())
for case in range(T):
    n = int(input())
    res = 0
    



    print(lst)


                
