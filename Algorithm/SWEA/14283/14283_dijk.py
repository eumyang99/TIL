from collections import defaultdict
import sys
sys.stdin = open('input.txt')

def dijk(start):
    dist = [float('inf')] * (n+1)
    visited = [0] * (n+1)
    dist[start] = 0
    visited[start] = 1

    for e, w in dic[start]:
        dist[e] = w

    for _ in range(n+1):
        minv = float('inf')
        for i in range(n+1):
            if not visited[i] and dist[i] < minv:
                idx = i
                minv = dist[i]
        visited[idx] = 1

        for e, w in dic[idx]:
            dist[e] = min(dist[e], dist[idx] + w)
    
    return dist[n]


T = int(input())
for case in range(T):
    n, e = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(e):
        s, e, w = map(int, input().split())
        dic[s].append((e, w))


    print(f'#{case+1} {dijk(0)}')

