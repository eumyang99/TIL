import sys
sys.stdin = open("input.txt")


T = int(input())
for case in range(T):
    N, K = map(int, input().split())

    # 모든 부분 집합 구해서 result에 담고
    lst = list(range(1,13))
    result = []
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(lst[j])
        result.append(temp)

    cnt = 0
    # result에 담긴 부분집합을 하나씩 꺼내서
    for i in result:
        # 그 녀석의 길이가 N이면서
        if len(i) == N:
            # 합이 K이면
            if sum(i) == K:
                # 카운트 +1
                cnt += 1
    print(f'#{case+1} {cnt}')
