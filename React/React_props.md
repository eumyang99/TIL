# Props

- **Props = Properties**

  

- **Props는 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 것이다.**

  - 어떤 값도 전달이 가능하지만 함수도 전달이 가능하다.

  - 함수 전달을 통해 자식에게 함수를 실행시키도록 해서 자식이 부모에게 데이터를 전달할 수 있게 한다.

  - 자식 컴포넌트는 부모 컴포넌트 안에서도 생성이 가능하지만 보통 같은 경로에 새로운 javascript 파일을 만들어서 import 하여 사용한다.

  - ```javascript
    // 자식 컴포넌트 생성
    
    const Child = () => {
      return <div> 렌더링 되는 부분 </div>;
    };
    
    // 밖에서 쓸 사용할 수 있도록 내보내는 코드
    export default Child;
    ```

  - ```javascript
    // 부모 컴포넌트에서 사용
    
    // 자식이 부모 안에 없을 때는 import해서 사용
    import Child from "./Child";
    
    const App = () => {
      return (
        <div className="App">
        
        	<Child /> // 부모 컴포넌트에 렌더링 되는 부분에 자식 컴포넌트를 렌더링 함
        
        </div>
      );
    };
    ```

  

- **부모 컴포넌트에서 자식 컴포넌트로 데이터 전달**

  - ```javascript
    // 부모 컴포넌트에서 전달
    import Child from "./Child";
    
    // 전달할 데이터
    const someData = 'star'
    const anyData = 'moon'
    
    const App = () => {
      return (
        <div className="App">
        
        	// 자식이 받아서 쓸 데이터 이름={보낼 데이터} 형식으로 전달
        	<Child someData={someData} anyData={anyData} />
        
        </div>
      );
    };
    ```

  - ```javascript
    // 자식 컴포넌트에서 받음
    
    // props을 받으면 다른 정보가 포함된 props객체로 전달되기 때문에
    // 사용할 데이터만  { 전달 받은 데이터 이름 }와 같은 방법으로 꺼내서 사용한다.
    const Child = ({ someData, anyData }) => {
      
      
      // 받은 데이터를 가공해서 사용할 수도 있고
      const propData = someData;
    
      
      return (
        <div>
        
          // 바로 렌더링 할 수도 있음
          <h3>{anyData}</h3>
        
        </div>
      );
    };
    
    export default Child;
    ```

    

  - 보낼 데이터가 많으면 객체 형태로 담아서 보내는 것이 좋다.

    ```javascript
    // 부모 컴포넌트에서 전달
    import Child from "./Child";
    
    // 전달할 데이터
    const propData = {
      a : 1,
      b : 2,
      c : 3,
    }
    
    const App = () => {
      return (
        <div className="App">
        
        	// 데이터 이름을 지정하지 않고 spread 연산자를 통해 펼쳐서 전달
        	// <Child a:{a} b:{b} c:{c} /> 와 동일함
        	<Child {...propData} />
        
        </div>
      );
    };
    ```

    ```javascript
    // 자식 컴포넌트에서 받음
    
    // 마찬가지로 사용할 데이터만  { 전달 받은 데이터 이름 }와 같은 방법으로 꺼내서 사용한다.
    const Child = ({ a, b }) => {
    
      const propData = a;
    
      return (
        <div>
          <h3>{ b }</h3>
        </div>
      );
    };
    
    export default Child;
    ```

  

---

- **렌더링 되는 기준**
  - 본인 컴포넌트의 state가 변경될 때 마다 리렌더
  - 본인이 prop 받는 값이 변경될 때 마다 리렌더
  - 부모 컴포넌트가 리렌더 되면 자식 컴포넌트도 리렌더





