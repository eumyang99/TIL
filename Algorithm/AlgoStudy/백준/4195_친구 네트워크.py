import sys
input = sys.stdin.readline

def find(x):
    # if parent[x] != x:
    #     return find(parent[x])
    if parent[x] != x:
        modified_parent = find(parent[x])
        parent[x] = modified_parent
        return modified_parent
    return x

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        parent[b] = a
        res[a] += res[b]

T = int(input())
for case in range(T):
    n = int(input())
    labeled_person = {}
    label_num = 0
    parent = []
    res = {}
    for i in range(n):
        s, e = input().split()
        if s not in labeled_person:
            labeled_person[s] = label_num
            parent.append(label_num)
            res[label_num] = 1
            label_num += 1

        if e not in labeled_person:
            labeled_person[e] = label_num
            parent.append(label_num)
            res[label_num] = 1
            label_num += 1

        union(labeled_person[s], labeled_person[e])

        print(res[find(labeled_person[s])])
        

        
