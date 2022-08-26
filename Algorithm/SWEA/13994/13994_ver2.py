import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    print(lst)
    dic = {i:0 for i in range(1, 1001)}

    for i in range(n):
        s, e = lst[i][1], lst[i][2]

        if lst[i][0] == 1:
            for x in range(s, e+1):
                dic[x] += 1


        elif lst[i][1] == 2:
            for x in range(s, e, 2):
                dic[x] += 1
            dic[e] += 1


        else:
            if s % 2 == 0:
                for x in range(s+1, e):
                    if x % 4 == 0:
                        dic[x] += 1
                dic[s] += 1
                dic[e] += 1
            elif s % 2 == 1:
                for x in range(s+1, e):
                    if x % 3 == 0 and x % 10 != 0:
                        dic[x] += 1
                dic[s] += 1
                dic[e] += 1

    print(f'#{case+1} {max(dic.values())}')




