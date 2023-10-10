from collections import defaultdict
import heapq

## 트리의 지름 : 임의의 노드에서 가장 먼 노드를 찾고 그 노드에서 가장 먼 노드까지의 길이를 찾으면 됨

import sys
input = sys.stdin.readline

def dijk(start):
    weight = [float("inf")] * (n+1)
    weight[start] = 0
    que = [(0, start)]

    while que:
        w, e = heapq.heappop(que)
        if w > weight[e]:
            continue

        for nw, ne in dic[e]:
            new_weight = w + nw
            if new_weight < weight[ne]:
                weight[ne] = new_weight
                heapq.heappush(que, (new_weight, ne))

    maxi = max(weight[1:])
    maxi_idx = weight.index(maxi)

    return (maxi, maxi_idx)

n = int(input())
dic = defaultdict(list)
for _ in range(n):
    temp = tuple(map(int, input().split()))
    s = temp[0]
    for i in range(1, len(temp)-1, 2):
        w, e = temp[i+1], temp[i]
        dic[s].append((w, e))
else:
    start = s

temp_maxi, temp_maxi_idx = dijk(start)
res_maxi, res_maxi_idx = dijk(temp_maxi_idx)
print(res_maxi)
