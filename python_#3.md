# for문

- str은 for문으로 한글자씩 가져올 수 있다.

  - ```python
    a = 'class'
    for idx in a:
        print(idx)
    #c
    #l
    #a
    #s
    #s
    ```

  

- dict는 for문으로 가져오면 키 값만 나온다.

  - ```python
    grades = {'A' : 80, 'B' : 90}
    for student in grades:
        print(student)
    #A
    #B
    ```

  - 그러나 `.items()`를 활용하면 키와 밸류 모두 가져올 수 있다.

  - ```python
    grades = {'A' : 80, 'B' : 90}
    for student, grade in grades.items():
        print(student, grade)
    ```

  - `.keys()`를 활용하면 키 값만,  `.valuse()`를 활용하면 밸류 값만 가져올 수 있다.

  

- enumerate()

  - (index, value) 형태의 '튜플'로 만들어준다

    - ```python
      members = ['A', 'B', 'C']
      for idx, member in enumerate(members):
          print(idx, member)
          
      #0 A
      #1 B
      #2 C
      ```

  

- List comprehension

  - code / for 변수 in iterable

  - code / for 변수 in iterable / if 조건식

    ```python
    cubic_list = [] #리스트를 먼저 만들고
    for number in range(1, 4): #1, 2, 3
        cubic_list.append(number ** 3) #cubic_list 리스트에 number**3을 추가
    print(cubic_list)
    ```

    ```py
    cubic_list = [number ** 3 for number in range(1, 4)]
    #[]리스트 기호 안에 <code / for 변수 in iterable>을 바로 입력
    print(cubic_list)
    ```

    위 두 코드는 같은 코드

  

- Dictionary comprehension

  - {key: value for 변수 in iterable}

  - {key: value for 변수 in iterable if 조건식}

    ```py
    cubic_dict = {} #딕셔너리를 먼저 만들고
    for number in range(1, 4): #1, 2, 3
        cubic_list[number] : number ** 3 
        #cubic_dict에 <number> key와 <number **3> value를 추가
    print(cubic_dict)
    ```

    ```py
    cubic_dict = {number: number ** 3 for number in range(1, 4)}
    #{}딕셔너리 기호 안에 <'key'와 value가 될 'code' / for 변수 in iterable>을 바로 입력
    print(cubic_dict)
    ```

    위 두 코드는 같은 코드

  

- for문의 else

  - break 없이 for문이 끝나면 else가 실행

    - ```python
      integers = tuple(range(1,6))
      for i in integers:
          if i % 2 ==1:
              print(i)
      else:
          print('끝')
      
      #1
      #3
      #5
      #끝
      ```

---



# 함수

## 함수의 입력

