import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    a = round(n**(3**-1))       # a에 n의 세제곱근을 반올림해서 할당
    b = a**3                    # 양의 정수인 세제곱근이 존재한다면
                                    # 부동소수점을 고려하더라도
                                    # 다시 세제곱했을 때 본인으로 돌아와야함
                                # 세제곱근이 존재하지 않는다면
                                    # round가 오히려 격차를 키워
                                    # 세제곱햇을 때 본인으로 돌아올 수 없음
                                # b에 a의 세제곱을 할당

    if b == n:                  # 다시 세제곱했을 때 본인으로 돌아왔다면
        print(f'#{case+1} {a}') # 세제곱근 출력
    else:                       # 아니면 -1 출력
        print(f'#{case+1} -1')