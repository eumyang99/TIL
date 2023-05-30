https://school.programmers.co.kr/learn/courses/30/lessons/150365?language=python3#

def solution(n, m, x, y, r, c, k):
    answer = ''
    xStart = x
    yStart = y
    xGap = r - x
    yGap = c - y
    xMustDirection = xGap
    yMustDirection = yGap


    mustMove = abs(xGap) + abs(yGap)

    # 불가능한 경우들
    if k < mustMove:
        return "impossible"
    if (k - mustMove) % 2:
        return "impossible"
    
    # 가능한 경우
    # 딱 맞는 경우
    if k - mustMove == 0:
        if xGap >= 0:
            answer = answer + "d"*abs(xGap)
            if yGap > 0:
                answer = answer + "r"*abs(yGap)
            else: 
                answer = answer + "l"*abs(yGap)
        elif xGap < 0:
            if yGap > 0:
                answer = answer + "r"*abs(yGap)
            else: 
                answer = answer + "l"*abs(yGap)
            answer = answer + "u"*abs(xGap)

    else:
        remain = k - mustMove
        go = remain / 2
        back = remain / 2

        while xGap != 0 or yGap != 0 or go != 0 or back != 0:
        # 내려갈 수 있는 상황
            if xStart < n:
                if xGap > 0:
                    xStart += 1
                    xGap -= 1
                    answer = answer + "d"
                elif xMustDirection >= 0:
                    xStart += 1
                    go -= 1
                    answer = answer + "d"
                continue

            
            # 왼쪽으로 갈 수 있는 상황
            if yStart > 1:
                if yGap < 0:
                    yStart -= 1
                    yGap += 1
                    answer = answer + "l"
                else:
                    yStart -= 1
                    remain -= 1
                    answer = answer + "l"
                continue
                

            # 오른쪽으로 갈 수 있는 상황
            if yStart < m:
                if yGap > 0:
                    yGap -= 1
                    yStart += 1
                    answer = answer + "r"
                else:
                    remain -= 1
                    yStart += 1
                    answer = answer + "r"
                continue
                    

            # 위로 갈 수 있는 상황
            if xStart > 1:
                if xGap < 0:
                    xGap =+ 1
                    xStart -= 1
                    answer = answer + "u"
                else:
                    remain -= 1
                    xStart -= 1
                    answer = answer + "u"
                continue
            



    return answer


print(solution(3,4,2,3,3,1,5))
