import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    v, e = map(int, input().split())
    dic = {i+1 : [] for i in range(v)}

    for i in range(e):
        x, y = map(int, input().split())
        dic[x].append(y)
        dic[y].append(x)

    s, g = map(int, input().split())

    queue = []
    visited = [False]*(v+1)
    visited[s] = True
    dist = [0]*(v+1)

    def exp(s):
        for i in dic[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[s] + 1
        if visited[g] == True:
            return True
        if len(queue) == 0:
            return 0
        elif exp(queue.pop(0)) == True:
            return True

    exp(s)
    print(f'#{case+1} {dist[g]}')

