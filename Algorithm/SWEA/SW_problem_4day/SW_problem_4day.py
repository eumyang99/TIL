from pprint import pprint
import sys
sys.stdin = open('input.txt')

# dfs 함수
# 해당 노드의 간선정보를 토대로 다음 깊이의 노드로 진입
# 진입하면 해당 visited를 True로 바꾸어 중복 진입 제거
def dfs(node):
    visited[node] = True
    for n in range(100):
        if info_lst[node][n] == 1 and visited[n] == False:
            dfs(n)

T = 10
for case in range(T):
    # case와 간선 수
    C, E = map(int, input().split())
    info_input = list(map(int, input().split()))
    # 노드 정보 들어갈 빈 행렬 생성
    info_lst = [[0]*100 for i in range(100)]
    # 인풋 받은 간선 정보를 빈 행렬에 입력
    for i in range(E):
        info_lst[info_input[2*i]][info_input[2*i+1]] = 1

# 출발지점
    s = 0
# 도착지점
    g = 99
# False로 초기화된 방문 기록 리스트
    visited = [False]*100

# dfs 함수에 시작노드 입력
    dfs(s)

# 해당 시작점에서 도착지점까지 도달했으면
# visited의 도착지점 인덱스는 True로 바뀌었을 것
    if visited[g] == True:
        print(f'#{C} 1')
    else:
        print(f'#{C} 0')