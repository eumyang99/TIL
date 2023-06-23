import sys
input = sys.stdin.readline

## 발상 참고
## 처음에는 재귀함수를 사용해서 S에서 T를 만들려고 했다.
## 그러나 T의 마지막 알파벳을 통해서 해당 작업을 특정할 수 있었다.
## ABAB 일 경우, 마지막 작업은 B를 추가하는 작업
## 따라서 ABA에서 시작했을 것
## ABA 일 경우, 마지막 작업은 B를 추가하는 작업
## 따라서 AB에서 시작했을 것
## 그렇기 때문에 T의 작업을 역으로 진행하면서 S와 같아지는지를 확인하면 된다. 

s = input().rstrip()
t = input().rstrip()

while len(t) != len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]

if t == s:
    print(1)
else:
    print(0)
