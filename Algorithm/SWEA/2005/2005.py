import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    size = int(input())
    print(f'#{case+1}')
    if size == 1:
        print(1)
    
    elif size == 2:
        print(1)
        lst = [1, 1]
        print(*lst)

    else:
        print(1)
        lst = [1, 1]
        print(*lst)
        for _ in range(size-2):
            for i in range(1, len(lst)):
                lst[i-1] = lst[i] + lst[i-1]
            else:
                lst = [1] + lst
                print(*lst)
