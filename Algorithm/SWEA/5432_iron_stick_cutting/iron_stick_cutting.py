import sys
sys.stdin = open("input.txt")

### '('가 등장하면 +1하고, ')'가 등장하면 -1을 누적했을 때
### ')'가 등장한 순서를 기준으로
### 왼쪽으로 두칸을 앞의 누적값이 ")"이 등장했을 때 누적값과 같다면 ex) 3 4 3[")"]가 등장
### ")"이 등장했을 때의 누적값만큼 조각이 생김

### 그러나 ')'가 등장한 순서를 기준으로
### 왼쪽으로 두칸을 앞의 누적값이 ")"이 등장했을 때 누적값과 -2 차이가 난다면 ex 4 3 2[")"]가 등장
### 막대 조각이 끝나는 것이므로 조각 하나가 생김

### 누적합을 체크하고 기록하기 위해 accu라는 리스트를 만들어 누적값을 기록하며 ")"이 등장할 때마다 앞의 누적합과 비교했음
T = int(input())
for case in range(T):
    lst = list(input())

    result = 0
    accu = []
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
            accu.append(cnt)
        elif lst[i] == ')':
            cnt -= 1
            accu.append(cnt)
            # 레이저가 쏘아지는 부분
            if accu[i-2] == accu[i]:
                result += cnt
            # 막대기가 끝나는 부분
            elif accu[i-2] == accu[i]+2:
                result += 1

    print(f'#{case+1} {result}')






    # temp = lst[:]
    # for i in range(len(lst)-1):
    #     if lst[i] == '(' and lst[i+1] == ')':
    #         temp[i] = '*'
    # for i in range(len(lst)-1, -1, -1):
    #     if temp[i-1] == '*':
    #         temp.pop(i)

    # cnt = 0
    # accu = []
    # for i in range(len(temp)):
    #     if temp[i] == '(':
    #         cnt += 1
    #         accu.append(cnt)
    #     elif temp[i] == ')':
    #         cnt -= 1
    #         accu.append(cnt)
    #     else:
    #         accu.append(-1)


    # result = 0
    # for i in range(1, max(accu)+1): # 0~3 최대 중첩 수
    #     while i-1 in accu:
    #         s = accu.index(i) # 1 2 3
    #         e = accu.index(i-1) # 0 1 2

    #         result += accu[s+1:e].count(-1)+1
    #         accu.pop(e)
    #         accu.pop(s)

    # print(f'#{case+1} {result}')
       
    



    # result = 0
    # while '(' in temp:
    # # 현재 가장 넓은 범위의 막대기 처음과 끝 인덱스
    #     z_idx = []
    #     s_idx = [temp.index('(')]
    #     cnt = 0
    #     for i in range(len(temp)):
    #         if temp[i] == '(':
    #             cnt += 1
    #         elif temp[i] == ')':
    #             cnt -= 1
    #         else:
    #             pass

    #         if cnt == 0 and temp[i] == ')' :
    #             z_idx.append(i)


    #     for i in range(len(z_idx)-1):
    #         s_idx.append(temp[z_idx[i] : z_idx[i+1]].index('(')+z_idx[i])

    #     for i in range(len(z_idx)):
    #         result += temp[s_idx[i]+1:z_idx[i]].count('*')+1
    #         temp[s_idx[i]] = ''
    #         temp[z_idx[i]] = ''
    # print(f'#{case+1} {result}')






        

    
        