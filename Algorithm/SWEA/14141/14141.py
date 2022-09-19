import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, hex = input().split()

    print(f'#{case+1}', end=' ')                # 케이스 먼저 출력
    for i in range(int(n)):                     # 문자열 처음부터 순회
        target = hex[i]                         # 각 문자를 target에 할당
        if target.isdigit():                        # 타겟이 숫자면
            for x in range(4-1, -1, -1):                # 해당 숫자를 비트연산으로 출력
                if int(target) & (1<<x):
                    print(1, end='')
                else:
                    print(0, end='')
        else:                                       # 타겟이 문자면
            for x in range(4-1, -1, -1):                # 해당 글자가 의미하는 숫자를 비트연산으로 출력
                if ord(target)-55 & (1<<x):             
                    print(1, end='')
                else:
                    print(0, end='')                
    print()                                     # 줄바꿈 출력
