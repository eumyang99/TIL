# List 사용하기

- ComponentA -> ComponentList -> ComponentItem 컴포넌트 구조를 상정

  - ComponentA

  ```javascript
  import ComponentList from "./ComponentList";
  
  const ComponentA = () => {
    
    // 더미 리스트 생성
    const dummyList = [
      {
        id: 1,
        a: "a1",
        b: "b1",
        c: "c1",
      },
      {
        id: 2,
        a: "a2",
        b: "b2",
        c: "c2",
      },
      {
        id: 3,
        a: "a3",
        b: "b3",
        c: "c3",
      },
      {
        id: 4,
        a: "a4",
        b: "b4",
        c: "c4",
      },
    ];
  
    return (
      <div>
      	
      	// 자식 컴포넌트한테 리스트 prop
        <ComponentList dummyList={dummyList} />
      </div>
    );
  };
  
  export default componentA;
  ```

  - ComponentB

  ```javascript
  import ComponentItem from "./ComponentItem";
  
  // 리스트를 prop 받고
  const ComponentList = ({ dummyList }) => {
    return (
      <div>
      
      	// map 메소드를 사용하여 자식 컴포넌트에 하나씩 prop
      	// 리스트 각각의 자식 요소들은 고유 key값을 가져야 하기 때문에 고유한 key값 전달
        {dummyList.map((it) => (
          <ComponentItem key={it.id} {...it} />
        ))}
      </div>
    );
  };
  
  // 만약 부모 컴포넌트에서 해당 리스트를 정의하지 못하고 undefined를 전달하면
  // 리스트 구조에 맞게 짜여진 자식 컴포넌트들에서 에러가 발생할 수 있다.
  // 따라서 이러한 경우 prop 받는 데이터의 디폴트값을 미리 설정할 수 있다.
  ComponentList.defaultProps = {
    dummyList: [],
  };
  
  export default ComponentList;
  ```

  - ComponentC

  ```javascript
  // 사용
  
  const ComponentItem = ({ id, a, b, c }) => {
    return (
      <div>
        <span>{id}</span>
        <span>{a}</span>
        <span>{b}</span>
        <span>{c}</span>
      </div>
    );
  };
  
  export default ComponentItem;
  ```

  



