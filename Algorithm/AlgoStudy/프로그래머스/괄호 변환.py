# 문제에서 시키는 대로 재귀 로직의 코드를 구현하면 됨

def cut_reverse(left):
    res = ""
    for i in range(1, len(left) - 1):
        res = res + ("(" if left[i] == ")" else ")")
    return res


def solution(p):
    # 빈 문자열이면 반환
    if p == "":
        return ""

    # 여는 괄호면 +1, 닫는 괄호면 -1
    # 균형이 잡혀있다면 accu는 0이 될 것
    accu = 0
    # 문자열을 순회하며
    for i in range(len(p)):
        # 괄호에 맞게 accu 가감
        if p[i] == "(":
            accu += 1
        else:
            accu -= 1

        # 아직 균형 잡히지 않았다면 continue
        if accu:
            continue

        # 균형 잡혀있는데
        # 첫 괄호가 여는 괄호면 무조건 올바른 문자열
        # => 균형이 잡혔다는 것은 첫 여는 괄호를 닫는 괄호가 있다는 것
        # 첫 여는 괄호와 마지막 닫는 괄호 사이가 올바르지 않을 수가 없음
        # 올바르지 않다는 것은 닫는 괄호가 여는 괄호보다 먼저 나왔다는 것인데
        # 그러한 경우 먼저 나온 닫는 괄호에서 이미 올바른 괄호가 완성됨
        if p[0] == "(":
            return p[:i + 1] + solution(p[i + 1:])
        # 그렇지 않으면 틀린 문자열
        else:
            return "(" + solution(p[i + 1:]) + ")" + cut_reverse(p[:i + 1])
