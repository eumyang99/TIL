# useEffect

- **컴포넌트 라이프 사이클**

  1. Mount
     - 컴포넌트가 처음 렌더링 되는 시점

  2. Update
     - 컴포넌트의 내용이 바뀌어 다시 렌더링 되는 시점
  3. Unmount
     - 컴포넌트가 사라지는 시점

  4. 참고
     - Detect : 컴포넌트 안의 특정 값의 변화만 감지하여 다시 렌더링



- **useEffect 사용법**

  - ```react
    // import 해서 사용
    
    import { useEffect } from "React"
    ```

  

  - Mount : 처음 렌더링 될 때만

    ```react
    import { useEffect } from "React"
    
    useEffect(()=> {
      console.log("Mount!")
    }, [])
    
    // 두 번째 인자에 빈 배열을 넣으면 컴포넌트가 마운트 될 때만 실행
    ```

  

  - Update : 업데이트 될 때

    ```react
    import { useEffect } from "React"
    
    useEffect(()=> {
      console.log("Update!")
    })
    
    // 두 번째 인자를 설정하지 않으면 컴포넌트가 업데이트 될 때만 실행
    ```

  

  - Unmount : 컴포넌트가 사라질 때

    ```react
    import { useEffect } from "React"
    
    useEffect(()=> {
      console.log("Mount!")
      
      return () => {
        // useEffect의 첫 번째 인자인 콜백 함수에 return 반환값은 Unmount 시점에 실행됨
        console.log("Unmount!")
      }
    })
    ```

  

  - Detect : 특정 값만 바뀔 때

    ```javascript
    import { useEffect } from "React"
    
    useEffect(()=> {
      console.log("Update!")
    }, [count])
    
    // 두 번째 인자에 들어가는 값이 변할 때만 실행
    // 이를 통해 해당 값에 조건을 걸어서 다른 작업을 할 수 있다
    ```

    

---

### 요약

- Mount : useEffect 두 번째 인자에 **빈배열**
- Update : useEffect 두 번째 인자가 **없음**
- Unmount : useEffect 첫 번째 인자의 **return**
- Detect : useEffect 두 번째 인자에 **[감지할 대상]**