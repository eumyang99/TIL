import sys
input = sys.stdin.readline

## 너무나도 어려웠던 문제....
## 처음 발상은 각 국가에 승리확률*3 + 무승부 확률*1 로 해결했지만 틀린 논리다.
## 이런 식으로 하면 적은 확률로 이길 수 있는 시나리오가 잡히지 않는다.
## 무조건 승률이 높은 나라가 진출하는 것으로 계산된다.

## 따라서 6개의 모든 경기 중 3개의 경우(승, 무승부, 패)를 모둔 3**6번 계산해봐야 한다.
## 각각의 시나리오(6번의 경기를 마친)로 진행될 확률을 구하고,
## 그 시나리오에 따른 승점을 계산해서 진출 가능성을 구한다.
## 예를 들어 6번의 경우를 마친 시나리오의 확률이 20%라고 하자.
## 이 때 a:9, b:5, c:5, d:3 의 승점을 받는다고 하면
## a는 20% 확률로 진출한다. 따라서 a의 최종 확률에 20%를 더한다.
## b, c는 둘 중에 한 국가만 진출하기 때문에 이 시나리오의 경우 각각 20% / 2 의 확률로 진출한다.
## 따라서 b와 c의 최종 확률에 각각 10%를 더한다.
## d는 진출 자리가 없기 때문에 확률을 더하지 않는다.


## 파라미터는 현재 경기 번호(0~5), 해당 시나리오 누적 승점 딕셔너리, 시나리오 진행 확률 
def uu(match, each_score, per):
    global res
    ## 2.
    ## 마지막 경기를 마쳤을 때
    if match == 6:
        ## 누적 승점을 temp에 내림차순으로 담는다.
        temp = []
        for name, score in each_score.items():
            temp.append((name, score))
        temp.sort(key= lambda x: x[1], reverse=True)
        
        ## 1위군, 2위군, 3위군, 4위군을 나누는 과정이다.
        ## start는 각 군의 시작 idx
        ## 이전 국가의 승점과 비교해서 순위가 나뉘면 temp[start:i] 까지 rank에 담는다.
        ## start = i 로 갱신한다.
        rank = []
        start = 0
        for i in range(1, 4):
            if temp[i-1][1] > temp[i][1]:
                rank.append(temp[start:i])
                start = i
        ## 마지막으로 모든 국가를 rank에 담는다.
        else:
            rank.append(temp[start:])
        
        ## 2위군까지의 확률을 최종 res 딕셔너리에 더하는 과정이다.
        ## 진출자의 수는 2로 초기화
        winner = 2
        ## 각 1순위군부터 순회한다.
        for group in rank:
            ## 만약 winner의 자리가 없다면 그만!
            if winner <= 0:
                break
            ## 해당 순위군이 winner 자리에 모두 들어갈 수 있다면
            if winner >= len(group):
                ## 해당 순위군의 나라는 이 시나리오에서 100% 진출한다.
                ## 따라서 res에 per(시나리오 확률)을 그대로 더해준다.
                for name, score in group:
                    res[name] += per
                ## 그리고 winner의 숫자를 해당 순위군의 크기만큼 줄여준다.
                winner -= len(group)
            ## winner 자리는 있지만 해당 순위군이 winner 자리를 초과할 때,
            ## 확률을 나누어 가져가야 한다.
            else:
                for name, score in group:
                    ## 따라서 아래와 같은 확률을 res에 더해준다.
                    res[name] += per * (winner / len(group))
                ## 그리고 winner의 숫자를 해당 순위군의 크기만큼 줄여준다.
                ## for문 탈출용
                winner -= len(group)
        
        ## 이 시나리오는 끝났으니 return으로 함수를 되돌려준다.
        return
    
    ## 1.
    ## 재귀함수로 DFS를 돌린다.
    ## 각 매치에 따라 승점을 더해주면서 다음 파라미터로 경기 번호, 누적 승점 딕셔너리, 확률을 넘긴다.
    ## 행여 확률이 0인 경우 넘어간다.(그러한 시나리오는 없으니까! 또한 확률을 계속 누적곱을 해야 하는데 0을 곱하면 안되기 때문!)
    for i in range(2, 5):
        if float(lst[match][i]) != 0:
            new_match = match + 1
            new_each_score = {k: v for k, v in each_score.items()}
            new_per = per*float(lst[match][i])
            if i == 2:
                new_each_score[lst[match][0]] += 3
            elif i == 3:
                new_each_score[lst[match][0]] += 1
                new_each_score[lst[match][1]] += 1
            else:
                new_each_score[lst[match][1]] += 3
            uu(new_match, new_each_score, new_per)


country = input().split()
lst = [input().split() for _ in range(6)]

## 최종 확률을 저장할 res 딕셔너리
res = {}
for name in country:
    res[name] = 0

## 함수에 넣을 초기값 딕셔너리
each_score = {}
for name in country:
    each_score[name] = 0

uu(0, each_score, 1)

## 국가 순서대로 확률 출력
for name in country:
    print(res[name])
