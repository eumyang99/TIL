import sys
sys.stdin = open('input.txt')


##### 받은 리스트로만 풀기
def func(parent):                           # 부모 인덱스
    c_1 = parent*2                          # 자식 인덱스
    c_2 = parent*2 + 1
    for c in c_1, c_2:                      # 자식 인덱스 각각에 대해
        p = parent                          # p는 부모 인덱스 저장
        if c > n:                               # 자식 인덱스가 존재하지 않으면
            return                              # 종료
        while lst[c] < lst[p]:              # 자식이 부모보다 작으면 반복
            lst[c], lst[p] = lst[p], lst[c] # 스왑
            c = p                           # 자식은 부모 인덱스를 갖게 되고
            p = p // 2                      # 부모는 한 층 위로




T = int(input())
for case in range(T):
    n = int(input())
    lst = [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        func(i)

    idx = n // 2
    res = 0
    while idx >= 1:                             # 마지막 인덱스를 타고 부모 노드 합
        res += lst[idx]
        idx = idx // 2

    print(f'#{case+1} {res}')


##### 리스트 만들어서 풀기(왜 이게 더 빠르지?)
def func(value, cnt):                           # 받은 리스트의 첫 value부터 해당 리스트 속 value의 순서(heap리스트의 인덱스 역할)
    heap[cnt] = value                           # heap리스트에 인덱스 맞추어 할당
    p = cnt//2                                  # 부모 노드의 인덱스는 해당 인덱스의 // 2
    while value < heap[p]:                      # 부모가 heap에 추가된 자식 보다 작으면 반복
        heap[cnt], heap[p] = heap[p], heap[cnt] # 스왑
        cnt = p                                 # 자식 인덱스였던 cnt를 부모인덱스로 할당
        p = p // 2                              # 부모 인덱스는 한층 위로



T = int(input())
for case in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = [0]*(n+1)

    cnt = 1
    for value in lst:
        func(value, cnt)
        cnt += 1


    idx = n // 2
    res = 0
    while idx >= 1:
        res += heap[idx]
        idx = idx // 2

    print(f'#{case+1} {res}')


























    



