## 핵심 발상
## 세 자리 이진수 9개 중 "110" 보다 큰 것은 "111" 밖에 없다
## 따라서 "111" 패턴이 등장할 때만 "110"을 앞으로 옮길 수 있다

def solution(s):
    answer = []
    for bin in s:
        res = ""
        ## 옮길 수 있는 "110"이 제외된 숫자 배열
        stack = []
        ## 옮길 수 있는 "110" 패턴 개수
        pattern = 0
        for num in bin:
            if len(stack) < 2 or num == "1":
                stack.append(num)
            else:
                if stack[-1] == "1" and stack[-2] == "1":
                    stack.pop()
                    stack.pop()
                    pattern += 1
                else:
                    stack.append(num)
        
        ## 슬라이딩 윈도우 개념 활용
        ## 마지막 남은 숫자가 1인 경우, 1을 맨 뒤로 보내기 위해서 추가로 1을 2개 더함
        stack = stack + ["1", "1"]
        ## stack에 남은 숫자를 앞에서부터 3개씩 확인
        for i in range(len(stack)-2):
            three_num = "".join(stack[i:i+3])
            ## 윈도우에 포함된 숫자가 "111"이면
            if three_num == "111":
                ## 삽입할 수 있는 모든 "110"을 먼저 삽입 후
                for _ in range(pattern):
                    res += "110"
                ## stack에 남은 숫자를 모두 더한 뒤 종료
                res += "".join(stack[i:-2])
                break
            ## 윈도우에 포함된 숫자가 "111"이 아닌 경우, "110"삽입할 필요가 없기 때문에
            else:
                ## stack[i]만 추가 후 다음 윈도우로 넘어감
                res += stack[i]
        ## stack을 모두 탐색한 뒤에도 삽입할 "110"이 남아 있다면
        else:
            ## 남은 "110"을 모두 덧붙임
            for _ in range(pattern):
                res += "110"
            
            
        answer.append(res)
    return answer