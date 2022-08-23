T = int(input())
for case in range(T):
    N, K = map(int, input().split())
 
 
    lst = []
    for i in range(N):
        lst.append(list(map(int, (input().split()))))
 
    # 조건에 부합하는 자리가 나오면 cnt+1
    cnt = 0
    # 모든 행에 대해
    for x in range(N):
        # 해당 행에 1의 개수가 K보다 작다면 자리는 절대 존재할 수 없으니 넘어감
        if lst[x].count(1) < K:
            continue
        # 해당 행의 첫 배열이 111...111(K개)0이면 +1
        if lst[x][:K+1] == [1]*K + [0]:
            cnt += 1
        # 해당 행의 마지막 배열이 0111...111(K개)이면 +1
        if lst[x][-K-1:] == [0] + [1]*K:
            cnt += 1
        # 그리고 그 사이에 0111...111(K개)0이 존재하면 +1
        for h in range(N-K+1):
            if lst[x][h:h+5] == [0] + [1]*K + [0]:
                cnt += 1
    
    # 주어진 행렬을 전치행렬로 바꾸어 위의 for문을 재사용
    for x in range(N-1, -1, -1):
        for y in range(N-1-x):
            lst[x][1+y+x], lst[1+y+x][x] = lst[1+y+x][x], lst[x][1+y+x]
    
    # 각 열에 대한 검사를 똑같이 함
    for x in range(N):
        if lst[x].count(1) < K:
            continue
        if lst[x][:K+1] == [1]*K + [0]:
            cnt += 1
        if lst[x][-K-1:] == [0] + [1]*K:
            cnt += 1
        for h in range(N-K+1):
            if lst[x][h:h+K+2] == [0] + [1]*K + [0]:
                cnt += 1
 
    print(f'#{case+1} {cnt}')