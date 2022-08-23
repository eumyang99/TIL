T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
 
    # 버블 정렬 후 하나씩 출력
    for x in range(N-1):
        for i in range(N-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
 
    print(f'#{case+1}', end=' ')
    for i in lst:
        print(i, end=' ')
    print()