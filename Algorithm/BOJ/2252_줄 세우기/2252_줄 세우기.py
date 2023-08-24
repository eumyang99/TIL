from collections import defaultdict, deque
import sys
input = sys.stdin.readline

## 노션 - 알고리즘 - 정렬 - 위상정렬

n, m = map(int, (input().split()))
dic = defaultdict(list)
barrier = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    barrier[b] += 1

que = deque()
for i in range(1, n+1):
    if barrier[i] == 0:
        que.append(i)

while que:
    student = que.popleft()
    print(student)
    for next in dic[student]:
        barrier[next] -= 1
        if barrier[next] == 0:
            que.append(next)
