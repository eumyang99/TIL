## 바텀업 DP 풀이

arr = [(50, 1)]
for i in range(20, 0, -1):
    for multi in range(3, 0, -1):
        if i * multi <= 20:
            if (i*multi, 1) not in arr:
                arr.append((i * multi, 1))
                continue
        else:
            if (i*multi, 0) not in arr:
                arr.append((i * multi, 0))
arr.sort()
                
def solution(target):
    memo = [[target+1, 0] for _ in range(target+1)]
    memo[0] = [0, 0]
    for score in range(target+1):
        for adding_score, SB in arr:
            next_score = score + adding_score
            if target < next_score: break
            if memo[score][0] + 1 < memo[next_score][0]:
                memo[next_score] = [memo[score][0] + 1, memo[score][1] + SB]
            elif memo[score][0] + 1 == memo[next_score][0] and memo[next_score][1] < memo[score][1] + SB:
                memo[next_score][1] = memo[score][1] + SB
    
    return memo[target]