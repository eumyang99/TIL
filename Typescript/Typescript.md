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
    name : string
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
      name : string
      age : number
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
      name : string
      age : number
      gender? : string
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
      name : string
      age : number
      gender? : string
      readonly birthYear : number
      1 : string
      2 : string
      3 : string
      4 : string
    }
    
    let user : User = {
      name : "choa",
      age : 30,
      birthYear : 2000
    }
    
    // 위의 경우 1,2,3,4 에 대한 모든 할당이 필요
    // 따라서 optional로 지정
    interface User {
      name : string
      age : number
      gender? : string
      readonly birthYear : number
      1? : string
      2? : string
      3? : string
      4? : string
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

## 함수

- ```typescript
  // 기본적인 내용은 간단하니 많이 사용될 유용한 내용을 기재
  
  // 인자로 name을 받으면 return에 name을 반영
  // name을 받지 않으면 world 출력
  function hello(name? : string) {
    return `Hello, ${name || "world"}`
  }
  
  // 혹은 인자에 초기값을 할당
  function hello2(name = "world") {
    return `Hello, ${name}`
  }
  
  ```

- ```typescript
  // 함수에 인자로 여러개를 받아 array로 만드는 
  
  function add(...nums: number[]) {
    return nums.reduce((result, num) => result + num, 0)
  }
  
  add(1, 2, 3) // 6
  add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) // 55
  
  ```

- ```typescript
  interface User {
    name : string,
    age : number
  }
  
  function join(name: string, age:number | string): User | string {
    if (typeof age === "number") {
      return {
      	name,
      	age
    	}
    } else {
      return "나이는 숫자로 입력!"
    }
  }
  
  const sam: User = join("Sam", 30)
  const jane: string = join("Jane", "30")
  // 위의 경우 age가 number 일 때도 User나 string 타입을 반환할 수 있고
  // age가 string 일 때도 User나 string 타입을 반환할 수 있기 때문에 에러가 뜸
  
  // 따라서 함수에 오버로드를 해서 해결할 수 있음
  interface User {
    name : string,
    age : number
  }
  function join(name: string, age:number): User
  function join(name: string, age:string): string
  // 이렇게 하면 age가 number일 때는 User 반환
  // age가 string 일 때 string 반환
  // 따라서 age는 number와 string이 들어올 수 있고
  // 각각에 따라 반환되는 타입이 1:1 대응이 되기 때문에 해결됨 
  function join(name: string, age:number | string): User | string {
    if (typeof age === "number") {
      return {
      	name,
      	age
    	}
    } else {
      return "나이는 숫자로 입력!"
    }
  }
  
  const sam: User = join("Sam", 30)
  const jane: string = join("Jane", "30")
  ```

## Generic

- 해당 타입의 변수를 설정하는 시점에 타입을 지정함
- 조금 더 유동적으로 타입 설정이 가능

- ```typescript
  function getSize<T>(arr): number {
    return arr.length
  }
  
  const arr1 = [1, 2, 3]
  getSize<number>(arr1) // 3
  
  const arr2 = ["a", "b", "c"]
  getSize<string>(arr2) // 3
  
  const arr3 = [false, true, true]
  getSize<boolean>(arr3) // 3
  
  const arr4 = [{}, {}, { name:"Tim" }]
  getSize<object>(arr4) // 4 
  ```

- ```typescript
  interface Mobile<T> {
    name: string
    price: number
    option: T
  }
  
  const m1: Mobile<object> = {
    name: "s21",
    price: 1000,
    option: {
      color: "red",
      coupon: false
    }
  }
  
  const m2: Mobile<string> = {
    name: "s20",
    price: 900,
    option: "good"
  }
  
  // option Mobile 타입을 따르면서도 option에 다양한 타입의 데이터가 할당될 수 있음
  // m1 의 경우 option엔 object
  // m2 의 경우 string이 할당
  ```

## keyof

- interface의 key값들만 가져옴

- ```typescript
  interface User {
  	id: number
  	name: string
  	age: number
  	gender: "m" | "f"
  }
  
  type UserKey = keyof User // "id" | "name" | "age" | "gender"

## Partial

- interface의 일부 property만 사용 가능

- ```typescript
  interface User {
  	id: number
  	name: string
  	age: number
  	gender: "m" | "f"
  }
  
  let admin: Partial<User> = {
    id: 1,
    name: "Bob"
  }
  ```

## Required

- interface의 일부 property가 optional일 경우에도 필수로 사용해야만 함

- ```typescript
  interface User {
  	id: number
  	name: string
  	age?: number
  
  }
  
  let admin: Required<User> = {
    id: 1,
    name: "Bob",
    age: 30
  }
  ```

## Readonly

- interface의 일부 property가 optional일 경우에도 필수로 사용해야만 함

- ```typescript
  interface User {
  	id: number
  	name: string
  	age?: number
  }
  
  let admin: Readonly<User> = {
    id: 1,
    name: "Bob",
  }
  
  // admin.id = 4 에서 admin의 id를 바꿀 수 없음
  ```

## Record

- Record<K, T> 에서 K는 key, T는 type

- ```typescript
  const score: Record<"1" | "2" | "3" | "4", "A" | "B" | "C" | "D" > = {
    1: "A",
    2: "c",
    3: "B",
    4: "D"
  }
  
  // 위 부분을 정리하면
  type Grade = "1" | "2" | "3" | "4"
  type Score = "A" | "B" | "C" | "D" | "F"
  
  const score: Record<Grade, Score> = {
    1: "A",
    2: "C",
    3: "B",
    4: "D"
  }
  ```

- ```typescript
  interface User {
  	id: number
  	name: string
  	age: number
  }
  
  function isValid(user: User) {
    const result: Record<keyof User, boolean> = {
      	id: user.id > 0,
  			name: user.name !== "",
  			age: user.age > 0
    }
    return result
  }
  ```

## Pick

- interface의 일부 property만 골라서 사용할 때

- ```typescript
  interface User {
  	id: number
  	name: string
  	age: number
    gender: "M" | "W"
  }
  
  const admin: Pick<User, "id" | "name"> = {
    id: 0,
    name: "Bob"
  }
  
  // User의 id와 name만 가져와서 타입을 사용할 수 잇음
  ```

## Omit

- interface의 일부 property만 제외하고 사용할 때

- ```typescript
  interface User {
  	id: number
  	name: string
  	age: number
    gender: "M" | "W"
  }
  
  const admin: Omit<User, "id" | "name"> = {
    id: 0,
    name: "Bob"
  }
  ```

## Exclude

- 일부 타입을 제거하고  사용할 때

- ```typescript
  type T1 = string | number | boolean
  type T2 Exclude<T1, number | string>
  
  // 이 때 T2의 type은 number와 string이 제거되고 boolean만 남음
  ```

## NonNullable

- type에서 null과 undefined를 제거

- ```typescript
  type T1 = string | number | null | undefined | void
  type T2 NonNullable<T1>
  
  // 이 때 T2의 type은 null undefined 제거되고 string, number, void 남음
  ```

## 
