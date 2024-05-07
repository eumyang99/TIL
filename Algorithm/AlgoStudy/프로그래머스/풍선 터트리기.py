def solution(a):
    min_idx = a.index(min(a))
    answer = 1
    
    left_min, right_min = 1000000001, 1000000001
    for i in range(min_idx):
        if a[i] < left_min:
            answer += 1
            left_min = a[i]
        
    for i in range(len(a) - 1, min_idx, -1):
        if a[i] < right_min:
            answer += 1
            right_min = a[i]
        
    return answer