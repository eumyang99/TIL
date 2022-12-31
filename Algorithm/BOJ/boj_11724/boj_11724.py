import sys
input = sys.stdin.readline




#### DFS 풀이법
from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict(list)

for _ in range(m):                      # 양방향이기 때문에 s와 e를 모두 key값으로 받는다
    s, e = map(int, input().split())
    dic[s].append(e)
    dic[e].append(s)

res = 0                                 # 출력할 결과
used = set()                            # 이미 확실히 사용된 노드

for s in dic:                           # dic의 key값들을 순회하며
    if s not in used:                   # 해당 key값이 사용되지 않았다면
        stack = []                          # 스택을 만들고
        visited = set()                     # visited를 만들고
        stack.append(s)                     # s를 스택과 visited에 넣는다
        visited.add(s)
        used.add(s)                         # 이 노드는 필수적으로 사용되니 used에 넣는다

        while stack:                        # 이제 while문으로 bfs를 돌림
            for node in dic[stack[-1]]:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)
                    used.add(node)          # 추가된 노드는 사용된 노드이므로 used에도 추가
                    break
            else:
                stack.pop()
    
        res += 1                            # 한 BFS가 끝났다면 하나의 연결노드를 찾은 것이니 res에 추가

res += n - len(used)                        # 간선을 갖지 않고 노드만 있는 정점도 하나의 연결 노드이기 때문에
                                            # 전체 노드에서 사용된 노드 개수를 차감해서 res에 더한다
print(res)


#### BFS 풀이법