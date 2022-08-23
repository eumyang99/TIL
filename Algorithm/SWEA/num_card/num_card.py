import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    n = int(input())
    card = input()

    card_lst = [int(card[i]) for i in range(len(card))]

    cnt = [0]*10
    for i in card_lst:
        cnt[i] += 1


    alot_card = 0
    max_card = 0
    for i in range(len(cnt)):
        if cnt[i] >= max_card:
            max_card = cnt[i]
            alot_card = i

    print(f'#{case+1} {alot_card} {cnt[alot_card]}')
