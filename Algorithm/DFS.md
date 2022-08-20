# DFS(깊이 우선 탐색)

- **그래프에서 노드와 간선 정보를 토대로, 먼저 가능한 한 깊이 들어가는 우선순위로 모든 경로를 탐색할 수 있는 방법이다.**

- 노드와 간선의 정보를 2차원 배열에 담을 수도, 딕셔너리에 담을 수도, 리스트에 담을 수도 있고 여러 방법이 있다.

- **탐색을 하는 방법**

  - 스택을 명시적으로 사용하는 방법
  - 재귀호출을 사용하는 방법이 있다.

- **주의할 점**

  - 간선이 단방향인지 양방향인지를 인지하여 정보를 저장할 것

  - 한번 방문한 곳을 재방문 하지 않도록 방문한 곳을 기록하는 정보를 저장할 것

    

- 내 손에 먼저 익은 것은 2차원 배열로 정보를 담아 재귀호출을 사용하여 탐색하는 방법이다.

- SWEA S/W 문제해결 기본 - 길찾기 문제로 코드 예시

```python
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
    # 인풋 받은 간선의 정보를 빈 행렬에 입력, a -> b 이동이 가능하면 info_lst[a][b] = 1
    ### 간선의 정보가 '0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7'
    ### 이렇게 들어오기 때문에 두 칸씩 나누어 정보를 입력
    for i in range(E):
        info_lst[info_input[2*i]][info_input[2*i+1]] = 1
        # 만약 간선이 양방향일 경우
        # info_lst[info_input[2*i+1]][info_input[2*i]] = 1 를 추가
 
# 출발지점 고정
    s = 0
# 도착지점 고정
    g = 99
# False로 초기화된 방문 기록 리스트
# visited의 인덱스가 노드와 매핑 
# 노드 개수만큼의 False를 갖고 있어야 한다.
    visited = [False]*100
 
# dfs 함수에 시작노드 입력
    dfs(s)
 
# 해당 시작점에서 도착지점까지 도달했으면
# visited의 도착지점 인덱스는 True로 바뀌었을 것 
    if visited[g] == True:
        print(f'#{C} 1')
    else:
        print(f'#{C} 0')
```

- 상황에 따라 A경로를 통해 마지막 노드를 방문하고 다시 나와 B경로를 통해서 다시 방문했던 노드를 재방문 해야 할 수도 있다.
  - 예를 들어 간선이 있다는 가정 하에
    - a -> b -> c -> d
  
    - a -> b -> d
  
    - a -> c -> d
  
    - a -> d
  
  - 위의 네 경우를 다르게 판단해야 하는 상황이 있을 수 있다. 

```python
def dfs(s):
    # 방문 했으면 visited에 True
    visited[s] = True
    for ~ :
        if info_lst[node][n] == 1 and visited[n] == False:
            dfs(i) # 한 depth 깊게 들어감
    # 만약 그곳이 해당 경로의 마지막 노드여서 더이상 깊게 들어갈 수 없다면
    else:
		생략
        # 그 노드의 visited를 다시 False로 바꾸어 다시 방문할 수 있도록 한다
        visited[s] = False
```

- 위와 같은 맥락으로 어떤 노드들로 연결된 경로의 경우인지를 구분하여 탐색할 수도 있다.

  

---



### 소해

- 노드와 간선의 정보를 2차원 배열이 아닌 다른 방법으로 저장하여 사용하는 방법을 더 연습할 필요성을 느낀다.
- 탐색 방법 역시 재귀호출 말고 스택을 이용하는 것도 연습해 봐야겠다.
