import sys
input = sys.stdin.readline


def left_search(idx):
    l_idx = idx - 1
    while l_idx in used and l_idx != 0:
        l_idx -= 1
    return l_idx

def right_search(idx):
    r_idx = idx + 1
    while r_idx in used and r_idx != n:
        r_idx += 1
    return r_idx


n = int(input())

lst = []
calc = [float("inf")]

for i in range(n):
    if i == 0:
        x, y = map(int, input().split())
        lst.append(x)
        lst.append(y)
    else:
        x, y = map(int, input().split())
        lst.append(y)

for i in range(n-1):
    calc.append(lst[i] * lst[i+1] * lst[i+2])
else:
    calc.append(float("inf"))
    
res = 0
used = set()
for _ in range(n-1):
    min_num = min(calc)
    min_idx = calc.index(min_num)
    for i in range(n+1):
        if calc[i] == min_num and i not in used:
            if lst[i] > lst[min_idx]:
                min_idx = i
    res += min_num
    used.add(min_idx)
    calc[min_idx] = float("inf")

    changing_left_idx = left_search(min_idx)
    changing_right_idx = right_search(min_idx)

    if changing_left_idx != 0:
        left_num_idx = left_search(changing_left_idx)
        calc[changing_left_idx] = lst[left_num_idx] * lst[changing_left_idx] * lst[changing_right_idx]

    if changing_right_idx != n:
        right_num_idx = right_search(changing_right_idx)
        calc[changing_right_idx] = lst[right_num_idx] * lst[changing_right_idx] * lst[changing_left_idx]

print(res)

