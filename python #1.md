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

## 산술연산자

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   **   | 거듭제곱 |

---





# 자료형

- 수치형
- 문자열
- 불린형
- None

## 수치형

- int (정수형)

- float (실수형)

  - 부동 소수점 : 2진법을 사용하는 컴퓨터는 `3.2 - 3.1`과 `1.2 - 1.1`의 결과를 다르게 냄

  - 해결법

    - ``` python
      a = 3.2 - 3.1 # 0.10000000000009
      b = 1.2 - 1.1 # 0.09999999999987
      
      # 1. 임의의 작은 수 활용
      print(abs(a-b) <= 1e-10) # True
      
      # 2. math 모듈 활용
      import math
      print(math.isclose(a, b)) # True
      ```

---



## 문자열

- 따옴표 안에 따옴표를 표현할 경우

  - 작은따옴표가 들어 있는 경우 큰따옴표로 문자열 생성
  - 그 반대도 가능

- 삼중 따옴표

  - ``` python
    print('''문자열 안에 '작은따옴표'나 "큰따옴표"를 사용할 수 있음''')
    # 출력 결과
    문자열 안에 '작은따옴표'나 "큰따옴표"를 사용할 수 있음
    ```

- Escape sequence

  - | 예약 문자 |   내용(의미)    |
    | :-------: | :-------------: |
    |    \n     |     줄 바꿈     |
    |    \t     |       탭        |
    |    \r     |   캐리지 리턴   |
    |    \0     |    널(Null)     |
    |    \\\    |        \        |
    |    \\'    | 단일인용부호(') |
    |    \\"    | 이중인용부호(") |

- 문자열 연산

  - 문자열 덧셈과 곱셈

    ``` python
    print("hello" + "World") #Helloworld
    print("Python" * 3) # PythonPythonPython
    ```

- String Interpolation

  - %-formatting

    - `%s %A`는 %s 자리에 A가 str으로
    - `%d %B`는 %d 자리에 B가 int로
    - `%f %C`는 %f 자리에 C가 float로

  - str.format()

    - ``` python
      name = 'Ryu'
      score = 4.5
      
      print('hello, {}!!! 성적은 {}'.format(name, score))
      #Hello, Ryu!!! 성적은 4.5
      ```

  - f-strings

    - ``` python
      name = 'Ryu'
      score = 4.5
      print(f'Hello, {name}!!! 성적은 {score}')
      #Hello, Ryu!!! 성적은 4.5
      
      pi = 3.141592
      print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓ㅅ이는 {pi*2*2}')
      # 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368   // 계산 가능
      ```

---



## 불린형

- True / False

- 비교 연산자

  - <, <=, >, >=, ==, !=, is, is not

- 논리 연산자

  - | 연산자  |              내용              |
    | :-----: | :----------------------------: |
    | A and B |    A와 B 모두 True시, True     |
    | A or B  |   A와 B 모두 False시, False    |
    |   Not   | True를 False로, False를 True로 |

  - Falsy : False는 아니지만 False 취급 되는 값

    - 0, 0.0, (), [], {}, None, ""(빈 문자열)

  - 논리 연산자 우선순위

    - Not, and, or 순으로 우선순위가 높음

    - ``` python
      print(not True) # False
      print(not 0) # True
      print(not 'hello') #False
      print(not Ture and False or not False) # True
      print(((not True) and False) or (not False)) # 위 식과 동일 True
      ```

  - 논리 연산자의 단축 평가

    - 앞의 결과가 확실하면 뒤를 확인하지 않고 첫 번째 값 반환

    - ``` python
      print(3 and 5) #5, and는 5까지 확인을 해봐야 하기 때문
      print(3 and 0) #0, 위와 같고 0은 False 취급
      print(0 and 3) #0, 앞에서 먼저 False 취급하는 0이 있기 때문에 뒤를 확인하지 않음
      
      a = 5 and 4
      print(a) # 4
      
      b = 5 or 3
      print(b) # 5
      
      c = 0 and 5
      print(c) # 0
      
      d = 5 or 0
      print(d) #5
      ```

---



# 컨테이너



## 컨테이너 분류

- 시퀀스형 : 리스트(가변형), 튜플(불변형), 레인지(불변형)
- 비시퀀스형 : 세트(가변형), 딕셔너리(가변형)



## 시퀀스형

- 리스트 : 여러 개의 값을 **순서가 있는 구조로 저장**

  - 리스트 생성과 접근

    - 대괄호[ ] 혹은 list() 로 생성
    - 리스트 포함 모든 자료형을 리스트에 담을 수 있음
    - 내용 변경 가능 : 가변형

  - list[i]로 값에 접근

    ``` py
    list_a = ['A', 'B', 'C', 'D', 'E']
    print(list_a[0]) # A
    ```

  - 요소 변경

    ``` python
    list_a = ['A', 'B', 'C', 'D', 'E']
    list_a[2] = '사과'
    print(list_a) # ['A', 'B', '사과', 'D', 'E']
    ```

---



- 튜플 : 여러 개의 값을 **순서가 있는 구조로 저장**하는데 값을 변경할 수 없음

  - 튜플 생성과 접근

    - 소괄호 () 혹은 tuple() 로 생성
    - 튜플은 수정 불가한 시퀀스. 인덱스로 접근 가능

  - tuple[i]로 값에 접근

    ``` python
    a = (1, 2, 3, 1)
    print(a[1]) # 2
    ```

  - 튜플 생성 주의사항

    - 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 ,(쉼표)를 붙여야 함

      ``` python
      tuple_a = (1,) # 쉼표를 붙여야 함
      a = 1, # 괄호 없이 쉼표만으로도 튜플 생성됨
      print(type(a)) # ,<class 'tuple'>
      ```

    - 복수 항목일 경우에는 쉼표가 필요 없지만 붙이는 것을 추천

      ``` python
      tuple_a = (1, 2, 3,)
      a = 1, 2, 3,
      print(type(a)) # ,<class 'tuple'>
      ```

  - 튜플 대입

    - 우변의 값을 좌변의 변수에 한 번에 할당하는 과정

      ``` python
      x, y = 1, 2
      x, y = (1, 2)
      # 두 과정은 동일하게 튜플로 처리됨
      ```

  ---

  

- 레인지 : 숫자의 시퀀스를 나타내기 위해 사용, 주로 반복문과 함께 사용

  - range의 사용 방법

    - 기본형  range(n) : 0 ~ n-1 까지의 숫자 시퀀스

    - 범위 지정 range(n, m) : n ~ m-1 까지의 숫자 시퀀스

    - 범위 및 스텝 지정 : range(n, m, s) : n ~ m-1 까지 s만큼 증가시키는 숫자 시퀀스

      ``` python
      print(list(range(1, 10, 2))) # [1, 3, 5, 7 ,9]
      
      #역순
      print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2, 1]
      print(list(range(6, 1, -2))) # [6, 4, 2]
      print(list(range(6, 1, 1)))  # []
      ```

      