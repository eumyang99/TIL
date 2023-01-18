### Spread 연산자

- 반복되는 property를 상속 받는 연산자 :   **...**  

- object

  ```javascript
  const cookie = {
      base : "cookie",
      madeIn : "korea"
  }
  
  const chocochipCookie = {
      ...cookie,
      toping: "chocochip"
  }
  
  // 일 때
  
  console.log(chocochipCookie)
  
  
  // 결과
  // {base : "cookie", madeIn : "korea", toping: "chocochip"}
  
  ```

- array

  ```javascript
  const noTopingCookies = ["A", "B"];
  const topingCookies = ["C", "D", "E"];
  
  const allCookies = [...noTopingCookies, "함정쿠키", ...topingCookies];
  
  console.log(allCookies)
  
  // 결과
  // ["A", "B", "함정쿠키", C", "D", "E"]
  
  ```

  

  