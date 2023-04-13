import sys
input = sys.stdin.readline


def preorder(node):
    print(node, end="")
    left, right = dic[node][0], dic[node][1]
    if left != ".":
        preorder(left)
    if right != ".":
        preorder(right)

def inorder(node):
    left, right = dic[node][0], dic[node][1]
    if left != ".":
        inorder(left)
    print(node, end="")
    if right != ".":
        inorder(right)

def postorder(node):
    left, right = dic[node][0], dic[node][1]
    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(node, end="")

n = int(input())
dic = {}
for _ in range(n):
    m, l, r = input().split()
    dic[m] = [l,r]

preorder("A")
print()
inorder("A")
print()
postorder("A")