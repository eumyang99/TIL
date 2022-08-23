import sys
input = sys.stdin.readline

T = int(input())

# 스택 생성
num_stack = []

# T번 인풋 받을 예정
for i in range(T):
    order = input()

    # 만약 인풋 받은 문자의 첫 4개가 'push'면
    # 인풋 받은 문자를 나누어 스택에 추가할 숫자를 num에 저장
    if order[:4] == 'push':
        t, num = order.split()
        num_stack.append(num)

    # 'pop'이면
    elif order[:3] == 'pop':
        # 스택에 숫자가 있을 경우 팝하며 출력
        if num_stack:
            print(num_stack.pop())
        # 스택이 비었으면 -1 출력
        else:
            print(-1)

    # 'size'이면
    elif order[:4] == 'size':
        # 스택 길이 출력
        print(len(num_stack))

    # 'empty'이면
    elif order[:5] == 'empty':
        # 스택에 뭐가 있으면 0 출력
        if num_stack:
            print(0)
        # 아니면 1 출력
        else:
            print(1)

    # 'top'이면
    else:
        # 스택에 뭐가 있으면 스택 마지막 요소 출력
        if num_stack:
            print(num_stack[-1])
        # 아니면 -1 출력
        else:
            print(-1)