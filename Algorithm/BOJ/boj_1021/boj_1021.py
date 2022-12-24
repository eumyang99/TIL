import sys
input = sys.stdin.readline


n, m = map(int, input().split())
lst = list(map(int, input().split()))
# q = []                      # 전체 숫자를 q에 담는다
# for i in range(1, n+1):         
#     q.append(i)

# res = 0                     # 출력할 결과
# pointer = 0                 # 현재 위치한 idx
# size = n                    # 삭제되고 남은 현재 배열의 크기

# for num in lst:             # 뽑아낼 숫자들을 순회하며
#     idx = q.index(num)      # 해당 숫자가 q리스트의 어느 idx에 있는지 확인
#     q.pop(idx)              # 해당 숫자를 미리 pop

#     if pointer < idx:                           # 만약 현재 포인터보다 뽑아낼 숫자의 idx가 더 크다면 
#         right = idx - pointer                   # 오른쪽으로 갈 때의 거리
#         left = pointer + ((size-1) - idx) + 1   # 왼쪽으로 갈 때의 거리를 
#         if right <= left:                       # 비교해서 
#             res += right                        # 작은 값을 res에 추가
#         else:
#             res += left
#     elif pointer > idx:                         # 반대도 상동
#         right = idx + ((size-1) - pointer) + 1 
#         left = pointer - idx
#         if right <= left:
#             res += right
#         else:
#             res += left
    
#     pointer = idx   # 포인터의 위치를 삭제한 숫자의 idx에 둠
#     size -= 1       # 숫자가 하나 삭제되었으니 size를 하나 줄임
    
# print(res)          # 결과 출력



#### 리스트 pop을 사용하지 않는 수학적 방법(더 오래 걸림... 왜??)
res = 0             # 출력할 결과
pointer = 1         # 현재 숫자
size = n            # 제거되고 남은 숫자 개수
temp = []           # 제거된 숫자를 모음

for i in range(m):                          # 제거할 숫자를 순회하며
    deleted = 0                             # 해당 숫자로 이동할 때까지 가는 동안 제거된 숫자 개수
    if pointer == lst[i]:                       # 만약 포인터와 제거할 숫자가 같으면
        size -= 1                               # 사이즈를 하나 줄이고
        pointer = lst[i] + 1                    # 포인터는 제거한 숫자 + 1로 이동
        temp.append(lst[i])                     # 제거한 숫자를 temp에 저장
        continue                                # 다음 제거할 숫자로
    
    elif pointer < lst[i]:                      # 만약 포인터보다 제거할 숫자가 크다면
        for x in temp:                          # 포인터와 제거할 숫자 사이에 이미 제거된 숫자를 카운트해서
            if pointer <= x and x < lst[i]:     # (현재 포인터가 제거된 숫자에 있는 경우를 생각해서 <= 를 사용)
                deleted += 1
        right = lst[i] - pointer - deleted      # 오른쪽 이동할 거리 - 제거된 숫자 개수를 뺀다
        left = size - right                     # 왼쪽으로 이동할 경우 전체 사이즈에서 오른쪽으로 이동할 개수를 뺀다(이 풀이의 핵심)

    elif pointer > lst[i]:                      # 만약 제거할 숫자가 포인터보다 크다면
        for x in temp:                          # 이하 상동
            if lst[i] <= x  and x < pointer:
                deleted += 1
        right = pointer - lst[i] - deleted
        left = size -right
    
    if right <= left:               # 오른쪽으로 가는 방법과 왼쪽으로 가는 방법 중
        res += right                # 작은 것을 res에 더함
    else:
        res += left

    
    size -= 1                       # 사이즈를 하나 줄이고
    temp.append(lst[i])             # 제거된 숫자를 temp에 저장
    pointer = lst[i] + 1            # 포인터는 제거한 숫자보다 하나 크게
                                    # 한 칸 이동한 숫자도 제거된 숫자일 경우를 대비해서 제거된 숫자를 카운트할 때 경우를 고려함

print(res)

