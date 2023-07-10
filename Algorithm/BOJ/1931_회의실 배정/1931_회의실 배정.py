import sys
input = sys.stdin.readline

## 발상
## 일찍 끝나는 녀석들로 채우면 된다

## 그러기 위해서 [s, e]들을 담은 lst를 정렬해야 하는데
## 처음에는 lambda를 사용해서 e를 오름차순 정렬했다
## 이 경우 s,e 가 [9, 9], [1, 9]일 때, [9, 9]가 먼저 for문에 걸리면서 [1, 9]를 체크하지 못했다.
## 따라서 크게 e를 기준으로 정렬하고 같은 e일 경우 s를 기준으로 정렬할 필요가 있었다.
## 따라서 lambda: x[0]으로 정렬 후, lambda: x[1]로 정렬했는데 됐다.
## 문제는 비효율적이라는 느낌!!

## 알아본 바, 파이썬의 기본 sort()는 앞에 것부터 정렬하고 이후 같은 값일 경우 뒤까지 다 정렬해준다.
## 따라서 e로 먼저 정렬, 그 다음 s로 정렬해야 하니
## lst에 담을 때, [s, e]로 담지 않고 [e, s]로 담았다.

n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append([e, s])

lst.sort()

res = 0
last = 0
for i in range(n):
    if lst[i][1] >= last:
        res += 1
        last = lst[i][0]

print(res)