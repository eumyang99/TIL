import sys
input = sys.stdin.readline

marking = [0, 2, 1]

def check():
    v, edge = map(int, input().split())
    edges = [[] for _ in range(v+1)]
    for _ in range(edge):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)

    visited = [0] * (v+1)
    for i in range(1, v+1):
        if visited[i]: continue
        visited[i] = 1
        stack = [i]
        while stack:
            s = stack.pop()
            for e in edges[s]:
                if not visited[e]:
                    visited[e] = marking[visited[s]]
                    stack.append(e)
                    continue
                if visited[e] == visited[s]:
                    return "NO"
                
    return "YES"

t = int(input())
for _ in range(t):
    print(check())
