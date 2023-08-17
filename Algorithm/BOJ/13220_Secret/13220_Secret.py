import sys
input = sys.stdin.readline

## 발상
## kmp로 풀이했다
## 문제 상황은 회전된 문자열이 같은지 확인하는 것이다
## 따라서 이렇게 회전된 문제의 경우 주어진 데이터를 반복해서 나열한다 ("ABC"가 주어진 경우 "ABCABC"로)

n = int(input())
word_a = list(map(int, input().split()))
word_aa = word_a + word_a
word_b = list(map(int, input().split()))
j = 0
table = [0] * n
for i in range(1, n):
    while j > 0 and word_b[j] != word_b[i]:
        j = table[j-1]
    if word_b[j] == word_b[i]:
        j += 1
        table[i] = j

j = 0
for i in range(2*n):
    while j > 0 and word_aa[i] != word_b[j]:
        j = table[j-1]
    if word_aa[i] == word_b[j]:
        j += 1
        if j == n:
            print("YES")
            break
else:
    print("NO")