import sys
sys.stdin = open('input.txt')


T = 10
for case in range(T):
    size = int(input())
    word = input()

    stack = []  # 연산자를 담을 스택
    post = ''  # 후위표기법으로 식을 담을 빈 문자열
    for i in word:  # 문자를 하나씩 꺼내서
        if i == '+' or i == '-':  # 만약 i가 '+'일 때
            if not stack:  # 스택이 비었으면
                stack.append(i)  # 스택에 i 추가
            elif stack[-1] == '+' or stack[-1] == '-':  # 스택의 top이 '+' 이나 '-'이면
                post = post + stack.pop()  # 스택의 top을 post에 추가하고
                stack.append(i)  # stack에 i 추가
            elif stack[-1] == '*' or stack[-1] == '/':  # 스택의 탑이 '*' 이나 '/'이면
                while len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):  # 스택이 비어있지 않으면서 스택의 탑이 '*' 이나 '/'이 아닐 때까지
                    post = post + stack.pop()  # 스택을 팝해서 post에 추가
                stack.append(i)  # 그리고나서 스택에 i추가
            else:
                stack.append(i)

        elif i == '*' or i == '/':  # i가 '*'일 때
            if not stack:  # 스택이 비었으면
                stack.append(i)  # 스택에 i 추가
            elif stack[-1] == '+' or stack[-1] == '-':  # 스택의 top이 '+' 이나 '-'이면
                stack.append(i)  # 스택에 i 추가
            elif stack[-1] == '*' or stack[-1] == '/':  # 스택의 탑이 '*' 이나 '/'이면
                post = post + stack.pop()  # 스택의 top을 post에 추가하고
                stack.append(i)  # stack에 i 추가
            else:
                stack.append(i)

        elif i == '(': # '('면 스택에 추가
            stack.append(i)

        elif i == ')': # ')' 면 '('이 나오기 전까지 스택에 추가하고
            while stack[-1] != '(':
                post = post + stack.pop()
            stack.pop() # 남아있는 '('을 제거

        else:  # i가 숫자일 때
            post = post + i  # post에 추가

    else:  # 주어진 문자열을 다 순회했을 때
        while len(stack) > 0:  # 스택에 남아있는 것은 탑에 있는 것부터 post에 추가
            post = post + stack.pop()


    # 후위표기법을 통한 계산
    for i in post:  # post의 문자를 하나씩 꺼내서
        if i == '+':  # i가 '+'일 때
            stack.append(stack.pop() + stack.pop())  # 스택의 top 2개 팝한 후 둘을 더해서 스택에 다시 추가
        elif i == '*':  # i가 '*'일 때
            stack.append(stack.pop() * stack.pop())  # 스택의 top 2개 팝한 후 둘을 곱해서 스택에 다시 추가
        elif i == '/':  # i가 '*'일 때
            stack.append(stack.pop() / stack.pop())
        elif i == '-':  # i가 '*'일 때
            stack.append(stack.pop() - stack.pop())
        else:  # i가 숫자일 때
            stack.append(int(i))  # 계산을 위해 정수형으로 변환하여 스택에 추가

    print(f'#{case + 1} {stack[0]}')  # 마지막으로 하나 남은 스택을 출력