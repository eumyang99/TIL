# leaf 노드부터 개수를 누적해서 부모 노드에 기록
# 이 과정을 재귀로 구현

# 초기 루트노드의 값을 재귀로 찾아서 모든 노드의 값을 메모
# 메모에서 원하는 노드의 값을 찾아서 출력

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5 + 1)
input = sys.stdin.readline


def recur(node, parent):
    if memo[node]:
        return memo[node]

    for child in edges[node]:
        if child == parent:
            continue
        memo[node] += recur(child, node)

    memo[node] += 1
    return memo[node]


n, r, q = map(int, input().split())
edges = defaultdict(list)
for _ in range(n - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

memo = [0] * (n + 1)
recur(r, r)
for _ in range(q):
    node = int(input())
    print(memo[node])
