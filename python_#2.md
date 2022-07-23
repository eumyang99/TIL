# 비시퀀스형 컨테이너

## 셋(Set)

- Set : 중복되는 요소 없이 순서에 상관 없는 데이터들의 묶음

- 순서에 상관이 없어 인덱스 사용이 불가

- 담고 있는 요소 삽입, 변경, 삭제 가능 -> 가변형

- 셋(Set) 생성

  - 중괄호 `{}` 혹은 `set()`으로 생성
  - 빈 Set을 만들기 위해서는 반드시 `set()`을 사용해야 함

- 셋(Set) 사용하기

  - 셋을 사용하면 중복된 값을 쉽게 제거할 수 있음, 단 이후 순서 무시됨

    ``` python
    A = ['1', '1', '2', '3', '3', '3', '4', '5']
    print(len(set(A))) # 4
    
    print(set(A)) # {'4', '1', '2', '3', '5'} 실행 마다 순서 변경됨
    ```

- 셋(Set) 연산자

  - `|` : 합집합

  - `&` : 교집합

  - `-` : 차집합

  - `^` : 대칭차집합

    - ```python
      A_set = {1, 2, 3, 4}
      B_set = {1, 2, 3, "Hello", (1,2,3)}
      
      print(A_set | B_set) # {1, 2, 3, 4, 'Hello', (1, 2, 3)}
      
      print(A_set & B_set) # {1, 2, 3}
      
      print(A_set - B_set) # {4}
      
      print(A_set ^ B_set) # {4, 'Hello', (1, 2, 3)}
      ```



## 딕셔너리(Dictionary)

- 딕셔너리(Dictionary) : 키-값(key-value) 쌍으로 이루어진 자료형

- 딕셔너리(Dictionary)의 key는 변경 불가능한(immutable) 데이터만 활용 가능

  - string, integer, float, boolean, tuple, range

- 반면에 values는 형태에 구애 받지 않는다.

- 딕셔너리(Dictionary) 생성

  - 중괄호`{}` 혹은 `dict()`로 생성

  - key를 통해 value에 접근

    - ```python
      dict_a = {'a': 'red', 'b': 'blue', 'lst':[1,2,3]}
      print(dict_a) # {'a': 'red', 'b': 'blue', 'lst': [1, 2, 3]}
      print(dict_a['a']) # red
      print(dict_a['b']) # blue
      print(dict_a['lst']) # [1, 2, 3]
      
      dict_b = dict(a='red', b='blue', lst=[1,2,3])
      print(dict_b) # {'a': 'red', 'b': 'blue', 'lst': [1, 2, 3]}
      ```



## 형변환

- 암시적 형 변환(implicit)
  -  사용자의 의도와 관계 없이 파이썬 내부적으로 자료형을 변환하는 것
- 명시적 형 변환(explicit)
  - 사용자가 특정 함수를 활용해서 의도적으로 자료형을 변환하는 것



- 암시적 형 변환

  - bool

  - numeric type(int, float)

    - ```python
      print(True + 10) # 11
      print(3 + 10.0) # 13.0
      ```

- 명시적 형 변환

  - int
    - str, float -> int
    - 단, 정수 형식이 아닌 str 이거나 정수 형식이 아닌 float 인 경우는 불가능

  - float
    - str, int -> float
    - 단, float 형식이 아닌 str은 불가
  - str
    - int, float, list, tuple, dict -> str