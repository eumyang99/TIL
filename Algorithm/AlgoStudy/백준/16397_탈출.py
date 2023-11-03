from collections import deque
import sys
input = sys.stdin.readline

## 발상
## bfs로 접근한다
## que에 (숫자, cnt)를 담는다
## pop한 숫자를 두 가지 숫자로 바꾸고
## 두 숫자가 범위 안에 있으면서 버튼 기회 안에 있고 먼저 방문된 녀석이 아니라면(먼저 방문된 녀석이 무조건 최소 횟수) que에 담는다
## 목표 숫자를 찾으면 출력한다
n, t, g = map(int, input().split())

visited = [0] * 100000
que = deque([(n, 0)])
while que:
    num, cnt = que.popleft()
    if num == g:
        print(cnt)
        break

    ## 1 더하기
    add = num + 1
    if add <= 99999 and cnt < t and not visited[add]:
        visited[add] = 1
        que.append((add, cnt+1))

    ## 2 곱하고 큰 자리 1 빼기
    multi = num * 2
    if multi <= 99999:
        for i in range(5):
            if 1 <= multi // (10**i) <= 9:
                multi -= 10**i
                if cnt < t and not visited[multi]:
                    visited[multi] = 1
                    que.append((multi, cnt+1))
                    break
else:
    print("ANG")
        
