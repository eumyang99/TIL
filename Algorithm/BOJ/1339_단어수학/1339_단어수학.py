import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

max_length = 0
for word in words:
    if max_length < len(word):
        max_length = len(word)

size = {}
for word in words:
    word_length = len(word)
    for i in range(word_length):
        if word[i] not in size:
            size[word[i]] = 10**(word_length-i-1)
        else:
            size[word[i]] += 10**(word_length-i-1)

sorted_size = sorted(size.values(), reverse=True)

res = 0
num = 9
for value in sorted_size:
    res += value*num
    num -= 1

print(res)