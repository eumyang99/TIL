from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    fire, n = map(int, input().split())         # 화덕 크기와 피자 개수
    lst = list(map(int, input().split()))       # 피자 치즈 정보
    pizza = []
    for i in range(len(lst)):
        pizza.append([lst[i], i+1])             # 피자 치즈정보와 피자 넘버링


    que = deque()                               # 큐 생성
    for i in range(fire):                       # 화덕 크기만큼 큐에 피자 넣음
        que.append(pizza.pop(0))


    while len(que) != 1:                        # 큐가 1 남을 때까지 반복
        if que[0][0] == 0:                      # 화덕입구의 피자가 0이면
            que.popleft()                       # 그 피자 pop
            if pizza:                           # 만약 더 넣을 피자가 있다면
                que.appendleft(pizza.pop(0))    # pop한 자리에 append
        else:                                   # 화덕입구의 피자가 0이 아니면
            que[0][0] //= 2                     # 2로 나누고
            que.append(que.popleft())           # 큐 맨뒤로 보냄

    print(f'#{case+1} {que[0][1]}')             # 큐가 하나 남았을 때 그 녀석의 넘버링 출력
