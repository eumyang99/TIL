# useCallback

- 함수에 사용하는 React.memo와 유사하다.
  - useCallback은 prop하는 **함수**에 사용
  - React.memo는 prop하는 **값**에 사용
- 부모 컴포넌트가 리렌더링 될 때 A함수가 재정의 된다면 A함수가 아무런 변화가 없더라도 A함수를 prop받는 컴포넌트도 리렌더링 된다.
- 자식 컴포넌트는 기존의 A함수와 재정의된 A함수의 차이를 알지 못한다.
  - prop받는 객체를 구분하지 못했던 것 처럼...
- 이런 불필요한 리렌더링을 막기 위해 함수에 memoization을 적용하는 기능이다.



- 사용법

  ```react
  // import 해서 사용
  import { useCallback } from "react";
  
  // 첫번째 인자에 적용할 함수를 넣고 두번째 인자에 dependency를 리스트에 담는다
  // dependency
  // : 이 값이 변경되는 것을 감지하면 새롭게 작동하고 그렇지 않다면 memoization된 것을 사용한다.
  const onStar = useCallback(()=>{},[]);
  ```
  
  
  
- 사용 예시

  ```react
  // import 해서 사용
  import { useCallback, useState } from "react";
  
  // prop할 함수에 대해 useCallback으로 감싸준다
    const onCreate = useCallback((author, content, emotion) => {
      const created_date = new Date().getTime();
      const newItem = {
        author,
        content,
        emotion,
        created_date,
        id: dataId.current,
      };
  
      dataId.current += 1;
      
      // setData에 콜백함수를 넣어 data를 갱신한다
      // 콜백함수는 data를 인자로 받아서
      // 새롭게 추가된 newItem을 data리스트의 맨 앞으로 추가한 리스트를 반환한다
      setData((data) => [newItem, ...data]);
    // 여기서는 dependency를 설정하지 않았다
    // 이 코드의 경우 onCreate는 data가 변하는 것과 상관없이
    // 이 onCreate함수가 실행될 때만 실행되어야 하는 상황이다
    }, []);
  
  ```
  





---

### 참고

```react
  const onCreate = useCallback((author, content, emotion) => {
    const created_date = new Date().getTime();
    const newItem = {
      author,
      content,
      emotion,
      created_date,
      id: dataId.current,
    };

    dataId.current += 1;
    setData([newItem, ...data]);
  }, []);

```

1. 바로 위 예시의 onCreate에서 사용하는 data는 첫 렌더링 때 빈 배열이다.

   - 이 때 onCreate 함수 속 data는 빈 배열로 고정

2. 이후 API를 가져와서 data는 값을 가지게 된다.

   - data가 갱신이 되었어도 dependency가 없어서 여전히 useCallback 함수 속 data는 빈 비열이다.

3. onCreate로 인해 새로운 데이터가 기존의 data에 추가되어야 하는데 실제 data는 API를 통해 데이터를 가지고 있지만

   이 콜백함수의 data는 빈 배열이기 때문에 새롭게 추가된 데이터 하나만을 state의 data에 저장한다.


4. 따라서 기존 API를 통해 가져온 데이터들은 모두 사라지고 새롭게 추가된 데이터만 남는다.

5. 이 문제를 해결하기 위해 onCreate 함수가 실시간의 데이터를 반영하도록 하기 위해 사용 예시에서는 setData의 인자로

   실시간의 data를 반영하는 콜백 함수를 담은 것이다.
