import sys
input = sys.stdin.readline

## 발상
## 앞에 서는 사람일수록 뒤 사람에게 시간 영향을 여러번 미침
## 따라서 소요시간이 짧은 순서대로 돈을 인출하면 됨
## 첫번째 인출하는 사람의 소요시간이 A일 때, 전체가 5명이면 A*5만큼 전체 대기시간에 추가함
## 두번째 인출하는 사람의 소요시간이 B일 때, 전체가 5명이면 A*4만큼 전체 대기시간에 추가함
## 반복

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

res = 0
for i in range(n):
    res += lst[i]*(n-i)

print(res)

