import sys
sys.stdin = open('input.txt')

### 힙과 다르게
### 이진 탐색 트리는 가장 높은 루트를 기준으로
### 왼쪽의 모든 서브 노드보다 커야하고
### 오른쪽의 모든 서브 노드보다 작아야 한다. 

# 중위순회를 통한 트리 구현
def inorder(node):
    global cnt
    if node <= n:
        inorder(node*2)
        tree[node] = cnt
        cnt += 1
        inorder(node*2 +1)
        
T = int(input())
for case in range(T):
    n = int(input())

    tree = [0]*(n+1)
    cnt = 1

    inorder(1)
    print(f'#{case+1} {tree[1]} {tree[n//2]}')

