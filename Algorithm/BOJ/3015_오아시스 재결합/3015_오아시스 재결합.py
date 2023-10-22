import sys
input = sys.stdin.readline

## 풀이 참조
## 같은 숫자들이 연속적으로 stack에 담길 경우 나의 접근법으로는 stack에 추가할 때마다 모든 stack을 순회해야 한다
## 따라서 같은 숫자가 연속적으로 몇번 나오는지에 대한 정보를 stack에 같이 담는다

n = int(input())
arr = [int(input()) for _ in range(n)]

res = 0
stack = [(arr[0], 1)] ## (숫자, 연속된 횟수)
for num in arr[1:]:
    ## stack이 있으면서 num이 마지막 숫자보다 크면
    while stack and stack[-1][0] < num:
        ## pop해서 연속된 횟수를 res에 추가
        res += stack.pop()[1]

    ## 위 과정을 거치고 스택이 비어 있다면
    if not stack:
        ## num을 추가하고 continue
        stack.append((num, 1))
        continue

    ## num이 스택의 마지막 숫자와 같다면
    if stack[-1][0] == num:
        ## 연속된 횟수만큼 res에 추가
        cnt = stack.pop()[1]
        res += cnt
        ## pop을 해도 스택에 요소가 있다면 해당 요소는 num보다 큰 숫자일 것
        if stack:
            ## 따라서 그 숫자의 연속 횟수와 관계없이 연속된 마지막 숫자와 만날 수밖에 없기에 res += 1
            res += 1

        ## 연속 횟수를 높인 숫자를 stack에 추가하고 continue
        stack.append((num, cnt + 1))
        continue
    
    ## num이 스택의 마지막 숫자보다 작다면
    if stack[-1][0] > num:
        ## 만날 수 있는 숫자는 스택의 마지막 숫자 하나뿐이기에 res += 1
        res += 1
        ## 스택에 num 추가
        stack.append((num, 1))

print(res)




## 나의 풀이(시간초과)
## 핵심 : 인풋 받은 arr를 순회하며 각 숫자 a를 스택에 넣는다. 단, 스택을 거꾸로 순회하며 a보다 작은 숫자는 pop한다
## a를 스택에 담기 전에 스택에 담긴 녀석들 중 짝을 지을 수 있는 숫자를 탐색한다

## 과정
## 스택에 넣을 숫자 a를 기준으로 스택을 거꾸로 순회하며
## a보다 큰 숫자를 만날 때까지 res += 1 을 한다
## a보다 작은 숫자는 이후 다른 사람을 만날 수 없기 때문에 pop한다
## a와 같은 숫자는 pop하지 않는다(이 부분에서 시간초과)


import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

res = 0
stack = [arr[0]]
last_idx = 0 # arr 마지막부터 순회하기 위해 arr의 마지막 idx를 저장
for num in arr[1:]: ## arr를 순회
    this_idx = last_idx ## 비교할 숫자를 this_idx에 저장
    while 0 <= this_idx: ## 스택을 거꾸로 순회하며
        if stack[this_idx] < num: ## num보다 작으면
            res += 1
            stack.pop()
            this_idx -= 1 ## 그 다음 비교할 숫자의 idx 감소
            last_idx -= 1 ## pop했기 때문에 마지막 idx 감소

        elif stack[this_idx] == num: ## num과 같은 숫자라면
            res += 1 ## 만날 수 있기 때문에 res += 1
            this_idx -= 1 ## pop하지 않고 다음 비교할 숫자의 idx만 감소
        
        else: ## num보다 크면
            res += 1
            break

    stack.append(num) ## stack에 num을 담고
    last_idx += 1 ## arr 길이 증가
print(res)


