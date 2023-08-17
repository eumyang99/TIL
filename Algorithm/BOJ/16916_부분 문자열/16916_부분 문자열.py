import sys
input = sys.stdin.readline

def kmp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    table = [0]*(pattern_len)
    j = 0
    for i in range(1, pattern_len):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    j = 0
    for i in range(text_len):
        while j > 0 and text[i] != pattern[j]:
            j = table[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == pattern_len:
                return print(1)
    else:
        return print(0)
text = input().rstrip()
pattern = input().rstrip()

kmp(text, pattern)