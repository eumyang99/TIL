import sys
import heapq
input = sys.stdin.readline

## 발상 : 풀이 참고

## 주요 접근법
## 1. 사이즈가 가장 작은 가방부터 넣을 수 있는 가장 비싼 보석을 temp에 놓고 그 중 가장 비싼 보석을 넣으면 됨
## 2. 그 다음 가방 사이즈에 넣을 수 있는 보석을 temp에 다 넣은 뒤 역시 그 중 가장 비싼 보석을 넣으면 됨
## 3. 이 접근법이 greedy

## 주요 개념 Heap
## heap은 부모 자식 간의 대소 비교로 이루어진 트리 구조
## heap을 이용하여 list에 push하면 자동으로 위 조건이 만족되는 리스트를 구성해줌(트리의 node 번호가 list의 index)
## heap은 최소값, 최대값을 빠르게 찾아줌
## 루트 노드에 최대값을 저장한다면 최대힙, 최소값을 저장한다면 최소힙

## 이 문제에서는 temp에 저장하는 보석의 최대값만을 계속 찾아야 하니 최대힙을 사용함
## 파이썬의 기본 heapq는 최소힙으로 세팅되어 있음
## 따라서 최대힙을 이용하고 싶다면 - 부호를 붙여서 저장(절대값이 가장 큰 값이 루트노드에 저장되도록)
## 최대값을 사용하고 싶다면 pop을 할 때, - 를 붙여서 pop을 하면 됨

n, k = map(int, input().split())
J_lst = [list(map(int, input().split())) for _ in range(n)]
B_lst = [int(input()) for _ in range(k)]

J_lst.sort(reverse=True)
B_lst.sort()

res = 0
temp = []
if J_lst == []:
    print(0)
else:
    for bag_size in B_lst:
        while J_lst and J_lst[-1][0] <= bag_size:
            heapq.heappush(temp, -J_lst[-1][1])
            J_lst.pop()
        if temp:
            res -= heapq.heappop(temp)

print(res)





## heap 자료구조를 만들어 추가하고 삭제하는 기능을 직접 구현해보았으나 시간 초과가 뜸

# res = 0
# temp = []
# if J_lst == []:
#     print(0)
# else:
#     for bag_size in B_lst:
#         while J_lst and J_lst[0][0] <= bag_size:
#             temp.append(J_lst[0][1])
#             added_idx = len(temp)-1
#             while 1:
#                 if added_idx != 0:
#                     if added_idx % 2 == 1:
#                         parent_idx = int((added_idx-1) // 2)
#                     else:
#                         parent_idx = int((added_idx-2) // 2)
#                     if temp[parent_idx] < temp[added_idx]:
#                         temp[parent_idx], temp[added_idx] = temp[added_idx], temp[parent_idx]
#                         added_idx = parent_idx
#                     else:
#                         break
#                 else:
#                     break
#             J_lst.pop(0)
#         if temp:
#             temp[0], temp[-1] = temp[-1], temp[0]
#             res += temp.pop(-1)
            
#             target_idx = 0
#             while 1:
#                 left_child_idx = target_idx*2+1
#                 right_child_idx = target_idx*2+2
#                 if left_child_idx <= len(temp)-1 and right_child_idx <= len(temp)-1:  # 자식 둘 다 있을 때
#                     bigger_idx = left_child_idx
#                     if temp[right_child_idx] > temp[left_child_idx]:
#                         bigger_idx = right_child_idx
#                     if temp[target_idx] < temp[bigger_idx]:
#                         temp[target_idx], temp[bigger_idx] = temp[bigger_idx], temp[target_idx]
#                         target_idx = bigger_idx
#                         continue
#                     else:
#                         break

#                 elif left_child_idx <= len(temp)-1 and right_child_idx > len(temp)-1: # 왼쪽 자식만 있을 때
#                     if temp[target_idx] < temp[left_child_idx]:
#                         temp[target_idx], temp[left_child_idx] = temp[left_child_idx], temp[target_idx]
#                         target_idx = left_child_idx
#                         continue
#                     else:
#                         break
#                 else:   # 둘 다 없을 때
#                     break

#     print(res)
                
