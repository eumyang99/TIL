import sys
input = sys.stdin.readline

## 발상
## 회수가 늘어나는 기준을 찾는다
## 1
## 1 1
## 1 2 1
## 1 2 2 1
## 1 2 3 2 1
## 1 2 3 3 2 1
## 1 2 3 4 3 2 1
## 시그마k 공식을 써서 해당하는 회수를 찾는다

t = int(input())
lst = [tuple(map(int, input().split())) for _ in range(t)]
for xy in lst:
    dist = xy[1] - xy[0]
    k = 1
    while 1:
        if k * (k+1) < dist:
            k += 1
        else:
            if k * k >= dist:
                print(2*k-1)
                break
            else:
                print(2*k)
                break