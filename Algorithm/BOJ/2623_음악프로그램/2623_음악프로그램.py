from collections import defaultdict, deque
import sys
input = sys.stdin.readline

## 발상
## 위상정렬

n, m = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(m)]

dic = defaultdict(list)
barrier = [0] * (n+1)

for i in range(m):
    for x in range(2, len(lst[i])):
        dic[lst[i][x-1]].append(lst[i][x])
        barrier[lst[i][x]] += 1
q = deque()
for i in range(1, n+1):
    if barrier[i] == 0:
        q.append(i)

res = []
while q:
    singer = q.popleft()
    res.append(singer)

    for next_singer in dic[singer]:
        barrier[next_singer] -= 1
        if barrier[next_singer] == 0:
            q.append(next_singer)

if len(res) == n:
    print("\n".join(map(str, res)))
else:
    print(0)

