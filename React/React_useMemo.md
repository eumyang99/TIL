# useMemo

- 메모이제이션(memoization)

  - 이미 계산된 결과를 불필요하게 재연산하지 않도록 결과값을 기억하고 바로 꺼내오는 최적화 방법

- useMemo

  - ```react
    // import해서 사용
    import {useMemo} from "React"
    ```

- useMemo 사용법

  ```react
  // 기존 함수와 함수 실행 및 반환값 저장
  const helloWorld = () => {
    return "helloWorld"
  }
  const greeting = helloWorld()
  
  
  /*
    //useMemo 적용
    useMemo(A, B)에서 A에 기존 콜백함수를 넣는다.
    useMemo(A, B)에서 B에 변화 감지될 값을 넣는다.
  */
  const helloWorld = useMemo(() => {
    return "helloWorld"
  },[state.length])
  
  // 위의 경우 state.length가 달라지면 hellowWorld가 실행된다
  // state의 길이는 그대로, 값만 수정된다면 hellowWorld는 실행되지 않는다.
  
  // useMemo의 반환값은 문자 그대로 값이기 때문에
  // helloWorld()처럼 함수 실행으로 사용하지 않는다
  const greeting = helloWorld
  
  ```

  

  - useMemo 적용 전

  ```react
  // useMemo 적용 전
  const getDiaryAnalysis = () => {
    if (data.length === 0) {
      return { goodcount: 0, badCount: 0, goodRatio: 0 };
    }
  
    const goodCount = data.filter((it) => it.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100.0;
    return { goodCount, badCount, goodRatio };
  };
  
  /*
    컴포넌트가 렌더링 될 때마다 getDiaryAnalysis함수가 실행됨
    내가 원하는 것은 goodCount, badCount, goodRatio 에 영향을 미치는 값이 달라졌을 때만
    getDiaryAnalysis함수를 실행시켜서 다시 계산하기를 원함
  */
  
  // 현재 getDiaryAnalysis는 함수이기 때문에 getDiaryAnalysis() 이렇게 사용해야 함
  const { goodCount, badCount, goodRatio } = getDiaryAnalysis();
  ```

  

  - useMemo 적용 후

  ```react
  // useMemo 적용 후
  import {useMemo} from "React"
  
  // useMemo
  const getDiaryAnalysis = useMemo(() => {
    if (data.length === 0) {
      return { goodcount: 0, badCount: 0, goodRatio: 0 };
    }
  
    const goodCount = data.filter((it) => it.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100.0;
    return { goodCount, badCount, goodRatio };
  },[data.length]);
  
  /*
    data.length가 변할 때만 getDiaryAnalysis를 실행해서 재연산을 하고
    그렇지 않으면 기존에 연산된 결과를 재사용 한다
  */
  
  // getDiaryAnalysis 값을 저장
  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;
  ```

  

  
