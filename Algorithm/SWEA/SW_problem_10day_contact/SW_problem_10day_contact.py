from collections import defaultdict, deque
import sys
sys.stdin = open('input.txt')


# 리스트 활용
T = 10
for case in range(T):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    dic = defaultdict(list)
    for i in range(n//2):                   # 간선 정보 dict로 받음
        p, c = lst[i*2], lst[i*2+1]         # 시작점 : {도착점들}
        if c not in dic[p]:
            dic[p].append(c)

    visited = set()                         # visited 생성
    visited.add(s)                          # 시작점 방문처리

    lst = [s]                               # lst에 시작점 넣고
    while 1:
        next_lst = []                       # 다음 전화받을 사람들 lst
        for i in lst:                       # lst에 있는 녀석들 각각에 대해
            for x in dic[i]:                # 그들이 걸 수 있는 사람들을
                if x not in visited:        # 방문조건이 맞으면
                    visited.add(x)          # 방문처리하고
                    next_lst.append(x)      # next_lst에 추가
        if next_lst:                        # 만약 next_lst가 있으면
            lst = next_lst[:]               # lst를 next_lst로 초기화하고 while문으로
        else:                               # 만약 next_lst가 비어 있으면
            break                           # while문 종료하고

    print(f'#{case+1} {max(lst)}')          # lst에 있는 녀석들 중 최대값 출력


# bfs 활용
T = 10                                  
for case in range(T):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))   
    dic = defaultdict(list)                 # 간선정보 dict로 받음
    for i in range(n//2):                   # # 시작점 : {도착점들}
        p, c = lst[i*2], lst[i*2+1]
        if c not in dic[p]:
            dic[p].append(c)
    
    dic_cnt = defaultdict(list)             # 각 노드에 대한 몇번째 전화인지 카운트할 새로운 리스트
    dic_cnt[s] = 0                          # 시작 노드에는 0을 할당
    visited = set()                         # visited 생성
    que = deque()                           # que생성
    visited.add(s)                          # 시작점 방문처리
    que.append(s)                           # 시작점 que에 추가

    while que:                                  # que가 비어있지 않다면
        p = que.popleft()                       # que를 pop해서 p에 할당
        nodes = dic[p]                          # nodes에는 p가 전화를 걸 수 있는 녀석들을 할당
        for node in nodes:                      # nodes 각각 node에 대해
            if node not in visited:             # 해당 node가 방문되지 않았다면
                dic_cnt[node] = dic_cnt[p] + 1  # dic_cnt[자식노드]는 dic_cnt[부모노드]의 cnt보다 +1 키움
                visited.add(node)               # node 방문처리
                que.append(node)                # node que에 추가

    max_value = max(dic_cnt.values())           # dic_cnt의 밸류(cnt) 중
                                                #가장 큰 녀석을 찾아 max_value에 할당


    # dic_cnt의 value값이 max_value 인 keys들 x에 대해 x들로 이루어진 리스트
    # 그 리스트의 max 값 출력
    res = max([x for x in dic_cnt.keys() if dic_cnt[x] == max_value])
    
    print(f'#{case+1} {res}')



##     def sort_key(key_value):
##         key, value = key_value
##         return (value, key)
##     sorted(lst, key=sum, reverse=True)

    

    

