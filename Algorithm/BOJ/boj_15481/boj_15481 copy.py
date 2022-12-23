import sys
input = sys.stdin.readline

def findset(x):                          
    while x != rep[x]:
        x = rep[x]
    return x


v, e = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(e)]
lst = sorted(data, key=lambda x: x[2])
rep = [i for i in range(v+1)]
parent = [i for i in range(v+1)]
rank = [0]*(v+1)


res = 0
cnt = 0
for s, e ,w in lst:
    ps, pe = findset(s), findset(e)
    if ps != pe:
        res += w
        rep[pe] = ps
        cnt += 1
        parent[e] = s
    if cnt == v-1:
        break
print(res)
print(parent)








# for s, e, w in start:
#     if parent[s] == e or parent[e] == s:
#         print(res)
#     else:
#         maxi = 0
#         temp_s, temp_e = 0, 0
#         ts, te = s, e
#         while 1:
#             if key[te] > temp_e:
#                 temp_e = key[te]
#             te = parent[te]
#             if parent[te] == s:
#                 if key[te] > temp_e:
#                     temp_e = key[te]
#                 maxi = temp_e
#                 break
#             if key[ts] > temp_s:
#                 temp_s = key[ts]
#             ts = parent[ts]
#             if parent[ts] == e:
#                 if key[ts] > temp_s:
#                     temp_s = key[ts]
#                 maxi = temp_s
#                 break
#         print(res - maxi + w)