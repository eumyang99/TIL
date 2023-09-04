import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    print(1)
else:
    que = [n]
    temp = []
    dist = 1
    cnt = 0
    flag = False
    used = {5}
    while 1:
        temp = []
        temp_set = set()
        while que:
            x = que.pop()
            a, b, c = x-1, x+1, 2*x
            if a == k or b == k or c == k:
                flag = True
                if a == k:
                    cnt += 1
                if b == k:
                    cnt += 1
                if c == k:
                    cnt += 1
                continue
            if not flag:
                if a > 0 and a not in used:
                    temp.append(a)
                    temp_set.add(a)
                if 0 < b < 2*k+1 and b not in used:
                    temp.append(b)
                    temp_set.add(b)
                if 0 < c < 2*k+1 and c not in used:
                    temp.append(c)
                    temp_set.add(c)
        else:
            if not cnt:
                que = temp
                used = used | temp_set
                dist += 1
            else:
                break


    print(dist)
    print(cnt)