- 패킹 / 언패킹

  - 패킹

    - ```py
      numbers = (1,2,3,4,5) #패킹
      print(numberes) #(1,2,3,4,5)
      ```

  - 언패킹

    - ```py
      numbers = (1,2,3,4,5)
      a, b, c, d, e = numbers #언패킹
      print(a, b, c, d, e) #1 2 3 4 5
      ```

    - ```py
      numbers = (1,2,3,4,5)
      
      a, b *rest = numbers
      print(a, b, rest) #1 2 [3, 4, 5]
      
      a, *rest, e = numbers
      print(a, rest ,e) #1 [2, 3, 4] 5
      ```

    

  - Asterisk (*)와 가변 인자

    - `*`  -> 시퀀스 언패킹 연산자

      - `*`를 사용해서 가변 인자를 만들 수 있다.

      - ```py
        def func(*args):
            print(args)
            print(type(args))
        
        func(1,2,3,'a','b')
        #(1,2,3,'a','b')
        #<class 'tuple'
        ```

      - 가변 인자 예시

        - ```python
          def sum_all(*numbers): #함수에 들어가는 인자를 (1,2,3,4,5,6)으로 튜플로 패킹
              result=
              for number in numbers:
                  result += number
              return result
          
          print(sum_all(1,2,3,4,5,6)) #21

        

        - ```python
          def family_name(father, mother, *pets):
              print(f'아버지 : {father}')
              print(f'어머니 : {mother}')
              print('동물들---')
              for name in pets:
                  print(f'동물 : {name}')
          
          family_name('아빠', '엄마', '초코', '뽀삐')
          #아버지 : 아빠
          #어머니 : 엄마
          #동물들---
          #동물 : 초코
          #동물 : 뽀삐
          ```


      

    - 가변 키워드 인자(**kwargs)

      - **kwargs는 딕셔너리로 묶여서 처리된다.

        - ```python
          def family_name(father, mother, **pets): 
              print(f'아버지 : {father}')
              print(f'어머니 : {mother}')
              if pets: #pets가 있으면
                  print('동물들---')
                  for animals, name in pet.items(): #dog='초코'와 cat='뽀삐' 입력
                      print(f'{animals} : {name}')
                     
          family_name('아빠', '엄마', dog='초코', cat='뽀삐')
          #아버지 : 아빠
          #어머니 : 엄마
          #동물들---
          #동물 : 초코
          #동물 : 뽀삐
          ```

      - *args와 **kwargs 동시 사용 예시

        - ```python
          def family_name(*parents, **pets):
              print(f'아버지 : {parents[0]}')
              print(f'어머니 : {parents[1]}')
              if pets:
                  print('동물들---')
                  for animals, name in pets.items():
                      print(f'{animals} : {name}')
                     
          family_name('아빠', '엄마', dog='초코', cat='뽀삐')
          
          #아버지 : 아빠
          #어머니 : 엄마
          #동물들---
          #dog : 초코
          #cat : 뽀삐
          ```



## 함수의 범위(Scope)

- Python 이름 검색 규칙
  - LEGB Rule : LEGB 순서로 이름을 찾아나간다.
    - Local scope
    
    - Enclolsed scope
    
    - Global scope
    
    - Built-in scope
    
      

- global 문

  - 현재 코드 블럭 전체에 적용된다.

    - ```python
      # 함수 내부에서 글로벌 변수를 변경
      a = 10
      def func1():
          global a #local 에서 global 변수 지정
          a = 3 #local 에서 global 변수 값을 변경
      
      print(a) # 10 -> 함수 func1이 실행되기 전에 a 값인 10
      func1() # 함수 실행
      print(a) # 3 -> 함수에서 a의 값을 변경
      #global 키워드를 사용하지 않았다면 local에 한정되어 a 변수가 생성되는 것
      ```

  - 주의1 : global에 나열된 이름은 같은 코드 블럭에서 global 앞에 나올 수 없다.

    - ```python
      # 주의1
      a = 10
      def func1():
          print(a) # global a 선언 전에 a를 사용
          global a
          a = 3
      
      print(a)
      func1()
      print(a)
      #SyntaxError가 등장
      ```

  - 주의2 : global에 나열된 이름은 파라미터, for 루프 대상, class/함수 정의 등으로 정의되지 않아야 한다.

    - ```python
      # 주의2
      a = 10
      def func1(a): # 파라미터에 global 사용
          global a
          a = 3
      
      print(a)
      func1()
      print(a)
      #SyntaxError가 등장
      ```

  

- nonlocal

  - 둘러싸고 있는 가장 가까운 scope의 변수를 연결한다.

    - ```python
      #nonlocal 예시
      x = 0
      def func():
          x = 1
          def func2():
              nonlocal x #eclosed scope인 func1의 변수 x를 지정
              x = 2 #eclosed scope인 func1의 변수 x를 변경
          func2()
          print(x) # 2
          
      func1()
      print(x) # 0
      ```

  - global과 달리 이미 존재하는 이름과 연결만 가능하다.

    - ```python
      # global에서는 선언된 적 없는 변수를 만들 수 있다
      def func1():
          global out #out이라는 선언된 적 없는 변수를 생성
          out = 3 #out에 3 할당
          
      func1() # func1을 실행
      print(out) # 3
      ```

    - ```python
      # nonlocal은 선언된 적 없는 변수를 활용할 수 없다
      def func1():
          def func2():
              nonlocal y # y는 앞서 선언된 적이 없는 변수다.
              y = 2
          func2()
          print(y)
          
      func1()
      # SyntaxError가 등장
      ```

  - 주의1 : nonlocal에 나열된 이름은 같은 코드 블럭에서 nonlocal 앞에 나올 수 없다.(=global문)

  

- 함수의 범위 주의

  - 기본적으로 함수에서 선언된 변수는 local 범위에 생성되고 함수가 종료되면 사라진다.
  - 해당 범위에 변수가 없으면 LEGB 순서로 이름을 검색한다.
    - 변수에 접근만 가능하고 수정할 수는 없다.
  - 상위 범위에 있는 변수를 수정하고 싶으면 global이나 nonlocal을 활용한다.
    - 하지만 코드가 복잡해지니 가급적 사용하지 말고 함수로 값을 바꾸러면 항상 argument로 넘기고 return 값을 사용하는 것이 좋다.

  

## 함수 응용

- map 함수 : `map(function, iterable)`

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(fuction)을 적용하고 그 결과가 True이 것을 map object로 반환

  - ```python
    numbers = [1,2,3]
    result = map(str, numbers)
    print(result, type(result)) # <map object at 0x0000023B8C806E20> <class 'map'> 바로 출력되지 않고 클래스가 'map'로 나옴
    print(list(result)) # ['1', '2', '3'] -> 이를 list로 형변환하여 확인
    ```

  

- filter 함수 : `filter(function, iterable)`

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(fuction)을 적용하고 그 결과가 True이 것을 filter object로 반환

  - ```python
    # 홀수 고르기
    def odd(n):
        return n % 2 # 나머지 0과 1을 반환
    nummers = [1,2,3]
    result = filter(odd, numbers) # 나머지가 1인 경우 True이기 때문에 해당 요소만 반환
    print(result, type(result)) # <filter object at 0x000001A58FB75E80> <class 'filter'> 바로 출력되지 않고 클래스가 'filter'로 나옴
    print(list(result)) # [1, 3] -> 이를 list로 형변환하여 확인
    ```

  

- zip 함수 : `zip(*lterables)`

  - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

  - ```python
    female = ['a','b']
    male = ['1', '2']
    pair = zip(female, male)
    print(pair, type(pair)) # <zip object at 0x00000236D49BF980> <class 'zip'> 바로 출력되지 않고 클래스가 'zip'으로 나옴
    print(list(pair)) #[('a', '1'), ('b', '2')] -> 이를 list로 형변환하여 확인
    ```

  

- lambda 함수 : lambda [parameter] : 표현식

  - 표현식을 계산한 결과값을 반환하는 함수

  - return문을 가질 수 없음

  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음

  - 함수를 간결하게 사용 가능

  - def를 사용할 수 없는 곳에서도 사용가능

  - ```python
    # 직육면체 부피 구하는 공식 - def 사용
    def cuvoid_volume(x, y, z):
        return x*y*z
    print(cuvoid_volume(3, 4, 5)) # 60
    
    # 직육면체 부피 구하는 공식 - lambda 사용
    cuvoid_volume = lambda x, y, z : x*y*z
    print(cuvoid_volume(3,4,5)) # 60
    ```

  

- 재귀 함수(recursive function)

  - 자기 자신을 호출하는 함수

  - 1개 이상의 base case(종료되는 상황)가 존재하고 수렴하도록 작성한다

  - ```python
    def factorial(n):
        if n == 1: # n이 1이 되면
            return 1 # 1을 반환
        else: # 그게 아니라면
            return n * factorial(n-1) # n과 f(n-1)을 곱해줘
    
    print(factorial(5)) # 120
    ```