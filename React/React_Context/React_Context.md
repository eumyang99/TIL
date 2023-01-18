# Context

- 자손의 자손 컴포넌트로 prop을 연달아 내리는 prop drilling 막기 위해 하나의 같은 문맥 아래에 있는 컴포넌트들에게 직통으로 prop을 내릴 수 있다.



- Context 생성 및 Context Provider를 통한 데이터 공급

  ```react
  // import
  import React from "React"
  
  // Context 생성
  // 다른 컴포넌트에서 사용해야 하니 export 해줘야 함
  export const MyContext = React.createContext(defaultValue)
  
  // 데이터 공급
  <MyContext.Provider value={전역으로 전달하고자 하는 값}>
    {/* 이 Context 안에 위치할 자식 컴포넌트들 */}
  </MyContext.Provider>
  
  ```

  - 참고 : export default 와 export의 차이

    ```react
    import React, {
      useCallback,
      useEffect,
      useMemo,
      useReducer,
      useRef,
      createContext,
    } from "react";
    
    // 위 예시에서 React는 export default로 내보내는 것
    // 비구조화 할당을 통해서만 import를 받을 수 있는 것은 export const의 경우
    ```



---

- 사용 예시

  - 상위 컴포넌트에서 context 생성

  ```react
  // state 값을 전달하는 Context
  export const DiaryStateContext = React.createContext();
  
  // 함수를 전달하는 Context
  export const DiaryDispatchContext = React.createContext();
  ```

  - 둘을 나누어서 Context를 생성한 이유

    ```react
    // state : state 값
    // onCreate, onRemove, onEdit : 함수
    
    <DiaryStateContext.Provider value={data, onCreate, onRemove, onEdit}>
    </DiaryStateContext.Provider>
    
    // 위처럼 전달하는 경우 state의 값이 바뀔 경우 prop하는 value 자체가 바뀌는 것이기 때문에 DiaryStateContext.Provider 컴포넌트가 리렌더링 된다.
    // 그럼 DiaryStateContext.Provider 컴포넌트의 자식 컴포넌트들(이 Context를 구독하는 모든 컴포넌트)도 불필요하게 모두 리렌더링 된다.
    // 위 같은 경우 세 개의 함수 모두 useCallback을 적용했으나 그래도 이 Context를 구독하는 모든 자식 컴포넌트 자체에서부터 먼저 렌더링 된다.
    
    // 이처럼 불필요한 렌더링 막기 위해서
    
    // data : state
    // memoizedDispatches : prop할 함수들을 useMemo로 묶어서 저장
    const [data, dispatch] = useReducer(reducer, []);
    const memoizedDispatches = useMemo(() => {
      return onCreate, onRemove, onEdit;
    }, []);
    
    <DiaryStateContext.Provider value={data}>
      <DiaryDispatchContext.Provider value={memoizedDispatches}>
        <div className="App">
          
          <DiaryEditor />
          <DiaryList />
        
        </div>
      </DiaryDispatchContext.Provider>
    </DiaryStateContext.Provider>
    
    
    // 1. 함수들을 구독하는 자식 컴포넌트들은 value에 state가 없어서 state의 변화에 반응하지 않는다.
    // 2. 함수들은 메모이제이션 되어있어서 state의 변화에 따른 부모 컴포넌트의 리렌더링에도 함수는 재정의 되지 않는다.
    // 3. 함수가 재정의 되지 않으니 함수를 구독하는 자식 컴포넌트는 리렌더 되지 않는다.
    
    ```
  
  
  - 하위 컴포넌트에서 Context 사용
  
   ```react
   // 하위 A 컴포넌트 : DiaryDispatchContext 사용
   
   // useContext import
   import { useContext } from "react";
   
   // Context import
   import { DiaryDispatchContext } from "./App";
   
   // DiaryDispatchContext라는 Context 객체 중 사용할 것을 가져와서 할당 
   const { onCreate } = useContext(DiaryDispatchContext);
   
   ```
  
  ```react
  // 하위 B 컴포넌트 : DiaryDispatchContext 사용
  
  // useContext import
  import { useContext } from "react";
  
  // Context import
  import { DiaryDispatchContext } from "./App";
  
  // DiaryDispatchContext라는 Context 객체 중 사용할 것을 가져와서 할당 
  const { onEdit, onRemove } = useContext(DiaryDispatchContext);
  
  ```
  
  ```react
  // 하위 C 컴포넌트 : DiaryStateContext 사용
  
  // useContext import
  import { useContext } from "react";
  
  // Context import
  import { DiaryStateContext } from "./App";
  
  // DiaryStateContext라는 Context 객체 중 사용할 것을 가져와서 할당
  const { data } = useContext(DiaryStateContext);
  ```
  
  