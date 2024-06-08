# 다익스트라 사용
# 숫자의 배열을 기존 다익스트라의 노드로 취급
# 숫자의 배열은 가중치 배열로 나타낼 수 없으니 hashmap으로 가중치 관리


import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def make_tuple(i, ni, nums):
    nums_arr = list(nums)
    nums_arr[i], nums_arr[ni] = nums_arr[ni], nums_arr[i]
    return tuple(nums_arr)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
edges = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    edges[s - 1].append((e - 1, w))

target = tuple(sorted(arr))
weight = defaultdict(int)
start = tuple(arr)
weight[start] = 0
que = [(0, start)]

while que:
    w, nums = heapq.heappop(que)
    if nums == target:
        print(w)
        break

    if w < weight[nums]:
        continue

    for i, edge in edges.items():
        for ni, nw in edge:
            new_w = w + nw
            next_nums = make_tuple(i, ni, nums)
            if weight[next_nums] == 0 or new_w < weight[next_nums]:
                weight[next_nums] = new_w
                heapq.heappush(que, (new_w, next_nums))
else:
    print(-1)
