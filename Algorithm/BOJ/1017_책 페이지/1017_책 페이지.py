import sys
input = sys.stdin.readline

## 진짜 싫다....
## 너무 짜증나는 문제...

def uu(res, length, count):
    last_num = int(n[length-count])

    if length - count == 0:
        for num in range(1,last_num):
            res[num] += 10**(count-1)
        else:
            x = n[1:]
            x = int(n[1:]) if x else 0
            res[last_num] += x + 1
        return print(*res)

    for i in range(1, 10):
        x = n[length-count+1:]
        x = int(n[length-count+1:]) if x else 0
        if i == last_num:
            if count == 1:
                res[i] += (int(n[:length-count]) + 1) * 10**(count-1)
            else:
                res[last_num] += int(n[:length-count]) * 10**(count-1) + x + 1
        elif i < last_num:
            res[i] += (int(n[:length-count]) + 1) * 10**(count-1)

        else:
            res[i] += (int(n[:length-count]))  * 10**(count-1)
    else:
        if last_num != 0:
            res[0] += (int(n[:length-count])) * 10**(count-1)
        else:
            res[0] += (int(n[:length-count])-1) * 10**(count-1) + x + 1
    uu(res, length, count+1)


n = input().rstrip()
length = len(n)
res = [0]*10
uu(res, length, 1)
