from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, E = map(int, input().split())

    adj = [[11*(N+1)]*(N+1) for _ in range(N+1)]        # adj는 행 -> 열로 갈 수 있으면 가중치를
    for i in range(N+1):                                # 갈 수 없으면 무한값을
        adj[i][i] = 0                                   # 행 == 열이면 0을 갖는 리스트

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  
    print(adj)
    res_lst = [0] + [11*(N+1)]*(N)                      # 0으로 부터 리스트의 각 노드(리스트의 idx)까지의 최소 거리

    q = deque([0])                                      # 시작점 0을 큐에 넣고
    while q:
        start = q.popleft()                             # 큐에서 팝한 것은 새로운 시작점
        for i in range(N+1):                            # 갈 수 있는 노드 전체를 순회하며
            # 자기 자신은 제외, 시작점에서 도착노드 거리 + 시작점까지의 누적거리가 계산된 최종 목적지 까지의 거리보다 작다면 
            if i != start and 0 < res_lst[start] + adj[start][i] < res_lst[i]:
                # 그리고 시작점에서 도착노드 거리 + 시작점까지의 누적거리가 이미 계산된 도착지점까지의 거리보다 짧다면
                if  res_lst[start] + adj[start][i] < res_lst[i]:
                    # 해당 노드까지의 누적값 갱신
                    res_lst[i] = res_lst[start] + adj[start][i]
                # 도착지점에서는 탐색할 필요가 없으니 도착지점은 q에 추가하지 않음
                if i != N:
                    q.append(i)
                

    print(f'#{case+1} {res_lst[N]}')
    







