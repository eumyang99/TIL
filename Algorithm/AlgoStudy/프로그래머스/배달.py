from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    dic = defaultdict(list)
    for s, e, w in road:
        dic[s].append((w, e))
        dic[e].append((w, s))

    weight = [500001] * (N+1)
    weight[1] = 0
    que = [(0, 1)]
    
    while que:
        w, s = heapq.heappop(que)
        if weight[s] < w: continue
        
        for nw, ns in dic[s]:
            new_weight = w + nw
            if weight[ns] < new_weight or K < new_weight: continue
            weight[ns] = new_weight
            heapq.heappush(que, (new_weight, ns))
    
    for w in weight:
        if K < w: continue 
        answer += 1 
        
    return answer