import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = float(input())
    temp = []
    for i in range(1, 14):                      # 13자리까지 나오면 실패
        if n - 2**(-i) >= 0:                        # n에서 2의 -i승을 차례대로 차감하면서 
            n -= 2**(-i)                                # 그 값을 차감했을 때 여전히 양수이면 
            temp.append('1')                            # i번째는 1
        else:                                           # 차감했을 때 음수이면
            temp.append('0')                            # i번째는 0
        if n == 0:                                  # 13번째까지 가기 전에 값이 n이 0이 되었으면 성공
            break

    if len(temp) != 13:                         # temp의 길이가 13이 아니라면
        print(f'#{case+1} {"".join(temp)}')         # temp출력
    else:                                       # temp의 길이가 13이면
        print(f'#{case+1} overflow')                # overflow 출력


