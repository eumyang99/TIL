import sys
sys.stdin = open('input.txt')


def func(root):
    global res
    res += 1                                # 함수에 진입할 때마다 res +1
    if root in tree:                        # root가 tree에 있으면
        for c in tree[root]:                # root의 밸류를 함수에 다시 넣음
            func(c)

T = int(input())
for case in range(T):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = dict()                           # 간선 정보를 딕셔너리로
    for i in range(e):                      
        p = lst[i*2]                        # 부모
        c = lst[i*2+1]                      # 자식
        if p not in tree:               # 부모가 tree에 없으면
            tree[p] = []                    # 부모 : 빈 리스트 만들고
            tree[p].append(c)               # 자식 추가
        else:                           # 부모가 tree에 있으면
            tree[p].append(c)               # 자식 추가

    
    res = 0
    func(n)
    print(f'#{case+1} {res}')

