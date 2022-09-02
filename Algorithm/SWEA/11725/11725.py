from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


# T = int(input())
# for case in range(T):
n = int(input())
dic = {i : [] for i in range(1, n+1)}       # 간선 정보를 dic 형태로 저장
for _ in range(n-1):
    x, y = map(int, input().split())        # 양방향으로 저장
    dic[x].append(y)
    dic[y].append(x)


# DFS
stack = []                          # 스택 만들고
stack = [1]                         # 시작점 추가
visited = [False]*(n+1)             # 인덱스 편하게 n+1개
visited[1] = True                   # 시작점 방문 기록
res = [0]*(n+1)                     # 인덱스 편하게 n+1개

while stack:                        # 스택이 없어질 때까지
    h = stack.pop()                 # 스택 pop
    for i in dic[h]:                # pop한 녀석의 간선을 토대로
        if visited[i] == False:     # 다음 녀석을 방문하지 않았다면
            visited[i] = True       # 방문체크하고
            stack.append(i)         # 스택에 추가
            res[i] = h              # h는 i의 부모 노드가 됨

for i in res[2:]:                   # 인덱스 감안해서 res출력
    print(i)


    
# BFS
# DFS와 다 같고 왼쪽에서 팝하냐 오른쪽에서 팝하냐 차이만 있음
que = deque()                       
que.append(1)
visited = [False]*(n+1)
visited[1] = True
res = [0]*(n+1)

while que:
    h = que.popleft()
    for i in dic[h]:
        if visited[i] == False:
            visited[i] = True
            que.append(i)
            res[i] = h

for i in res[2:]:
    print(i)




