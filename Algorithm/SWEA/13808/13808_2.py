import sys
sys.stdin = open('input.txt')


T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    info_lst = [[0] * (V+1) for i in range(V+1)]
    info = []
    for i in range(E):
        info.append(list(map(int, input().split())))

    for i in info:
        info_lst[i[0]][i[1]] = 1

    sg = list(map(int, input().split()))

    visited = [False] * (V+1)
    visited[sg[0]] = True


    def dfs(n):
        for i in range(1, V+1):
            if info_lst[n][i] == 1 and visited[i] == False:
                visited[i] = True
                dfs(i)


    dfs(sg[0])
    if visited[sg[1]] == True:
        print(f'#{case + 1} 1')
    else:
        print(f'#{case + 1} 0')




