import sys
input = sys.stdin.readline

## 발상
## KMP 실패함수를 만드는 방법을 활용한다.
## table의 마지막 값을 구하면 어디서부터 반복이 시작됐는지 알 수 있다.
## 따라서 text_len * table[-1] 로 답을 찾을 수 있다.

text_len, text = int(input()), input().rstrip()

if text:
    table = [0]*(text_len)
    j = 0
    for i in range(1, text_len):
        while j > 0 and text[i] != text[j]:
            j = table[j-1]
        if text[i] == text[j]:
            j += 1
            table[i] = j
    print(text_len - table[-1])
else:
    print(0)