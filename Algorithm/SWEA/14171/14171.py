import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):                       # 맨 윗줄과 맨 왼쪽줄 누적합으로 변경
        lst[0][i] += lst[0][i-1]
        lst[i][0] += lst[i-1][0]
    
    for x in range(1, n):                       # 앞서 변경된 숫자들을 제외한 숫자
        for y in range(1, n):                   # lst[1][1] ~ lst[n-1][n-1]까지 순회
            up = lst[x-1][y]                    # 해당 숫자의 뒤쪽, 아래쪽 숫자를 비교해서
            left = lst[x][y-1]                  # 작은 것과 누적합
            if up <= left:
                lst[x][y] += up
            else:
                lst[x][y] += left

    print(f'#{case+1} {lst[-1][-1]}')           # 마지막 숫자 출력

    
        

    
    
    
