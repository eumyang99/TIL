from collections import deque

import sys
input = sys.stdin.readline

## 그냥 단순 bfs 돌리면 풀리는 이상한 문제...
## 분기 처리를 해도 안 해도 풀린다.

def move(x, y, y_cap):
    total = x + y

    if total >= y_cap:
        y_res = y_cap
    else:
        y_res = total
    
    x_res = total - y_res
    return x_res, y_res


a_cap, b_cap, a_target, b_target = map(int, input().split())
a_drum, b_drum = 0, 0

visited = set()

# 0 : a / 1 : b
# 0 : fill / 1 : empty / 2 : move

que = deque([(0, 0, 0, 0, 0), (1, 0, 0, 0, 0)])
while que:
    drum, oper, a_drum, b_drum, cnt = que.popleft()

    if a_drum == a_target and b_drum == b_target:
        print(cnt)
        break

    if (drum, oper, a_drum, b_drum) in visited:
        continue

    visited.add((drum, oper, a_drum, b_drum))

    if oper == 0: ## 채우기
        if drum == 0:
            new_a_drum = a_cap
            new_b_drum = b_drum
        else:
            new_b_drum = b_cap
            new_a_drum = a_drum

        for this_drum in range(2):
            for op in range(3):
                if op == 0:
                    if drum == this_drum:
                        continue
                    else:
                        if drum == 0 and b_drum == b_cap:
                            continue
                        if drum == 1 and a_drum == a_cap:
                            continue 
                
                elif op == 1:
                    if drum == this_drum:
                        continue
                    else:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue
                
                elif op == 2:
                    if drum != this_drum:
                        if drum == 0 and a_drum == 0:
                            continue
                        if drum == 1 and b_drum == 0:
                            continue

                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))
    elif oper == 1:
        if drum == 0:
            new_a_drum = 0
            new_b_drum = b_drum
        else:
            new_b_drum = 0
            new_a_drum = a_drum
        
        for this_drum in range(2):
            for op in range(3):
                if drum == this_drum:
                    continue
                else:
                    if op == 0:
                        if drum == 0 and b_drum == b_cap:
                            continue
                        if drum == 1 and a_drum == a_cap:
                            continue 

                    elif op == 1:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue
                    
                    elif op == 2:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue

                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))

    else:
        if drum == 0:
            new_a_drum, new_b_drum = move(a_drum, b_drum, b_cap)
        else:
            new_b_drum, new_a_drum = move(b_drum, a_drum, a_cap)
    
        for this_drum in range(2):
            for op in range(3):
                if drum == this_drum:
                    if op == 2:
                        continue
                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))

else:
    print(-1)


from collections import deque

import sys
input = sys.stdin.readline

def move(x, y, y_cap):
    total = x + y

    if total >= y_cap:
        y_res = y_cap
    else:
        y_res = total
    
    x_res = total - y_res
    return x_res, y_res


a_cap, b_cap, a_target, b_target = map(int, input().split())
a_drum, b_drum = 0, 0

visited = set()

# 0 : a / 1 : b
# 0 : fill / 1 : empty / 2 : move

que = deque([(0, 0, 0, 0, 0), (1, 0, 0, 0, 0)])
while que:
    drum, oper, a_drum, b_drum, cnt = que.popleft()

    if a_drum == a_target and b_drum == b_target:
        print(cnt)
        break

    if (drum, oper, a_drum, b_drum) in visited:
        continue

    visited.add((drum, oper, a_drum, b_drum))

    if oper == 0: ## 채우기
        if drum == 0:
            new_a_drum = a_cap
            new_b_drum = b_drum
        else:
            new_b_drum = b_cap
            new_a_drum = a_drum

        for this_drum in range(2):
            for op in range(3):
                if op == 0:
                    if drum == this_drum:
                        continue
                    else:
                        if drum == 0 and b_drum == b_cap:
                            continue
                        if drum == 1 and a_drum == a_cap:
                            continue 
                
                elif op == 1:
                    if drum == this_drum:
                        continue
                    else:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue
                
                elif op == 2:
                    if drum != this_drum:
                        if drum == 0 and a_drum == 0:
                            continue
                        if drum == 1 and b_drum == 0:
                            continue

                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))
    elif oper == 1:
        if drum == 0:
            new_a_drum = 0
            new_b_drum = b_drum
        else:
            new_b_drum = 0
            new_a_drum = a_drum
        
        for this_drum in range(2):
            for op in range(3):
                if drum == this_drum:
                    continue
                else:
                    if op == 0:
                        if drum == 0 and b_drum == b_cap:
                            continue
                        if drum == 1 and a_drum == a_cap:
                            continue 

                    elif op == 1:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue
                    
                    elif op == 2:
                        if drum == 0 and b_drum == 0:
                            continue
                        if drum == 1 and a_drum == 0:
                            continue

                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))

    else:
        if drum == 0:
            new_a_drum, new_b_drum = move(a_drum, b_drum, b_cap)
        else:
            new_b_drum, new_a_drum = move(b_drum, a_drum, a_cap)
    
        for this_drum in range(2):
            for op in range(3):
                if drum == this_drum:
                    if op == 2:
                        continue
                que.append((this_drum, op, new_a_drum, new_b_drum, cnt+1))

else:
    print(-1)
