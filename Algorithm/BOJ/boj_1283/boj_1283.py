import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lst = [list(input().split()) for _ in range(n)]         # str으로 받아서 사용
        
used = set()                                            # 사용된 단어, 대문자 소문자 모두 add


for x in range(n):                  # 입력 받은 옵션 각각에 대해 ex) ['Save All']
    for y in range(len(lst[x])):    # 한 옵션의 여러 단어에 대해 
        word = lst[x][y]            # ex) word = ['Save'],  word = ['All']
        if word[0].upper() not in used and word[0].lower() not in used:     # 첫글자가 사용되지 않았으면
            used.add((word[0].upper()))                                     # 사용처리를 하고
            used.add((word[0].lower()))
            lst[x][y] = word.replace(f'{word[0]}', f'[{word[0]}]', 1)       # 해당글자를 바꾸어 줌
            break                                                           # 이후 종료

    else:                           # 만약 단어의 첫글자가 다 사용되었다면
        flag = 0                    # for문 종료를 위한 flag 생성
        for y in range(len(lst[x])):
            word = lst[x][y]        
            for i in range(len(word)):                  # 해당 단어의 앞글자부터 사용되었는지 확인하고
                if word[i].upper() not in used and word[i].lower() not in used:
                    used.add((word[i].upper()))
                    used.add((word[i].lower()))
                    lst[x][y] = word.replace(f'{word[i]}', f'[{word[i]}]', 1) # 바꾸어 줌
                    flag = 1        # flag를 1로 바꾸어 
                    break
            if flag == 1:           # for문 종료
                break

for words in lst:
    print(" ".join(words))







