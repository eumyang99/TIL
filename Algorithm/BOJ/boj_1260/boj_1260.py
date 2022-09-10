from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m, v = map(int, input().split())         # 간선 정보를 dict 형태로 받음
dic = {i:[] for i in range(1, n+1)}
for _ in range(m):
    p, q = map(int, input().split())
    dic[p].append(q)                # 양방향이니까 양쪽 다 기입
    dic[q].append(p)
for i in dic:                       # 정렬
    dic[i].sort()


# DFS
def dfs(h):
    for i in dic[h]:
        if i not in visited:
            visited.add(i)
            print(i, end=' ')
            dfs(i)

visited = set()             # 방문기록
visited.add(v)              # 시작점 방문
print(v, end=' ')           # 시작점 먼저 출력
dfs(v)
            

print()

# BFS
que = deque()               # 큐 생성
visited = set()             # 방문기록
que.append(v)               # 큐에 시작점 추가
visited.add(v)              # 시작점 방문
print(v, end=' ')           # 시작점 먼저 출력
while que:
    h = que.popleft()
    for i in dic[h]:
        if i not in visited:
            que.append(i)
            visited.add(i)
            print(i, end=' ')