# API 사용

- **API 호출 및 사용법**

  ```react
  // 데이터를 불러오는 데에 시간이 걸리니 비동기 처리를 위한 async
  const getData = async () => {
    
    // API를 불러오는 메소드 fetch에 await를 설정해서 
    // 뒤에 나올 initData 함수가 먼저 실행되지 않고 동기적으로 실행되게 함
    const res = await fetch(
      "https://jsonplaceholder.typicode.com/comments"
    ).then((res) => res.json());
  	
    // 불러온 정보를 내가 사용하기 적절하게 가공
    const initData = res.slice(0, 20).map((it) => {
      return {
        author: it.email,
        content: it.body,
        emotion: Math.floor(Math.random() * 5) + 1,
        created_date: new Date().getTime(),
        id: dataId.current++,
      };
    });
  	
    // state에 정보를 저장
    setData(initData);
  };
  
  // 컴포넌트가 마운트 될 때 getData를 실행
  useEffect(() => {
    getData();
  }, []);
  ```
  
  
  
