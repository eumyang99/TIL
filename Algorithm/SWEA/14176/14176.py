import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]   # 2차원 배열로 인풋
    lst.sort(key=lambda x : x[1])                               # 끝나는 시간 기준 오름차순으로 lst 정렬

    res = 1                         # 문제조건 상 첫 화물차 1개는 무조건 가능
    end = lst[0][1]                 # 첫 화물차의 끝나는 시간을 end에 할당

    for i in range(n):              # 리스트를 순회하면서
        if lst[i][0] >= end:        # 시작시간이 end 보다 같거나 미래라면
            res += 1                # res +1
            end = lst[i][1]         # end는 해당 화물차의 끝나는 시간으로 초기화    

    print(f'#{case+1} {res}')