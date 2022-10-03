import sys
sys.stdin = open('input.txt')

def partition(l, r):
    pivot = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j


def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)


T = int(input())
for case in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    
    qsort(0, n-1)
    print(f'#{case+1} {lst[n//2]}')
