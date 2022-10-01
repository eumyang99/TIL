from collections import defaultdict
import sys
sys.stdin = open('input.txt')

def prim(start):
    used = set()
    dist = [float('inf')] * (v+1)
    used.add(start)
    dist[start] = 0
    for e, w in dic[start]:
        dist[e] = w

    for _ in range(v):
        minv = float('inf')
        for i in range(v+1):
            if i not in used and dist[i] < minv:
                idx = i
                minv = dist[i]

        used.add(idx)

        for e, w in dic[idx]:
            if e not in used and dist[e] > w:
                dist[e] = w
    print(dist)
    return sum(dist)
T = int(input())
for case in range(T):
    v, e = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(e):
        s, e, w =  map(int, input().split())
        dic[s].append((e, w))
        dic[e].append((s, w))

    print(f'#{case+1} {prim(0)}')