import sys
input = sys.stdin.readline

n, atk = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]

res = 1
hp = 1 # 필요한 HP
for type, a, b in lst:
    if type == 1: # 몬스터
        share, remain = divmod(b, atk)
        if remain == 0: # 딱뎀일 경우
            hp += (share-1) * a
        else: # 막타 쳐야할 경우
            hp += share * a
    else: # 포션
        atk += a # 공격력 상승
        if hp - b >= 1: # 뒤에 영향을 미치는 정도 내에서 회복시켜줬을 때
            res = max(res, hp) # 지금까지 필요했던 HP 갱신
            hp = hp - b # 필요 HP 줄여주기
        else: # 필요 이상 회복시켜줬을 때
            res = max(res, hp) # 지금까지 필요했던 HP 갱신
            hp = 1 # 새로 시작

# 마지막까지의 전투가 가장 필요 HP가 높을 수 있으니 갱신
else:
    res = max(res, hp)

print(res)
