import sys
sys.stdin = open("sum_input.txt")

#최대값 구하는 함수
def my_max(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max :
            max = lst[i]
    return max

t = 10
for _ in range(t): # 케이스 개수만큼 10번 반복
    num = int(input()) 
    lst = [] # 빈 리스트를 만들고
    # 숫자 100개를 하나의 리스트로 만들어서 앞서 만든 리스트에 추가(총 100개의 리스트 원소를 갖게 됨)
    for _ in range(100):
        lst.append(list(map(int, input().split())))

    # 100개의 숫자가 들어있는 리스트 원소들의 합 중 가장 큰 값 구하기
    lst_row = [] 
    for i in range(100):
        lst_row.append(sum(lst[i]))
    max_row = my_max(lst_row)

    # 100개의 리스트 원소 중 0번째 값들의 합, 1번째 값들의 합 ... 99번째 값들의 합 중 가장 큰 값 구하기
    lst_col = []
    for idx in range(100):
        sums = 0
        for i in range(100):
            sums += lst[i][idx]
        lst_col.append(sums)
    max_col = my_max(lst_col)

    # 대각선L을 이루는 숫자 원소들의 합 구하기
    crs_L = 0
    for x in range(100):
        crs_L += lst[x][x]

    # 대각선R을 이루는 숫자 원소들의 합 구하기
    crs_R = 0
    for y in range(100):
        crs_R += lst[y][99-y]

    total_sums = [max_row, max_col, crs_L, crs_R] # 위에서 구한 네 가지 값들을 하나의 리스트로 묶고
    max_total_sums = my_max(total_sums) # 그 중 최대값을 추출
    print(f'#{num} {max_total_sums}')



