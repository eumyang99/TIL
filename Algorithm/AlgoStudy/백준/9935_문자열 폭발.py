import sys
input = sys.stdin.readline

words = input().rstrip()
bomb = input().rstrip()


## 결과물을 담을 array를 따로 만들 필요가 없다는 것을 이제야 깨달음...
## stack array만 사용해서 풀어봄

stack = []
for i in range(len(words)):
    stack.append(words[i])                          # 일단 알파벳을 스택에 담고
    if words[i] == bomb[-1]:                        # 방금 담은 알파벳이 bomb의 마지막 글자와 같을 때(bomb가 터질 첫번째 조건 감지)
        if "".join(stack[-len(bomb):]) == bomb:         # stack의 마지막 문자열이 bomb와 같다면(bomb 완성)
            for _ in range(len(bomb)):                  # stack에 쌓인 bomb을 pop으로 제거한다.
                stack.pop()


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))



# 옛날에 (()))()) 이런 식으로 예제가 주어지는 stack 문제를 풀어봤었음
# 이때 ()이게 완성되면 제거하는 건데(오늘 문제처럼)
# 이 문제가 "(" 와 ")" 열림과 닫힘이라는 의미가 있어서 여기에 생각이 갇혀 "쌍"을 찾아서 해결하는 거라고 생각했음

# 이런 접근으로 오늘 문제를 풀려고 했었음
# 그런데 오늘 문제는 쌍을 찾아서 제거하는 것이 아니고 같은 문자열을 만족해야 하는 거였어서 처음에 난감했음

# 이제와서 생각해보니 스택에서 제거하는 행위는 제거조건을 만족하는 마지막 요소를 찾는게 핵심인 것 같다는 생각이 들었음
# 마지막 요소 이전에 등장하는 것들은 중요하지 않음
# - "(" 이 녀석 보다는 ")" 이 녀석에 주목하는 것
# - 오늘 같은 문제는 폭탄의 마지막 문자에 주목하는 것

# 마지막 요소를 찾은 뒤, 나머지 조건을 만족하는 지 확인하면 됨

# 그래서 차후 유사한 문제를 만나면 스택에서 제거할 마지막 요소를 감지하는 데에 신경을 써볼 예정






