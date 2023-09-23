from collections import deque
import sys
input = sys.stdin.readline

## input 받는 것이 어려운 문제
## 문제 풀이는 연속된 R의 개수를 찾고
## D가 등장했을 때, 연속된 R의 개수의 홀짝을 기준으로
## pop or popleft를 결정한다
## 그리고 마지막에 남아있는 R의 개수를 기준으로 그냥 출력할지, 뒤집어 출력할지 결정한다

def uu():
    pattern = list(input().rstrip())
    length = int(input())

    cnt = 0
    for order in pattern:
        if order == "D":
            cnt += 1
    if cnt > length:
        input()
        return print("error")

    str_arr = input().rstrip()
    str_arr = str_arr[1:-1]
    arr = str_arr.split(",")
    arr = deque(arr)

    r_cnt = 0
    for i in range(len(pattern)):
        if pattern[i] == "R":
            r_cnt += 1
        else:
            if r_cnt % 2:
                arr.pop()
            else:
                arr.popleft()
    else:
        if r_cnt % 2:
            arr.reverse()
    
    print("[" + (",").join(arr) + "]")
        
t = int(input())
for _ in range(t):
    uu()

