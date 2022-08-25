import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(m):                          # 주어진 회수만큼
        lst.append(lst.pop(0))                  # 앞에 걸 pop해서 append함

    print(f'#{case+1} {lst[0]}')
