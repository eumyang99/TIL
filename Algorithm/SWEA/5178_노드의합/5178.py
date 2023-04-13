import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def find_value(tree, node, size):
    if tree[node] == -1:
        # tree[node] == tree[node*2] + tree[node*2+1]
        if node*2 != size:
            tree[node] = find_value(tree, node*2, size) + find_value(tree, node*2+1, size)
        else:
            tree[node] = find_value(tree, node*2, size)
        return tree[node]
    return tree[node]

T = int(input())
for case in range(T):
    n, m, l = map(int, input().split())
    tree = [-1 for _ in range(n+1)]
    for _ in range(m):
        node, value = map(int, input().split())
        tree[node] = value

    print(f'#{case+1} {find_value(tree, l, n)}')