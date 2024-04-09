def solution(n, results):
    answer = 0
    ## versus[선수] = [
    ## 보다 높은 순위의 선수들 set 완성 여부,
    ## 보다 낮은 순위의 선수들 set 완성 여부,
    ## 보다 높은 순위의 선수들 set,
    ## 보다 낮은 순위의 선수들 set
    ## ]
    versus = [[-1, -1, set(), set()] for _ in range(n+1)]
    for winner, loser in results:
        versus[winner][2].add(loser)
        versus[loser][3].add(winner)

    ## type = 2 는 보다 높은 순위
    ## type = 3 은 보다 낮은 순위
    def recur(player, type):
        ## 이미 완성된 set이 있으면 해당 set 반환
        if versus[player][type-2] != -1:
            return versus[player][type]
        
        vs_arr = list(versus[player][type])
        for partner in vs_arr:
            versus[player][type].update(recur(partner, type))
        versus[player][type-2] = len(versus[player][type])
        
        return versus[player][type]
        
    for player in range(1, n+1):
        high_cnt = versus[player][0] if versus[player][0] != -1 else len(recur(player, 2))
        low_cnt = versus[player][1] if versus[player][1] != -1 else len(recur(player, 3))
        if high_cnt + low_cnt == n - 1:
            answer += 1
    
    return answer