import sys
input = sys.stdin.readline

## 투포인터 문제
## 브루트포스로는 n^3의 시간복잡도이다
## 투포인터를 사용하면 n^2으로 줄어든다

## left는 for문으로 0 ~ n-3까지 할당
## 그리고 left 이후의 배열을 투포인터로 순회한다.
## 따라서 left 할당에 n, 해당 left 이후 mid, right를 투포인터로 순회하는데 n이기 때문에 총 n^2으로 시간을 줄일 수 있다.


def uu():
    cal = float("inf")
    l, m, r = 0, 1, n-1
    for left in range(n-2):
        mid, right = left+1, n-1

        while mid < right:
            temp = lst[left] + lst[mid] + lst[right]
            if abs(temp) < abs(cal):
                cal = temp
                l, m, r = left, mid, right

            elif temp < 0:
                mid += 1

            elif temp > 0:
                right -= 1

            elif temp == 0:
                return print(lst[l], lst[m], lst[r])
    
    print(lst[l], lst[m], lst[r])



n = int(input())
lst = list(map(int, input().split()))
lst.sort()
uu()

        

