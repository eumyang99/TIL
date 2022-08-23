import sys
input = sys.stdin.readline

# dfs 검사하는 재귀함수
def rev(s):
    global temp_rev
    global max_rev
    # 방문 했으면 visited에 True
    visited[s] = True
    # 방문한 노드의 수익 temp에 추가
    temp_rev += lst[s][1]
    # 방문한 녀석의 시작일+소요일 이후에 등장하며, [0, 0]이 아니며, 방문하지 않은 노드로 들어감
    for i in range(s+lst[s][0], N):
        if lst[i] != [0,0] and visited[i] == False:
            rev(i)
    # 만약 그곳이 마지막 노드여서 더이상 방문할 수 없다면
    else:
        # 그때 까지 더한 temp가 현재 max보다 클 경우 max 갱신
        if max_rev < temp_rev:
            max_rev = temp_rev
        # 뒤로 돌아가서 다시 새로운 경로 찾아야 하니
        # 노드 나가면서 해당 노드의 수익은 차감
        temp_rev -= lst[s][1]
        # 다른 경로로 다시 돌아올 수도 있으니 visited에 False 재할당
        visited[s] = False


# 자료들을 받고
N = int(input())
lst = [list(map(int, input().split())) for i in range(N)]
# 애초에 정해진 시간 내에 상담을 마치지 못할 녀석들은 [0, 0]으로 바꿈
# [0, 0]으로 되어 있으면 앞으로 고려하지 않을 것
for i in range(N):
    if (i+1) + lst[i][0] > N+1:
        lst[i] = [0,0]

# dfs의 첫 노드가 될 녀석들을 리스트에 담음
s_able = []
# 리스트 처음부터 체크하는데
for i in range(N):
    # 만약 리스트 요소가 아까 고려하지 않기로 한 [0, 0]이 아니면
    if lst[i] != [0,0]:
        # 해당 요소의 시작일+소요일 내에 있는 녀석들을 추가
        for s in range(lst[i][0]):
            s_able.append(s+i)
        # 가장 이른 날에 가능한 녀석을 찾았으면 종료
        break

# 최대 수익 0으로 시작
max_rev = 0
for s in s_able:
    # 중복 방문 확인을 위한 visited
    visited = [False]*N
    temp_rev = 0
    rev(s)

print(max_rev)