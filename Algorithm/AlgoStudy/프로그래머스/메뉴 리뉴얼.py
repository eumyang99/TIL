## orders의 메뉴들을 문자열이 아닌 set으로 변환
## memo[교집합 사이즈 크기] = {"사이즈 크기에 맞는 메뉴 조합" : 교집합 횟수, ...}
## 모든 고객을 짝지으며 두 고객 간의 최대 교집합 메뉴를 찾고
## 최대 교집합 메뉴를 course에 포함된 사이즈 각각에 따라 조합
## 조합된 메뉴를 정렬 후 string으로 변환
## memo[조합된 메뉴 사이즈][변환된 string] += 1

## 위 작업을 모두 마치면 메뉴 사이즈에 따라 {겹치는 메뉴 : 빈도}를 알 수 있음
## 이후 memo를 순회하면서 해당 사이즈의 최대 빈도를 찾고
## 최대 빈도를 value로 하는 key(menu)를 answer에 추가

## answer 정렬 후 출력  

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    memo = [defaultdict(int) for _ in range(max(course) + 1)]
    len_orders = len(orders)
    ## orders의 string을 set으로 변환한 arr
    set_orders = list(map(set, orders))
    ## 모든 고객을 짝지으며
    for i in range(len_orders - 1):
        for j in range(i+1, len_orders):
            ## 두 고객의 최대 교집합 메뉴를 저장
            max_menu_set = set_orders[i] & set_orders[j]
            ## course 사이즈를 순회하며
            for size in course:
                ## 최대 교집합 메뉴를 각 course 사이즈로 조합된 메뉴들을 저장
                each_menu_arr = list(combinations(max_menu_set, size))
                if each_menu_arr:
                    ## 조합된 각 메뉴를 memo에 누적 기록
                    for each_menu in each_menu_arr:
                        menu = "".join(sorted(list(each_menu)))
                        memo[size][menu] += 1

    ## 메모를 순회하면서
    for dic_by_size in memo:
        ## 각 사이즈에 맞는 코스 메뉴들의 최대 빈도수를 찾고
        cnt_type = list(dic_by_size.values())
        if not cnt_type: continue
        max_cnt = max(cnt_type)
        ## 최대 빈도수를 가진 메뉴를 answer에 저장
        for menu, cnt in dic_by_size.items():
            if cnt == max_cnt:
                answer.append(menu)
    
    ## answer 정렬 후 출력
    answer.sort()
    return answer