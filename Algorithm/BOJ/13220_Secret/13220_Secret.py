# import sys
# input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(a, b)

word = "ababbab"
j = 0
lst = [0]*len(word)
for i in range(1, len(word)):
    while j > 0 and word[j] != word[i]:
        j = lst[j-1]
    
    if word[j] == word[i]:
        j += 1
        lst[i] = j
    # j = lst[i-1]
    # if word[j] == word[i]:
    #     lst[i] = j+1
    # else:
    #     while j > 0:
    #         j = lst[j-1]
    #         if word[j] == word[i]:
    #             lst[i] = j+1
    #             break
print(lst)

