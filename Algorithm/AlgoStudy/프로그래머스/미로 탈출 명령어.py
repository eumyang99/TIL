## 발상

## 추가로 이동할 때, D로 이동하면 U로, L로 이동하면 R로 꼭 짝을 맞추어 이동해야 함

## Start에서 End로 도착하는 필수 방향 빈도 저장(DLRU 우선순위)
## 현재 위치에서 "DLRU" 우선순위로 갈 수 있으면 무조건 보냄
## 단, 필수 방향에 있으면 해당 방향 cnt 감소시키면서 저장된 방향 먼저 사용
## 그렇지 않다면 이동하면서 추가로 이동해야 하는 cnt를 감소시키면서 반대 방향을 필수 방향에 추가
## 추가로 이동해야 하는 cnt를 다 소모하면
## 필수 방향에 저장된 모든 정보를 "DLRU" 순서대로 모두 사용

direction = "dlru"
dx, dy = [1,0,0,-1], [0,-1,1,0]

def solution(n, m, x, y, r, c, k):
    answer = ""
    ## 필수 row 이동 크기, 필수 col 이동 크기
    x_dist, y_dist = r - x, c - y
    ## 추가로 이동해야 하는 거리
    adding_dist = k - (abs(x_dist) + abs(y_dist))
    ## 추가로 이동해야 하는 거리가 0보다 작거나(k가 부족)
    ## 홀수(짝이 맞지 않아서 도착 못함)라면 impossible 반환
    if adding_dist < 0 or adding_dist % 2: return "impossible"
    
    ## borad 범위 체크 함수
    def in_board(x, y):
        if 1 <= x < n+1 and 1 <= y < m+1:
            return True
        return False

    ## 필수 방향 빈도를 저장할 dic
    necessary_dic = dict()
    for dir in direction:
        necessary_dic[dir] = 0
    else:
        necessary_dic["d" if 0 < x_dist else "u"] = abs(x_dist)
        necessary_dic["r" if 0 < y_dist else "l"] = abs(y_dist)
    
    ## 추가 이동은 짝을 맞춰 이동하기 때문에 짝의 개수 = 추가 이동거리 // 2 
    adding_cnt = adding_dist // 2
    ## 짝의 개수를 다 소모하면 종료
    while 0 < adding_cnt:
        ## "DLRU" 순서대로 순회
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            ## borad 범위 밖이면 다음 방향 체크
            if not in_board(nx, ny): continue
            ## answer에 체크된 방향 추가
            answer += direction[i]
            ## 만약 해당 방향이 필수 방향에 있으면
            if necessary_dic[direction[i]]:
                ## cnt 감소
                necessary_dic[direction[i]] -= 1
            ## 필수 방향에 없으면 새로운 추가 이동의 짝이기 때문에
            else:
                ## 반대 방향을 필수 방향에 추가
                necessary_dic[direction[abs(i-3)]] += 1
                ## 짝의 개수 감소
                adding_cnt -= 1
            ## 현재 위치 재설정 후 방향 탐색 종료
            x, y = nx, ny
            break

    ## 짝을 다 소모했으면 필수 방향에는 꼭 가야만 하는 방향들만 남음        
    for dir, cnt in necessary_dic.items():
        ## "DLRU" 순서대로 answer에 남은 cnt만큼 추가
        answer += dir * cnt
                
    return answer

## 문제를 풀고도 여전히 헷갈렸던 점
## adding_cnt를 소모하는 while문에
## 필수 방향에 있는 것을 사용하면서 필수 방향에 새롭게 추가하는 방향이 섞이면
## adding_cnt를 다 소모하고 마지막에 일괄 더하는 작업에서 범위 문제가 발생하지 않을까 헷갈렸다.

## 해결 : 필수 방향에 있는 것들은 무조건 해당 방향에 대한 공간이 확보된 상태
## [ 초기 필수 방향 ] : 당연히 범위를 초과할 수 없음
## [ while문에서 answer에 추가한 방향의 반대 방향 ] : answer에 방향을 추가하면서 동시에 반대 방향에 대한 공간이 확보하는 꼴
## 이기 때문에 범위 문제가 발생하지 않음