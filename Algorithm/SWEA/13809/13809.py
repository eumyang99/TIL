import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    word = input()
    word_lst  = []
    size = 0
    for i in word:
        if size == 0:
            word_lst.append(i)
            size += 1
        elif word_lst[-1] != i:
            word_lst.append(i)
            size += 1
        elif word_lst[-1] == i:
            word_lst.pop()
            size -=1
    print(f'#{case+1} {size}')


