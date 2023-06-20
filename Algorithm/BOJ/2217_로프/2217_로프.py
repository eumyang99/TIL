import sys
input = sys.stdin.readline

## 발상
## 쓰이는 로프 중 가장 작은 무게 & 쓰이는 로프의 개수 사이의 관계를 주목
## (가장 작은 무게를 감당하는 로프 * 쓰이는 로프의 개수) 가 비교 대상
## 로프 리스트를 정렬하고 처음부터 순회하면서
## lst[i] => 쓰이는 로프 중 가장 약한 로프
## (n-i) => 사용된 로프의 개수
## 이 두 값을 곱해서 최대값을 찾음

n = int(input())
lst = list(int(input()) for _ in range(n))
lst.sort()

res = 0
for i in range(n):
    if lst[i]*(n-i) > res:
        res = lst[i]*(n-i)

print(res)