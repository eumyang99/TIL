from collections import deque
import sys
input = sys.stdin.readline

## 내 풀이
## BFS 사용
n, k = map(int, input().split())
if k <= n:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end=" ")
else:
    visited = [0]*100001
    visited[n] = 1

    start = [(n, [n], 0)] # 숫자, 루트, 비용
    que = deque(start)
    while que:
        num, route, cost = que.popleft()
        if num == k:
            print(cost)
            print(*route)
            break

        for next_num in [num-1, num+1, num*2]:
            if 0 <= next_num <= 100000 and not visited[next_num]:
                visited[next_num] = 1
                que.append((next_num, route + [next_num], cost+1))



## 경로를 que에 담지 않는 효율적이 방법(Java 코드 chatGPT로 번역)
## BFS + parent : [최단거리, 경로] 를 알아내야 하는 경우에 좋은 방법
from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
parent = [0] * 100001

def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        if now + 1 <= 100000 and visited[now + 1] == 0:
            visited[now + 1] = visited[now] + 1
            parent[now + 1] = now
            q.append(now + 1)
        if now - 1 >= 0 and visited[now - 1] == 0:
            visited[now - 1] = visited[now] + 1
            parent[now - 1] = now
            q.append(now - 1)
        if now * 2 <= 100000 and visited[now * 2] == 0:
            visited[now * 2] = visited[now] + 1
            parent[now * 2] = now
            q.append(now * 2)

        if visited[end] != 0:
            return

bfs(N, K)
print(visited[K] - 1)

stack = []
idx = K
while idx != N:
    stack.append(idx)
    idx = parent[idx]
stack.append(idx)

while stack:
    print(stack.pop(), end=' ')
 


## 풀이 참고
## 가장 효율적인 풀이
def F(N,K):
    if N>=K:
        return N-K,[*range(N,K-1,-1)]
    elif K==1:
        return 1,[0,1]
    elif K%2:
        A=F(N,K-1)
        B=F(N,K+1)
        if A[0]<B[0]:
            return A[0]+1,A[1]+[K]
        else:
            return B[0]+1, B[1]+[K]
    else:
        B=F(N,K//2)
        if K-N<B[0]+1:
            return K-N,[*range(N,K+1)]
        else:
            return B[0]+1,B[1]+[K]
N,K=map(int,input().split())
R=F(N,K)
print(R[0])
print(*R[1])