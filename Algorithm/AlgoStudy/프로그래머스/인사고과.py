def solution(scores):
    man = scores[0]
    lst = [[] for _ in range(200001)]
    for score in scores:
        lst[sum(score)].append(score)

    res = 1
    for i in range(sum(man)+1, 200001):
        res += len(lst[i])

    last_group = 200000
    for i in range(200000, -1, -1):
        if len(lst[i]) == 0:
            last_group -= 1
        else:
            break

    for x in range(sum(man)+1, last_group-1):
        for y in range(len(lst[x])):
            for z in range(x+2, last_group+1):
                for w in range(len(lst[w])):
                    if lst[x][y][0] < lst[z][w][0] and lst[x][y][1] < lst[z][w][1]:
                        res -= 1 
    return res
            

    # man = scores[0]
    # scores.sort(key=lambda x: sum(x))
    # max_total = sum(scores[-1])
    # man_total = sum(man)

    # if man_total == max_total:
    #     return 1
    # if man_total == max_total - 1:
    #     idx = len(scores) -1 
    #     end = len(scores) -1 
    #     while idx < len(scores):
    #         if max_total > sum(scores[idx]):
    #             end = idx
    #             break
    #         else:
    #             idx -= 1
    #     return len(scores) - end


    # idx = 0
    # start = 0
    # while idx < len(scores):
    #     if man_total < sum(scores[idx]):
    #         start = idx
    #         break
    #     else:
    #         idx += 1
            
    # idx = len(scores) -1 
    # end = len(scores) -1 
    # while idx < len(scores):
    #     if max_total -2 >= sum(scores[idx]):
    #         end = idx
    #         break
    #     else:
    #         idx -= 1

    # res = len(scores) - start + 1

    # for i in range(start, len(scores)):
    #     if man[0] < scores[i][0] and man[1] < scores[i][1]:
    #         return -1
    
    # for x in range(start, end):
    #     for y in range(x, len(scores)):
    #         if scores[x][0] < scores[y][0] and scores[x][1] < scores[y][1]:
    #             res -= 1
    #             break
    
    # return res


print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))