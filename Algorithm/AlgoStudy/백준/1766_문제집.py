import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

## 발상
## 이 문제의 핵심 발상은 앞에 막고 있는 녀석(선행이 필요한 문제)이 0인 문제를 작은 숫자부터 출력하는 것
## 배리어가 0인 녀석들 중 가장 작은 녀석을 출력하면서
## 지금 출력한 문제가 막고 있는 문제들의 배리어를 1씩 깎아 준다
## 깎고 난 뒤 배리어가 0이 된 문제를 다시 우선순위 큐(배리어가 0이 된 문제들)에 넣어준다
## 얘는 이제 막을 수 있는 문제가 없으니 등장해도 되기 때문
## 우선순위 큐에 넣음으로서 문제 번호가 작으면 큐에 먼저 들어와 있는 문제보다 선행해서 풀 수 있게 된다

n, m = map(int, input().split())
dic = defaultdict(list)
barrier = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    barrier[b] += 1

pq = []
for i in range(1, n+1):
    if barrier[i] == 0:
        pq.append(i)

while pq:
    x = heapq.heappop(pq)
    print(x, end=" ")
    for y in dic[x]:
        barrier[y] -= 1
        if barrier[y] == 0:
            heapq.heappush(pq, y)
