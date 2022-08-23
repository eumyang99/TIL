import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    stack = []
    word = input()
    for i in word:
        if i == '(' or i == '{' or i == ')' or i == '}':
            if len(stack) == 0:
                if i == ')' or i == '}':
                    print(f'#{case+1} 0')
                    break
                else:
                    stack.append(i)

            elif stack[-1] == '(':
                if i == ')':
                    stack.pop()
                else:
                    stack.append(i)

            elif stack[-1] == '{':
                if i == '}':
                    stack.pop()
                else:
                    stack.append(i)

    if len(stack) == 0:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')
