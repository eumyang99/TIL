from collections import deque
import sys
sys.stdin = open('input.txt')

def func():
    while 1:
        obj, cnt= q.popleft()                       # 연산 대상과 해당 숫자의 cnt를 같이 들고 다님
        for n_obj in obj*2, obj+1, obj-1, obj-10:   # 각 연산에 대해
            if 1 <= n_obj <= 1000000:               # 연산 결과가 범위 안에 있으면서
                if n_obj != m:                          # 원하는 숫자가 아닐 경우
                    if n_obj not in visited:                # visited 확인 후
                        visited.add(n_obj)                      # visited에 추가
                        q.append([n_obj, cnt+1])                # q에 추가
                else:                                   # 원하는 숫자를 찾은 경우
                    print(f'#{case+1} {cnt+1}')             # cnt +1 출력 후 종료
                    return

T = int(input())
for case in range(T):
    n, m = map(int, input().split())

    cnt = 0
    q = deque()
    q.append([n, 0])
    visited = set()         # 연산 결과가 같은 숫자로 나올 경우 먼저 발견된 녀석이 더 최적
                            # 중복을 방지하려 visited 생성

    func()        

    