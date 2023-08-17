import sys
input = sys.stdin.readline

text = input().rstrip()
pattern = input().rstrip()
text_len = len(text)
pattern_len = len(pattern)


table = [0]*pattern_len
j = 0
for i in range(1, pattern_len):
    while j > 0 and pattern[i] != pattern[j]:
        j = table[j-1]
    if pattern[i] == pattern[j]:
        j += 1
        table[i] = j

cnt = 0
location = []

j = 0
for i in range(text_len):
    while j > 0 and text[i] != pattern[j]:
        j = table[j-1]
    if text[i] == pattern[j]:
        j += 1
        ## 만약 패턴과 일치하는 부분을 찾았다면
        if j == pattern_len:
            ## 일치 회수를 +1 해주고
            cnt += 1
            ## 패턴일 일치하기 시작한 인덱스 i - j + 2 를 기록하고
            location.append(str(i - j + 2))
            ## 다시 다음 패턴을 찾으며 이미 패턴과 일치한 부분까지 j를 옮김
            ## 이 부분이 헷갈리지만 잘 원리를 생각하면 맞다.
            ## text =    "abcabcd"
            ## pattern = "abcabc "
            ## table =   "000123 "
            ## 일 때 현재 j는 6으로, pattern의 7번째 자리를 의미한다.
            ## 따라서 text의 마지막 문자인 d는 pattern의 마지막 문자인 c에 해당하는 table과 비교해야 한다.
            ## 고로 table의 j-1번째 값(table[5] = 3)과 비교해야 한다.  
            ## 따라서 j를 table[j-1]으로 바꾸어 text의 다음 문자인 d와 비교 해야한다.
            j = table[j-1]

print(cnt)
print(" ".join(location))