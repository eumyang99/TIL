# 파이썬 코드 작성법

- **주석**
  - 한 줄 주석
    - 주석 처리될 내용 앞에 '#' 입력
  - 여러줄 주석
    - 한 줄씩 #을 사용(문장 드래그 후 Ctrl + /)
    - ''' 이나 """ 으로 묶음
- **식별자**
  - 변수 이름 규칙
    - 영문, 언더스코어(_), 숫자로 구성
    - 첫 글자에는 숫자 X
    - 대소문자 구별
    - ['False', 'None', 'True', '**__**peg_parser**__**', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 는 예약어로 사용할 수 없음
    - 내장 함수나 모듈 등의 이름도 사용하지 않아야 함

---





# 연산자



	## 산술 연산자

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   **   | 거듭제곱 |