# 열을 먼저 뒤집고 행을 뒤집음(행을 뒤집고 열을 뒤집어도 상관없음)

# 1.
# 첫 행에서 "앞뒤가 다른 동전"의 열들을 모두 뒤집으면서 cnt를 올려줌(필요한 열을 최소로 뒤집는 과정)
# 이후 모든 행들 검사하면서 해당 행에서 또 열을 뒤집어야 하는 경우는 불가능한 경우, -1
# 각 행의 동전은 target과 모두 같게 있거나 다르게 있어야 함
# 다르게 있는 경우 해당 행은 뒤집어야 하기 때문에 cnt를 올려줌

# 2.
# 첫 행에서 "앞뒤가 같은 동전"의 열들을 모두 뒤집으면서 cnt를 올려줌
# 이후 과정은 동일

# 두 경우로 나눈 이유는 다른 열을 모두 뒤집고 행을 뒤집는 것보다
# 같은 열을 뒤집고 행을 뒤집는 것이 더 빠를 수 있기 때문

def check(diff, TF, r_size, c_size):
    accu = 0
    for j in range(c_size):
        if diff[0][j] == TF:
            continue
        accu += 1
        for i in range(r_size):
            diff[i][j] = not diff[i][j]

    for i in range(r_size):
        if accu == -1:
            break
        val = diff[i][0]
        for j in range(c_size):
            if diff[i][j] != val:
                accu = -1
                break
        else:
            if val:
                accu += 1
    return accu


def solution(beginning, target):
    r_size, c_size = len(target), len(target[0])
    diff = [[False for _ in range(c_size)] for _ in range(r_size)]

    for i in range(r_size):
        for j in range(c_size):
            if beginning[i][j] == target[i][j]:
                continue
            diff[i][j] = True

    diff_1 = [diff[i][:] for i in range(r_size)]
    diff_2 = [diff[i][:] for i in range(r_size)]

    check_arr = sorted([check(diff_1, True, r_size, c_size),
                       check(diff_2, False, r_size, c_size)])
    for answer in check_arr:
        if -1 < answer:
            return answer
    else:
        return -1
