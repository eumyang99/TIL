import sys
sys.stdin = open('input.txt')

T = 10
for case in range(10):
    n = int(input())
    lst = [0]
    
    for _ in range(n):
        lst.append(input().split())
    
    def func(node):                     
        if len(node) == 2:              # 해당 노드길이가 2이면
            print(node[1], end='')          # 글자 출력
        elif len(node) == 3:            # 해당 노드길이가 3이면
            func(lst[int(node[2])])         # 연결된 노드 한개에 들어갔다가
            print(node[1], end='')          # 글자 출력
        elif len(node) == 4:            # 해당 노드길이가 4이면
            func(lst[int(node[2])])         # 왼쪽 노드에 들어갔다가
            print(node[1], end='')          # 문자 출력하고
            func(lst[int(node[3])])         # 오른쪽 노드에 들어감

    print(f'#{case+1}', end=" ")
    func(lst[1])
    print()