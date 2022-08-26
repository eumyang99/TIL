import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    dic = {i:0 for i in range(1, 1001)}

    for i in range(n):
        s, e = lst[i][1], lst[i][2]
        if s == e:
            dic[s] += 1
        else:
            if lst[i][0] == 1:
                for x in range(s,e+1):
                    dic[x] += 1


            elif lst[i][0] == 2:
                for x in range(s, e, 2):
                    dic[x] += 1
                dic[e] += 1


            else:
                if s % 2 == 0:
                    ns = s + (4 - s % 4)
                    if ns < e:
                        for x in range(ns, e, 4):
                            dic[x] += 1
                    dic[s] += 1
                    dic[e] += 1
                elif s % 2 == 1:
                    ns = s + (3 - s % 3)
                    if ns < e:
                        for x in range(ns, e, 3):
                            if x % 10 == 0:
                                continue
                            dic[x] += 1
                    dic[s] += 1
                    dic[e] += 1

    print(f'#{case+1} {max(dic.values())}')




