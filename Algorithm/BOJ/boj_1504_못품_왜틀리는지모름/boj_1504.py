import sys
input = sys.stdin.readline
from collections import defaultdict

def dijk(start):
    visited = [0]*(v+1)
    key = [float('inf')]*(v+1)
    visited[start] = 1
    key[start] = 0
    for e, w in dic[start]:
        key[e] = w

    for _ in range(v-1):
        minv = float('inf')
        for i in range(v+1):
            if visited[i] == 0 and key[i] < minv:
                idx = i
                minv = key[i]
        try:
            visited[idx] = 1
        except:
            return key

        for e, w in dic[idx]:
            if key[e] > key[idx] + w:
                key[e] = key[idx] + w

    return key



v, e = map(int, input().split())
dic = defaultdict(list)
for _ in range(e):
    s, e, w = map(int, input().split())
    dic[s].append((e, w))
    dic[e].append((s, w))
start, end = map(int, input().split())
need = 0
for e, w in dic[start]:
    if e == end:
        need = w 
for e, w in dic[end]:
    if e == start:
        need = w 
if v not in dic:
    print(-1)
else:
    temp_1 = dijk(1)
    temp_2 = dijk(v)
    if temp_1[-1] == float('inf') or temp_1[start] == float('inf') or temp_1[end] == float('inf') or temp_2[start] == float('inf') or temp_2[end] == float('inf'):
        print(-1)
    else:
        a = min(temp_1[end] + temp_2[end], temp_1[start] + temp_2[start])
        b = min(temp_1[start] + temp_2[end], temp_1[end] + temp_2[start])
        if a + need*2 < b + need:
            print(a + need*2)
        else:
            print(b + need)
        # print(min(temp_1[start] + temp_2[end], temp_1[end] + temp_2[start]) + need)


