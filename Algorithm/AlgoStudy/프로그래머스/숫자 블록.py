def solution(begin, end):   
    answer = []
    for num in range(begin, end+1):
        maxi = 1
        for i in range(2, int(num ** (1 / 2)) + 1):
            share, remain = divmod(num, i)
            if remain: continue
            maxi = i
            if 10000000 < share: continue
            answer.append(share)
            break
        else:
            answer.append(maxi)
            
    if begin == 1:
        answer[0] = 0
    return answer