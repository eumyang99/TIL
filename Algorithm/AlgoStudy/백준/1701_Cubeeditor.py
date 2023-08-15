from collections import defaultdict
import sys
input = sys.stdin.readline

## 재귀도 터지고 시간도 오래 걸리고 답도 틀림

def uu(arr, cnt):
    used = [[] for _ in range(26)]
    for idx in arr:
        if idx+1 < n:
            used[lst[idx+1]].append(idx+1)
    temp = []
    for a in used:
        if len(a) >= 2:
            temp.append(a)
    if temp:
        for b in temp:
            return uu(b, cnt+1)
    else:
        return cnt
    

word = input().rstrip()
n = len(word)
## 소문자를 숫자로 변환
lst = [ord(i)-97 for i in word]

## 딕셔너리에 담음
dic = defaultdict(list)
for i in range(len(word)):
    dic[lst[i]].append(i)

res = 0
## 같은 알파벳 모두로 시작
for start_alpha in dic.keys(): #0, 1, 2
    temp = 0
    start_alpha_lst = dic[start_alpha][:]
    ## 같은 알파벳이 2개 이하면 같은게 있을 수 없으니 패스
    ## 두개 이상부터 재귀 함수
    if len(start_alpha_lst) > 1:
        temp = max(uu(start_alpha_lst, 1), temp)
    res = max(temp, res)
print(res)



