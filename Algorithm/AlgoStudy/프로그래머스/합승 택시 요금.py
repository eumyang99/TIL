from collections import defaultdict
import heapq
INF = 2000000001

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for x, y, w in fares:
        dic[x].append((w, y))
        dic[y].append((w, x))
        
    def dijk(start):
        weight = [INF] * (n+1)
        weight[start] = 0
        que = [(0, start)]
        cnt_set = set()
        while que:
            w, node = heapq.heappop(que)
            if node not in cnt_set:
                cnt_set.add(node)
                if len(cnt_set) == n: return weight
                
            if weight[node] < w: continue
            
            for nw, next_node in dic[node]:
                new_weight = w + nw
                if weight[next_node] < new_weight: continue
                weight[next_node] = new_weight
                heapq.heappush(que, (new_weight, next_node))
        
        return weight
    
    weights = [0] * (n+1)
    for start_node in [s, a, b]:
        weights = [x + y for x, y in zip(weights, dijk(start_node))]
            
    return min(weights)