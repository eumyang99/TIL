from collections import defaultdict, deque
import sys
input = sys.stdin.readline

## 발상
## 위상정렬
## 다만 선행되는 건물이 다 지어졌을 때,
## (선행되는 건물 중 가장 긴 소요시간 + 해당 건물 소요시간)을 누적해야 한다.

n = int(input())
lst = [0] + [tuple(map(int, input().split())) for _ in range(n)]
dic = defaultdict(list)
barrier = [0] * (n+1)
for i in range(1, n+1):
    info = lst[i]
    for e in info[1:-1]:
        dic[e].append((info[0], i))
        barrier[i] += 1

que = deque()
for i in range(1, n+1):
    if barrier[i] == 0:
        que.append((lst[i][0], i))

res = [0] * (n+1)
for time, node in que:
    res[node] = time

while que:
    time, node = que.pop()
    for w, e in dic[node]:
        barrier[e] -= 1
        ## barrier가 0이 되면
        if barrier[e] == 0:
            ## que에 우선 넣어주고
            que.append((w, e))
            
            ## 선행되어야 하는 건물 중 가장 큰 소요시간을 maxi에 담는다.
            maxi = 0
            for i in lst[e][1:-1]:
                maxi = max(maxi, res[i])
            ## 해당 노드의 소요시간 = maxi + 현재 건물의 소요시간
            res[e] = maxi + w


## print("\n".join(map(str, dp[1:]))) 이런 식으로 출력할 수 있네
## map으로 리스트를 str으로 바꾼 뒤 join으로 줄바꿈!
for time in res[1:]:
    print(time)

