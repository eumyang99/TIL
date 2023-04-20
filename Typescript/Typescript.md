# Typescript

1. types
2. method



## Types

- `string`
- `number`
- `boolean`
- `string[], number[]` 
  - `Array<string>`, `Array<number>`

- Tuple
  - `data : [string,number]`

- void, never

  - void

    - 함수값을 반환하지 않는 함수의 경우

    - ```typescript
      function sayHello(): void {
        console.log('hello')
      }
      ```

  - never

    - 항상 에러를 반환하거나 영원히 끝나지 않는 함수의 경우

    - ```typescript
      function showError(): never {
        throw new Error()
        
      }function infLoop(): never {
        while (true) {
          // 반복
        }
      }
      ```

- enum

  - ```typescript
    enum Os {
      Window,
      Ios,
      Android
    }
    
    // 자동 할당
    // Window 에는 1
    // Ios 에는 2
    // IAndroidos 에는 3
    
    // 수동 할당
    // Window 에는 3을 할당하면
    // Ios 에는 4
    // Android 에는 5
    ```

  - enum에 수동으로 값을 할당하지 않으면 0부터 차례대로 숫자가 할당된다

  - ```typescript
    // 양방향 매핑
    // 아래는 자동 할당의 경우
    enum Os {
      Window,
      Ios,
      Android
    }
    
    Os[0] = "Window"
    Os[1] = "Ios"
    Os[2] = "Android"
    
    Os["Window"] = 0
    Os["Ios"] = 1
    Os["Android"] = 2
    
    // 단방향 매핑
    // 아래는 수동 문자 할당의 경우
    enum Os {
      Window = "win",
      Ios = "ios",
      Android = "and"
    }
    
    Os.Window = "win"
    Os.Ios = "ios"
    Os.Android = "and"
    ```

- null, endefined

  - ```typescript
    let a:null = null
    let b:undefined = undefined
    ```



## interface

- property를 정의해서 객체를 표현하고자 할 때

- ```typescript
  interface User {
    name : string,
    age : number
  }
  
  let user : User = {
    name : "choa",
    age : 30
  }
  ```

- Optional Chaining

  - property가 있어도 되고 없어도 되는 경우

  - ```typescript
    interface User {
      name : string,
      age : number,
      gender? : string
    }
    
    let user : User = {
      name : "choa",
      age : 30
    }
    ```

- readonly

  - 초기에 할당된 값을 수정하지 못하도록 하는 경우

  - ```typescript
    interface User {
      name : string,
      age : number,
      gender? : string,
      readonly birthYear : number
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000
    }
    
    // 이 때 birthYear를 다시 수정하려고 하면 에러가 뜸
    user.birthYear = 1990 // 에러 발생
    ```

- 위 예시에서 User에 학년과 학점을 넣고 싶을 때

  - ```typescript
    interface User {
      name : string,
      age : number,
      gender? : string,
      readonly birthYear : number
      1 : string,
      2 : string,
      3 : string,
      4 : string,
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000
    }
    
    // 위의 경우 1,2,3,4 에 대한 모든 할당이 필요
    // 따라서 optional로 지정
    interface User {
      name : string,
      age : number,
      gender? : string,
      readonly birthYear : number
      1? : string,
      2? : string,
      3? : string,
      4? : string,
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000,
      1 : "A"
    }
    
    // optinal로 하기 불편하니
    // 이렇게 쳐리할 수 있음
    interface User {
      name : string,
      age : number,
      gender? : string,
      readonly birthYear : number
      // grade는 number고 이것을 key로 value가 string인 property를 여러개 받을 수 있음
    	[grade:number] : string
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000,
      1 : "A"
    }
    
    // 학점은 A, B, C, D 일 뿐인데 string으로 받으면 너무 범위가 넓으니
    // 학점을 Score Type으로 지정
    type Score = "A" | "B" | "C" | "D"
    
    interface User {
      name : string,
      age : number,
      gender? : string,
      readonly birthYear : number
    	[grade:number] : Score
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000,
      1 : "A"
    }
    ```

-  interface로 함수 정의

  - ```typescript
    // 예시 1
    interface Add {
      // number type의 인자를 두개 받고 
      // number type을 반환함
      (num1:number, num2:number) : number
    }
    
    const add : Add = function(x, y) {
      return x + y
    }
    
    // 예시 2
    interface IsAdult {
      (age:numebr) : boolean
    }
    
    const test : IsAdult = (age) => {
      return age > 19
    }
    ```

- interface로 class 정의

  - 자주 사용하지 않을 것 같아 차후에 정리

