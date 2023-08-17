import sys
input = sys.stdin.readline

## 발상
## kmp를 활용한다.
## kmp를 직접적으로 사용하는 것이 아니라 table 실패함수를 구하는 원리를 사용해서 푼다.
## 자세한 내용은 notion에 kmp 실패함수 table을 만드는 과정을 보면 된다.
## 추가된 내용은 문제 특성 상 pattern으로 사용하는 것을 

## for start in range(len(text)):
##    pattern = text[start:]

## 으로 해서 모든 패턴을 앞에서부터 하나씩 줄여나간다는 점

text = input().rstrip()

res = 0
for start in range(len(text)):
    pattern = text[start:]
    pattern_len = len(pattern)
    table = [0]*(pattern_len)
    j = 0
    for i in range(1, pattern_len):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    res = max(max(table), res)

print(res)



