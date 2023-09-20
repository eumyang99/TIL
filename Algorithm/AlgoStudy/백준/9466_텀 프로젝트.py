import sys
input = sys.stdin.readline

## 발상
## 사이클이 되는 학생 집단을 찾는다

def uu():
    n = int(input())
    lst = list(map(int, input().split()))

    ## used = 이미 사용 확인 처리된 학생들
    used = set()

    ## able = 사이클이 형성된 학생 수
    able = 0

    ## visited = 방문 리스트 = [다음 학생 번호, 타고 들어간 깊이]
    ## 첫번째 값이 -1이면 방문하지 않은 것
    visited = [[-1, 0]] * n

    ## 학생들을 순회하면서
    for idx, next_num in enumerate(lst):
        ## 이미 확인 처리 되지 않은 녀석이라면
        if idx not in used:
            next = next_num - 1
            ## 방문처리하고
            visited[idx] = [next_num - 1 , 1]
            ## 추후 used에 추가하고 visited를 원상복구하는 리스트
            ## 체인이 연결되는 모든 학생들을 저장
            temp_used = [idx]
            ## 깊이
            cnt = 1
            ## 다음 녀석이 확인 처리되지 않은 녀석이라면
            while next not in used:
                ## 그리고 방문처리 되지 않은 녀석이라면
                if visited[next][0] == -1:
                    ## 방문처리하고
                    visited[next] = [lst[next] - 1, cnt + 1]
                    ## 체인이 연결되었으니 temp_used에 저장
                    temp_used.append(next)
                    ## 다음 녀석으로 갱신
                    next = lst[next] - 1
                    cnt += 1
                ## 이미 방문한 녀석이라면 사이클이 형성된 것
                else:
                    ## 전체 깊이에서 사이클이 시작되는 녀석의 깊이를 빼면 사이클이 형성된 학생 수
                    able += cnt - visited[next][1] + 1
                    ## 다음 학생 확인을 위해 while문 탈출
                    break
            
            ## 다음 녀석이 이미 확인처리 된 녀석이라면 사이클 형성이 될 수 없음
            ## 현재까지 연결된 모든 녀석을 확인처리하고
            used.add(next)
            used.add(i for i in temp_used)
            ## 현재까지 연결된 모든 녀석들의 방문처리를 취소
            visited[next] = [-1, 0]
            for i in temp_used:
                used.add(i)
                visited[i] = [-1, 0]

    ## 전체 학생 수에서 사이클 형성이 된 학생 수를 빼서 출력
    print(n - able)

t = int(input())
for _ in range(t):
    uu()

