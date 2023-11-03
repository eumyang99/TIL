import sys
input = sys.stdin.readline

## 발상
## 1. 현재 빌딩에서 왼쪽으로 볼 수 있는 건물들
## 2. 현재 빌딩에서 오른쪽으로 볼 수 있는 건물들
## 두 경우로 나누어 각각 stack을 사용해서 해결

## 각 방향에서 진행 아래와 같이 진행
## 현재 방문한 빌딩보다 작거나 같은 빌딩이 stack에 없을 때까지 pop을 하고 cnt(stack의 길이 = 보이는 빌딩 개수) -= 1
    ## * 스택은 내림차순으로 저장됨

    ## 1. 스택이 비어있지 않다면 해당 방향에서 보이는 빌딩이 있다는 것
        ## 가장 가까운 빌딩(마지막 stack)의 번호를 near[현재 빌딩 번호]에 저장

    ## 2. 스택이 비어있다면 보이는 빌딩이 없으니 near에 저장하지 않음

    ## 3. 스택에 현재 빌딩을 저장하고 cnt += 1

    ## 4. cnt를 res[현재 빌딩 번호]에 저장

## 이후 res와 near를 참조하여 출력

n = int(input())
arr = [0] + list(map(int, input().split()))

## res : 빌딩 번호 idx에 보이는 빌딩 개수 저장
res = [0] * (n+1)
## near : 빌딩 번호 idx에 보이는 빌딩 중 가장 가까운 빌딩 번호 저장
near = [[] for _ in range(n+1)]

## 좌에서 우로 진행 : 왼쪽 방향으로 보이는 빌딩 탐색
## 첫번째 빌딩을 스택에 추가
stack = [(arr[1], 1)]
## cnt : stack 길이 - 1(자기 자신은 못보기 때문) 
cnt = 0
## 두번째 빌딩부터 마지막 빌딩까지 순회
for i in range(2, n+1):
    ## 현재 빌딩과 stack에 저장된 빌딩을 비교
    ## stack은 내림차순이기 때문에 마지막 빌딩의 높이가 가장 작음
    ## 현재 빌딩보다 작은 빌딩들은 모두 pop하고 cnt를 줄임
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
        cnt -= 1

    ## stack이 있다면 보이는 빌딩이 있다는 의미
    ## 해당 빌딩 번호를 near[현재 빌딩 번호]에 저장
    if stack:
        near[i].append(stack[-1][1])

    ## 현재 빌딩 stack에 추가
    stack.append((arr[i], i))
    ## cnt 추가
    cnt += 1
    ## 보이는 빌딩 개수 저장
    res[i] += cnt


## 우에서 좌로 진행 : 오른쪽 방향으로 보이는 빌딩 탐색
## 마지막 빌딩을 스택에 추가
## 이하 상동
stack = [(arr[-1], n)]
cnt = 0
for i in range(n-1, 0, -1):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
        cnt -= 1

    if stack:
        near[i].append(stack[-1][1])

    stack.append((arr[i], i))
    cnt += 1
    res[i] += cnt

## 출력
for i in range(1, n+1):
    if res[i]:
        print(res[i], end = " ")
        if len(near[i]) == 1:
            print(near[i][0])
        else:
            if abs(i - near[i][0]) <= abs(i - near[i][1]):
                print(near[i][0])
            else:
                print(near[i][1])
    else:
        print(0)