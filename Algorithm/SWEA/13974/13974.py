import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    v, e = map(int, input().split())
    dic = {i+1 : [] for i in range(v)}          # 간선 정보를 받기 위한 dict 생성
                                                # 인덱스 편하게 더미 생성

    for i in range(e):                          # dict에 간선 정보 저장
        x, y = map(int, input().split())        
        dic[x].append(y)
        dic[y].append(x)

    s, g = map(int, input().split())            # 시작점, 목표점

    queue = []                                  # 큐 생성
    visited = [False]*(v+1)                     # visited 생성, 인덱스 편하게 더미 생성
    visited[s] = True                           # 시작점은 True로 할당
    dist = [0]*(v+1)                            # 거리 정보 리스트 생성

    def exp(s):                                 # 시작점을 함수에 입력
        for i in dic[s]:                        # 시작점에 연결되는 노드들에 대해
            if visited[i] == False:             # 해당 노드가 방문되지 않아 False면
                queue.append(i)                 # 큐에 append
                visited[i] = True               # visited에 True
                dist[i] = dist[s] + 1           # 현재까지 이동한 거리 dist[s]에 +1을 하고 이동할 수 있는 지점에 할당
        if visited[g] == True:                  # 목표지점을 방문할 수 있는 지 확인
            return True                             # 가능하면 True 반환
        if len(queue) == 0:                     # 큐에 남아 있는 게 없다면
            return 0                            # 갈 수 있는 모든 곳을 가본 것이니 0 반환
        elif exp(queue.pop(0)) == True:         # 큐가 남아 있다면 가장 먼저 들어온 녀석부터 함수에 입력
            return True                         # 만약 들어간 함수가 목표점을 찾아서 True가 되었다면
                                                # 앞선 함수도 True로 반환, 차례로 함수 빠져나옴

    exp(s)                                      # 함수 실행 후
    print(f'#{case+1} {dist[g]}')               # 목표지점의 거리 반환

