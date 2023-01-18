# React.Memo

- React.Memo

  - 최적화를 위해 불필요한 렌더링을 막고 기존의 컴포넌트를 재사용하기 위한 기능

  - prop 받은 데이터가 변경되었을 때만 렌더링을 다시하고 그렇지 않은 경우 memoization으로 기존 값을 재사용 한다.

    

- React.Memo 사용법

  - ```react
    // import해서 사용
    import React from "React"
    ```

  - ```react
    const ComponentName = React.Memo(컴포넌트 콜백함수, 렌더링 여부를 결정할 T/F값)
    ```

  - ```react
    const counterA = ({ props}) => {
      return <div>하하</div>
    }
    
    // 위 컴포넌트에 React.Memo를 적용하면
    const counterA = React.Memo(({ props }) => {
      return <div>하하</div>
    })
    
    // 위 컴포넌트가 객체를 prop 받으면 두 번째 인자 설정
    const counterA = React.Memo(({ props }) => {
      return <div>하하</div>
    },T/F값)
    
    // T/F값은 기존 데이터와 변경된 데이터가 실질적으로 같은지를 판단하는 함수의 반환값을 입력
    ```

    

- useMemo 사용 예시

  ```react
  import React, { useEffect, useState } from "react";
  
  
  //////// 자식 컴포넌트 A
  const CounterA = React.memo(({ count }) => {
    
    // 업데이트되어 다시 렌더링 되는지 확인하는 useEffect
    useEffect(() => {
      console.log(`CounterA Update - count : ${count}`);
    });
    
    // count 값을 렌더링하는 자식 컴포넌트 A
    return <div>{count}</div>;
  });
  
  //////// 자식 컴포넌트 B
  const CounterB = ({ obj }) => {
    
    // 업데이트되어 다시 렌더링 되는지 확인하는 useEffect
    useEffect(() => {
      console.log(`CounterB Update - count : ${obj.count}`);
    });
    
    // count 값을 렌더링하는 자식 컴포넌트 B
    return <div>{obj.count}</div>;
  };
  
  
  // 자식 컴포넌트 B의 경우 객체를 prop 받음
  // 객체의 경우 객체 안의 값이 동일하게 변경되더라도(실질적으로 변하지 않음)
  // 두 객체를 다르게 판단하고 다시 렌더링을 함
  // ex) 키 180cm의 코난과 키 180cm의 도일이는 내용은 같지만 다른 사람이다.
  // 따라서 두 객체의 내용이 같은지 확인하는 함수를 만들어서 리렌더링 실행 여부를 판단한다
  const areEqual = (prevProps, nextProps) => {
    
    // boolean 값을 반환
    return prevProps.obj.count === nextProps.obj.count;
  };
  
  
  // CounterB 컴포넌트를 React.memo의 첫 번째 인자로 담고
  // 두 번째 인자로 artEqual(boolean)값을 담아서
  // true이면 넘어가고 false이면 다시 렌더링 함
  const MemoizedCounterB = React.memo(CounterB, areEqual);
  
  const OptimizeTest = () => {
    
    // CounterA 컴포넌트에 prop할 내용
    const [count, setCount] = useState(1);
    // CounterB 컴포넌트에 prop할 내용
    const [obj, setObj] = useState({
      count: 1,
    });
  
    return (
      <div style={{ padding: 50 }}>
        <div>
          <h2>Counter A</h2>
          <CounterA count={count} />
          <button onClick={() => setCount(count)}>A button</button>
        </div>
        <div>
          <h2>counter B</h2>
          <MemoizedCounterB obj={obj} />
          <button
            onClick={() =>
              setObj({
                count: obj.count,
              })
            }
          >
            B button
          </button>
        </div>
      </div>
    );
  };
  
  export default OptimizeTest;
  ```







---

## 요약

- ```react
  const ComponentName = React.Memo(컴포넌트 콜백함수, 렌더링 여부를 결정할 T/F값)
  ```

  
