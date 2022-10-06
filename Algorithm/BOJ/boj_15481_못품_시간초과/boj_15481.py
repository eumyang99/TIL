import sys
input = sys.stdin.readline
from collections import defaultdict

def prim(start):
    global key
    global parent

    mst = [0]*(v+1)
    key = [10000000001]*(v+1)
    parent = [-1]*(v+1)
    key[start] = 0
    parent[start] = start

    for _ in range(v+1):
        minv = 10000000001
        for i in range(v+1):
            if mst[i] == 0 and key[i] < minv:
                idx = i
                minv = key[i]
            
        mst[idx] = 1

        for e, w in dic[idx]:
            if mst[e] == 0 and w < key[e]:
                key[e] = w
                parent[e] = idx
    return sum(key[1:])


v, e = map(int, input().split())
dic = defaultdict(list)
start = []
for _ in range(e):
    s, e, w = map(int, input().split())
    dic[s].append((e, w))
    dic[e].append((s, w))
    start.append((s, e, w))

res = prim(1)


# for s, e, w in start:
#     if parent[s] == e or parent[e] == s:
#         print(res)
#     else:
#         maxi = 0
#         save = parent[s]
#         parent[s] = e
#         ts = e
#         while 1:
#             if key[ts] > maxi:
#                 maxi = key[ts]
#             ts = parent[ts]
#             print(ts)
#             if parent[ts] == s:
#                 if key[ts] > maxi:
#                     maxi = key[ts]
#                 break
#         print(res - maxi + w)
#         parent[s] = save




for s, e, w in start:
    if parent[s] == e or parent[e] == s:
        print(res)
    else:
        maxi = 0
        temp_s, temp_e = 0, 0
        ts, te = s, e
        while 1:
            if key[te] > temp_e:
                temp_e = key[te]
            te = parent[te]
            if parent[te] == s:
                if key[te] > temp_e:
                    temp_e = key[te]
                maxi = temp_e
                break

            if key[ts] > temp_s:
                temp_s = key[ts]
            ts = parent[ts]
            if parent[ts] == e:
                if key[ts] > temp_s:
                    temp_s = key[ts]
                maxi = temp_s
                break
        print(res - maxi + w)