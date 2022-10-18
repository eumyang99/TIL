import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

def findset(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        rank[x] += 1
        parent[y] = x


v, e = map(int, input().split())
data = []
for _ in range(e):
    s, e, w = map(int, input().split())
    data.append((s, e, w))
lst = sorted(data, key=lambda x: x[2])
parent = [i for i in range(v+1)]
rank = [0]*(v+1)

dic = defaultdict(list)
res = 0
cnt = 0
for s, e ,w in lst:
    ps, pe = findset(s), findset(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        # MST 간선 정보
        dic[s].append((e, w))
        dic[e].append((s, w))
    if cnt == v-1:
        break

print(parent)



for s, e, weight in data:
    if (e, weight) in dic[s]:
        print(res)
    else:
        dist_s = [0]*(v+1)
        dist_e = [0]*(v+1)
        used_s = set()
        used_e = set()

        sque = deque()
        eque = deque()
        sque.append(s)
        eque.append(e)
        
        while sque or eque:
            if sque and eque:
                os = sque.pop()
                oe = eque.pop()
                for ns, w in dic[os]:
                    used_s.add(ns)
                    sque.append(ns)
                    if dist_s[os] < w:
                        dist_s[ns] = w
                    else:
                        dist_s[ns] = dist_s[os]

                for ne, w in dic[oe]:
                    used_e.add(ne)
                    eque.append(ne)
                    if dist_e[oe] < w:
                        dist_e[ne] = w
                    else:
                        dist_e[ne] = dist_e[oe]
            elif sque:
                os = sque.pop()
                for ns, w in dic[os]:
                    used_s.add(ns)
                    sque.append(ns)
                    if dist_s[os] < w:
                        dist_s[ns] = w
                    else:
                        dist_s[ns] = dist_s[os]

            elif eque:
                oe = eque.pop()
                for ne, w in dic[oe]:
                    used_e.add(ne)
                    eque.append(ne)
                    if dist_e[oe] < w:
                        dist_e[ne] = w
                    else:
                        dist_e[ne] = dist_e[oe]

            gyo = used_s & used_e
            if len(gyo) == 1:
                a = gyo.pop()
                maxi = max(dist_s[a], dist_e[a])
                print(res - maxi + weight)
                break
            elif len(gyo) == 2:
                a = gyo.pop()
                maxi = max(dist_s[a], dist_e[a])
                print(res - maxi + weight)
                break



            
            


        


# 리스트에 인덱스에 해당하는 누적 최대값을 저장
# 세트에 bfs 깊이 들어갈 때마다 지나온 자리 저장
# 세트에 교집합이 생기면 위 리스트 인덱스 최대값으로 계산
    