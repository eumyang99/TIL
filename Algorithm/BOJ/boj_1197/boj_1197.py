# mst prim 알고리즘 정석

import sys
input = sys.stdin.readline
from collections import defaultdict

def prim(start):
    visited = [0] * (v+1)
    visited[start] = 1
    key = [float('inf')] * (v+1)
    key[start] = 0

    for e, w in dic[start]:
        key[e] = w

    for _ in range(v):
        minv = float('inf')
        for i in range(v+1):
            if visited[i] == 0 and key[i] < minv:
                idx = i
                minv = key[i]

        visited[idx] = 1

        for e, w in dic[idx]:
            if visited[e] == 0 and w < key[e]:
                key[e] = w

    return print(sum(key[1:]))



v, e = map(int, input().split())
dic = defaultdict(list)
for _ in range(e):
    s, e, w = map(int, input().split())
    dic[s].append((e, w))
    dic[e].append((s, w))

prim(1)

