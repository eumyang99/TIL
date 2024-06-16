def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    name_idx = {}
    for i in range(len(enroll)):
        name_idx[enroll[i]] = i
    
    parent = [i for i in range(len(enroll))]
    for child in range(len(referral)):
        parent_name = referral[child]
        if parent_name == "-": continue
        parent[child] = name_idx[parent_name]
    
    for i in range(len(seller)):
        seller_idx, money = name_idx[seller[i]], amount[i] * 100
        while 1 <= money:
            stollen_money = money // 10
            answer[seller_idx] += money - stollen_money
            if seller_idx == parent[seller_idx]: break
            seller_idx = parent[seller_idx]
            money = stollen_money
            
    return answer