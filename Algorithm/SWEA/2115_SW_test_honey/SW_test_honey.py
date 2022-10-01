import sys
sys.stdin = open('input.txt')


# 한 일꾼이 채취할 수 있는 벌꿀 범위에서 가장 많은 수익을 내는 경우를 부분집합을 사용해서 구함
def power_set(lst):                         
    max = 0                                 # 채취할 수 있는 벌꿀 범위에서 가장 높은 수익을 내는 값
    for i in range(1 << m):       
        temp_sum = 0                        # 수익화했을 때의 값을 누적하는 변수
        limit = 0                           # 채취할 수 있는 최대 양을 체크할 변수
        for j in range(m):
            if i & (1 << j):                # 해당 벌통을 채취했을 때
                limit += lst[j]             # limit에 채취한 벌꿀 양을 누적
                if limit > c:               # 누적된 양이 최대 한도를 초과했다면
                    break                   # 해당 부분집합에 대응하는 벌통 채취 조합은 불가능하니
                                            # 다음 부분집합으로 넘어감

                temp_sum += (lst[j]**2)     # temp_sum에 해당 벌통을 수익화했을 때 금액을 누적
        if temp_sum > max:                  # 이번 부분집합의 누적 수익량이 max보다 높다면
            max = temp_sum                  # max 갱신
    return max                              # max 반환



T = int(input())
for case in range(T):
    n, m, c = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    sum_lst = [[0]*(n-m+1) for _ in range(n)]


    for x in range(n):                                  # 한 일꾼이 채취할 수 있는 벌꿀 범위에서 가장 많은 수익을 내는 경우를 찾아 sum_lst에 추가
        for y in range(n-m+1):                          # m이 3이면 0,1,2 // 1,2,3 // 2,3,4 // ... 벌통에서 가능한 수익 중 최대를 찾는 것
            sum_lst[x][y] = power_set(lst[x][y:y+m])    # 0,1,2 의 최대 수익은 sum_lst[][0]에 // 1,2,3의 최대 수익은 sum_lst[][1]에 담는다



    # sum_lst의 가로줄의 최대값 두 개를 더하면 될 것 같지만
    # 그렇지 않을 경우도 있다.
    # 예를 들어 [100, 70, 100], [1, 90, 1], [1, 80, 1]이 가능할 때
    # 각 가로줄의 최대값을 더하면 190이지만 첫 줄에 두 명이 모두 채취한다면 200을 얻을 수도 있다
    # 따라서 이 경우도 찾아야 한다. 
    row_max = []                                            
    for x in range(n):                                          # 각 가로줄에 대해
        row_temp = 0
        for y in range(n-2*m+1):                                # 가로줄에서 두명이 채취할 경우의 최대값을
            temp_sum = sum_lst[x][y] + max(sum_lst[x][y+m:])
            if temp_sum > row_temp:
                row_temp = temp_sum
        row_max.append(row_temp)                                # row_max에 담는다
    one_line = max(row_max)                                     # 한 줄에서 두명이 채취할 때의 최대값을 one_line에 할당


    temp = []                                                   # 이번엔 서로 다른 가로줄에서 채취할 경우의 최대값을
    for i in range(n):
        temp.append(max(sum_lst[i]))
    temp.sort()
    two_line = temp[-1] + temp[-2]                              # two_line에 담는다

    if one_line > two_line:                                     # one_line과 two_line 중 큰 것을 출력한다
        print(f'#{case+1} {one_line}')
    else:
        print(f'#{case+1} {two_line}')


