import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

left, right = 0, len(lst) - 1
res = abs(lst[left] + lst[right])
res_left, res_right = left, right
while right < right:
    x = abs(lst[left] + lst[right - 1])
    y = abs(lst[left + 1] + lst[right])
    if x <= y:
        right -= 1
        if x < res:
            res_left, res_right = left, right
            res = x
    else:
        left += 1
        if y < res:
            res_left, res_right = left, right
            res = y

print(lst[res_left], lst[res_right])


