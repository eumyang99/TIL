# useState

- **useState는 import 해서 사용한다.**

  - ```javascript
    import { useState } from "react";
    
    // React에서 import
    ```

  - ```javascript
    const [state, setState] = useState();
    
    /*
    state => 저장되어 사용되는 값
    setState => state에 변화된 값을 저장하는 함수
    useState( state의 초기값 )
    
    const [저장되어 사용되는 값, state에 변화된 값을 저장하는 함수] = useState(state의 초기값);
    */
    ```

  - ```javascript
    // 사용법 예시
    
    const onEvent = () => {
      setState( 기존 state에 새롭게 저장할 값 )
    }
    ```

- **컴포넌트는 자신이 가진 state 값이 갱신되면 렌더링을 다시 한다.**





