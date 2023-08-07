import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap, min_heap = [], []
first, second = int(input()), int(input())
print(first)

if first <= second:
    max_heap.append(-first)
    min_heap.append(second)
    max_min, min_max = first, second
    print(first)

elif first > second:
    max_heap.append(-second)
    min_heap.append(first)
    max_min, min_max = second, first
    print(second)


max_cnt, min_cnt = 1, 1


for i in range(n-2):
    x = int(input())
    if max_cnt > min_cnt:
        if x >= max_heap[0]*-1:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(min_heap, heapq.heappop(max_heap)*-1)
            heapq.heappush(max_heap, -x)
        min_cnt += 1
    elif max_cnt == min_cnt:
        if x <= min_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(max_heap, heapq.heappop(min_heap)*-1)
            heapq.heappush(min_heap, x)
        max_cnt += 1
    else:
        if x <= min_heap[0]:
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, heapq.heappop(min_heap)*-1)
            heapq.heappush(min_heap, x)
        max_cnt += 1

    print(-max_heap[0])




