import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999999)
def uu(case, cnt, memo):
    global res
    if cnt == 5:
        for x in range(n):
            maxi = max(memo[x])
            if res < maxi:
                res = maxi
        return 
    
    for direction in range(4):
        case.append(direction)
        uu(case, cnt+1, move(memo, direction))
        case.pop()

def move(memo, direction):
    temp_memo = [memo[i][:] for i in range(n)]
    if direction == 0: # 상
        for y in range(n):
            temp = []
            this_idx = 0
            next_idx = 1
            zero_cnt = 0
            while next_idx < n and this_idx < n:
                if temp_memo[this_idx][y] == 0:
                    this_idx += 1
                    next_idx = this_idx + 1
                    zero_cnt += 1
                    continue
                if temp_memo[next_idx][y] == 0:
                    next_idx += 1
                    zero_cnt += 1
                    continue
                if temp_memo[this_idx][y] == temp_memo[next_idx][y]:
                    temp.append(temp_memo[this_idx][y] * 2)
                    this_idx = next_idx + 1
                    next_idx = this_idx + 1
                    zero_cnt += 1
                else:
                    temp.append(temp_memo[this_idx][y])
                    this_idx = next_idx
                    next_idx = this_idx + 1
            else:
                if this_idx < n:
                    temp.append(temp_memo[this_idx][y])
                temp = temp + [0]*zero_cnt
                for i in range(n):
                    temp_memo[i][y] = temp[i]

    if direction == 1: # 우
        for x in range(n):
            temp = []
            this_idx = n-1
            next_idx = this_idx - 1
            zero_cnt = 0
            while next_idx >= 0 and this_idx >= 0:
                if temp_memo[x][this_idx] == 0:
                    this_idx -= 1
                    next_idx = this_idx - 1
                    zero_cnt += 1
                    continue
                if temp_memo[x][next_idx] == 0:
                    next_idx -= 1
                    zero_cnt += 1
                    continue
                if temp_memo[x][this_idx] == temp_memo[x][next_idx]:
                    temp.append(temp_memo[x][this_idx] * 2)
                    this_idx = next_idx - 1
                    next_idx = this_idx - 1
                    zero_cnt += 1
                else:
                    temp.append(temp_memo[x][this_idx])
                    this_idx = next_idx
                    next_idx = this_idx - 1
            else:
                if this_idx >= 0:
                    temp.append(temp_memo[x][this_idx])
                temp = temp + [0]*zero_cnt
                temp.reverse()
                for i in range(n):
                    temp_memo[x][i] = temp[i]

    if direction == 2: # 하
        for y in range(n):
            temp = []
            this_idx = n-1
            next_idx = this_idx - 1
            zero_cnt = 0
            while next_idx >= 0 and this_idx >= 0:
                if temp_memo[this_idx][y] == 0:
                    this_idx -= 1
                    next_idx = this_idx - 1
                    zero_cnt += 1
                    continue
                if temp_memo[next_idx][y] == 0:
                    next_idx -= 1
                    zero_cnt += 1
                    continue
                if temp_memo[this_idx][y] == temp_memo[next_idx][y]:
                    temp.append(temp_memo[this_idx][y] * 2)
                    this_idx = next_idx - 1
                    next_idx = this_idx - 1
                    zero_cnt += 1
                else:
                    temp.append(temp_memo[this_idx][y])
                    this_idx = next_idx
                    next_idx = this_idx - 1
            else:
                if this_idx >= 0:
                    temp.append(temp_memo[this_idx][y])
                temp = temp + [0]*zero_cnt
                temp.reverse()
                for i in range(n):
                    temp_memo[i][y] = temp[i]

    if direction == 3: # 좌
        for x in range(n):
            temp = []
            this_idx = 0
            next_idx = 1
            zero_cnt = 0
            while next_idx < n and this_idx < n:
                if temp_memo[x][this_idx] == 0:
                    this_idx += 1
                    next_idx = this_idx + 1
                    zero_cnt += 1
                    continue
                if temp_memo[x][next_idx] == 0:
                    next_idx += 1
                    zero_cnt += 1
                    continue
                if temp_memo[x][this_idx] == temp_memo[x][next_idx]:
                    temp.append(temp_memo[x][this_idx] * 2)
                    this_idx = next_idx + 1
                    next_idx = this_idx + 1
                    zero_cnt += 1
                else:
                    temp.append(temp_memo[x][this_idx])
                    this_idx = next_idx
                    next_idx = this_idx + 1
            else:
                if this_idx < n:
                    temp.append(temp_memo[x][this_idx])
                temp = temp + [0]*zero_cnt
                for i in range(n):
                    temp_memo[x][i] = temp[i]
    return temp_memo

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

res = 0
uu([], 0, lst)
print(res)