## 내 방법
## 각 자리수의 글자가 포함하고 있는 모든 경우를 cnt_arr에 담음
## 규칙 : A(n+1) = 5*A(n) + 1
## 둘째 자리가 "I"인 경우,
## cnt_arr[1 : 둘째 자리] * ["A","E","I","O","U"].index("I") + 1
alphabet = ["A","E","I","O","U"]

cnt_arr = [1]
def make_cnt(cnt, depth):
    if depth == 5: return
    cnt_arr.append(cnt*len(alphabet) + 1)
    make_cnt(cnt_arr[-1], depth + 1)

def solution(word):
    answer = 0
    make_cnt(cnt_arr[0], 1)
    cnt_arr.sort(reverse = True)
    
    for i in range(len(word)):
        text = word[i]
        text_num = alphabet.index(text)
        answer += cnt_arr[i] * text_num + 1

    return answer


## 규칙 : A(n+1) = 5*A(n) + 1 점화식을 일반항으로 만들어서 푸는 방법
## A(n) = (5**n - 1) / (5 - 1)
def solution(word):
    answer = 0    
    for i, alpha in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(alpha) + 1

    return answer