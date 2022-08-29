import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# T = int(input())
# for case in range(T):
n = int(input())
lst = list(map(int, input().split()))

res = [n]                           # 제일 큰 숫자 먼저 res에 넣고 ex) 7
for i in range(len(lst)-1, 0, -1):  # 뒤부터 차근차근 ex) 6 5 4 3 2 1
    res.insert(lst[i-1], i)         # lst[i]에 담겨 있는 녀석을 인덱스 삼아 res에 i 삽입
print(*res)
