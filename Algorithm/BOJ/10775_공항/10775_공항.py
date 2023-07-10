import sys
input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        b = find(parent[x])
        parent[x] = b
    return x

g = int(input())
p = int(input())

parent = [i for i in range(g)]     # 어디로 가야 하는지
cnt = 0

for x in range(p):
    num = int(input())-1
    if parent[num] == num:
        parent[num] -= 1
        cnt += 1
    else:
        a = find(num)
        if a == -1:
            break
        else:
            parent[a] -= 1
print(parent)
print(cnt)


# 20
# 20
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 15
# 15
# 15
# 15
# 15
# 15
# 6
# 1
# 16
# 17
# 15
# 15
# 15






