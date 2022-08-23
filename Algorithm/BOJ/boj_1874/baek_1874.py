# import sys
# input = sys.stdin.readline



n = 8
# lst = [4, 3, 6, 8, 7, 5, 2, 1]
stack = []
for i in range(8):
    num = int(input())
    
    if len(stack) <= num:
        for x in range(num-len(stack)):
            print('+')
            stack.append('+')
        stack.pop()
        print('-')


        
    