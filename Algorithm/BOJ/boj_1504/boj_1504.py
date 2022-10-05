import sys
input = sys.stdin.readline
from collections import defaultdict
# 4가지 경우의 수를 생각해야 함
# 1. 1 - start - end - v
# 2. 1 - end - start - v
# 3. 1 - start - end - start - v
# 4. 1 - end - start - end - v
# 1,2 번의 경우 start에서 end로 가는 가중치를 한번만 더하면 되지만
# 3,4 번의 경우 start에서 end로 가는 가중치를 두번 더해야 함
# 이 중 최소값을 출력

# 다익스트라 정석
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

        # 모든 노드가 연결이 안되어 있는 경우 idx가 할당되지 않아서 에러가 생김
        try:
            visited[idx] = 1
        # 따라서 에러가 생기면 그냥 현재 연결되어 있는 상태의 key 리스트를 출력하고 끝냄
        except:
            return key

        for e, w in dic[idx]:
            key[e] = min(key[e], key[idx] + w)

    # key 리스트 반환
    return key



v, e = map(int, input().split())
dic = defaultdict(list)
for _ in range(e):
    s, e, w = map(int, input().split())
    dic[s].append((e, w))
    dic[e].append((s, w))
start, end = map(int, input().split())

key_1 = dijk(1)         # 1에서 start, end로 가는 최소값을 구하기 위해
key_v = dijk(v)         # v에서 start, end로 가는 최소값을 구하기 위해
key_start = dijk(start) # start에서 end로 가는 최소값을 구하기 위해

inf = float('inf')
# 만약 1에서 start나 end나 v로 가지 못하거나 그 반대인 경우 연결할 수 없으니 -1 출력
if key_1[start] == inf or key_1[end] == inf or key_1[v] == inf or key_v[start] == inf or key_v[end] == inf or key_v[1] == inf:
    print(-1)
# 그렇지 않을 경우
else:
    a = min(key_1[start]+key_v[end], key_1[end]+key_v[start]) # 1,2번 중 최소값
    b = min(key_1[start]+key_v[start], key_1[end]+key_v[end]) # 3,4번 중 최소값

    # a인 경우 start>end 한 번, b인 경우 두 번 더해서 작은 값을 출력
    if a + key_start[end] < b + key_start[end]*2:
        print(a + key_start[end])
    else:
        print(b + key_start[end]*2)




