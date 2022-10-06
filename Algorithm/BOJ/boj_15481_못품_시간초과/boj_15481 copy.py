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

dic = defaultdict(set)
dic_d = defaultdict(int)

res = 0
cnt = 0
for s, e ,w in lst:
    ps, pe = findset(s), findset(e)
    if ps != pe:
        union(ps, pe)
        res += w
        cnt += 1
        dic[s].add(e)
        dic[e].add(s)
        dic[e].add(e)
        dic[s].add(s)
        dic_d[(s,e)] = w
        dic_d[(e,s)] = w

    if cnt == v-1:
        break

for s, e, w in data:
    if e in dic[s]:
        print(res)
    else:
        q_1 = deque()
        q_2 = deque()
        q_1.append(s)
        q_2.append(e)
        visited = [0]*(v+1)
        max_1 = [0]*(v+1)


        while q_1 or q_2:
            if q_1 and q_2:
                ns = q_1.popleft()
                ne = q_2.popleft()
                gyo = dic[ns] & dic[ne]
                if not gyo:
                    for i in dic[ns]:
                        if visited[i] == 0:
                            visited[i] = 1
                            q_1.append(i)
                            if max_1[i] < dic_d[(ns,i)]:
                                max_1[i] = dic_d[(ns,i)]
                    for i in dic[e]:
                        if visited[i] == 0:
                            visited[i] = 1
                            q_2.append(i)
                            if max_1[i] < dic_d[(ne,i)]:
                                max_1[i] = dic_d[(ne,i)]
                elif len(gyo) == 1:
                    arrv = gyo.pop()
                    maxi = max(dic_d[(ns, arrv)], dic_d[(ne, arrv)], max_1[ns], max_1[ne])
                    print(res - maxi + w)
                    break
                elif len(gyo) == 2:
                    a = gyo.pop()
                    b = gyo.pop()
                    if a == s and b == e or a == e or b == s:
                        print(res)
                        break
                    maxi = max(max_1[ns], max_1[ne], dic_d[(a, b)])
                    print(res - maxi + w)
                    break
            elif q_1:
                ns = q_1.popleft()
                gyo = dic[ns] & dic[ne]
                if not gyo:
                    for i in dic[ns]:
                        if visited[i] == 0:
                            visited[i] = 1
                            q_1.append(i)
                            if max_1[i] < dic_d[(ns,i)]:
                                max_1[i] = dic_d[(ns,i)]
                elif len(gyo) == 1:
                    arrv = gyo.pop()
                    maxi = max(dic_d[(ns, arrv)], dic_d[(ne, arrv)], max_1[ns], max_1[ne])
                    print(res - maxi + w)
                    break
                elif len(gyo) == 2:
                    a = gyo.pop()
                    b = gyo.pop()
                    if a == s and b == e or a == e or b == s:
                        print(res)
                        break
                    maxi = max(max_1[ns], max_1[ne], dic_d[(a, b)])
                    print(res - maxi + w)
                    break            
            elif q_2:
                ne = q_2.popleft()
                gyo = dic[ns] & dic[ne]
                if not gyo:
                    for i in dic[ne]:
                        if visited[i] == 0:
                            visited[i] = 1
                            q_1.append(i)
                            if max_1[i] < dic_d[(ne,i)]:
                                max_1[i] = dic_d[(ne,i)]
                elif len(gyo) == 1:
                    arrv = gyo.pop()
                    maxi = max(dic_d[(ns, arrv)], dic_d[(ne, arrv)], max_1[ns], max_1[ne])
                    print(res - maxi + w)
                    break
                elif len(gyo) == 2:
                    a = gyo.pop()
                    b = gyo.pop()
                    maxi = max(max_1[ns], max_1[ne], dic_d[(a, b)])
                    print(res - maxi + w)
                    break            
