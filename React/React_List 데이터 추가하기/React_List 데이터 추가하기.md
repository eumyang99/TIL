# List 데이터 추가하기

- 자식 컴포넌트 간 데이터 전송
  - 부모 컴포넌트를 통해서 전달



- 컴포넌트 구조
  - CompoA -> CompoList
  - CompoA -> CompotEditor
  - CompoList 와 CompotEditor 는 모두 CompoA 의 자식 컴포넌트



- CompoA

  ```javascript
  import CompoList from "./CompoList";
  import CompotEditor from "./CompotEditor";
  
  import { useRef, useState } from "React";
  
  const ComponentA = () => {
    // data는 내가 사용할 리스트
    const [data, setData] = useState([]);
  	
    // 리스트 사용할 때 map 메소드를 사용하려면 리스트 자식요소 모두 고유한 key값을 받아야 함
    // 따라서 리스트 요소가 추가될 때마다 고유한 id 번호를 속성에 넣어주기 위한 초기값 설정
    const dataId = useRef(0);
  	
    // 리스트 추가하는 함수
    const onCreate = (a, b, c) => {
      const newItem = {
        a,
        b,
        c,
        
        // useRef 사용
        id: dataId.current,
      };
      
      // useRef 사용 후 +1
      dataId.current += 1;
      
      // 추가된 리스트 요소를 리스트 맨 앞으로 설정 후 state에 저장
      setData([newItem, ...data]);
    };
  
    return (
      <div>
  			// 함수를 prop
        <CompotEditor onCreate={onCreate} />
  
  			// 리스트를 사용할 컴포넌트로 리스트를 prop
        <CompoList addedList={data} />
      </div>
    );
  };
  
  export default ComponentA;
  
  ```

- CompotEditor

  ```javascript
  import { useState } from "React";
  
  // onCreate 함수를 prop 받음
  const CompotEditor = ({ onCreate }) => {
    
    // 이 useState는 실제로 렌더링되는 form의 입력란 값
    const [state, setstate] = useState({
      // 입력란은 비어 있어야 하기 때문에 빈 문자열로 설정
      a: "",
      b: "",
      c: "",
    });
  	
    // a란에 a를, b란에 b를, c란에 c를 입력 받았다고 가정하고 state 갱신
    setstate({ ...state, a: "a", b: "b", c: "c" });
    
    // 여기서 부모 컴포넌트의 리스트 요소를 추가하는 함수인 onCreate를 실행
    onCreate(state.a, state.b, state.c);
  
    return <div></div>;
  };
  
  export default CompotEditor;
  ```

- CompoList

  ```javascript
  // 부모 컴포넌트의 state가 onCreat함수로 갱신이 되면 갱신된 리스트가
  // 이 컴포넌트로 전달되고 여기서 사용하면 됨
  
  const CompoList = ({ addedList }) => {
    return <div></div>;
  };
  
  CompoList.defualtProps = {
    addedList:[]
  }
  
  export default CompoList;
  ```

  

