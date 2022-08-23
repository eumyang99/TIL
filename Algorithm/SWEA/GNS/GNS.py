import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    case, size = input().split()
    size = int(size)
    lst = input().split()
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dic = {}
    for i in range(len(a)):
        dic[a[i]] = i

    temp = []
    for i in range(len(lst)):
        temp.append(dic.get(lst[i]))
    temp.sort()

    result = []
    for i in temp:
        result.append(a[i])

    print(f'{case}')
    print(" ".join(result))












