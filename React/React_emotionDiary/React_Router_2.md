# Router_2

- REACT ROUTER V6
  - REACT에서  CSR 기반의 페이지 라우팅을 할 수 있게 해주는 라이브러리
  - 유용한 기능
    1. Path Variable : useParams
    2. Query String : useSearchParams
    3. Page Moving : useNavigate



- Path Variable

  - "/diary/1" 혹은 "/diary/2" 처럼 URL의 params를 사용하는 경우이다.

  - 처리 방법

    ```react
    //   path="/diary/:id" 처럼 콜론을 사용해 받는다.
    //   이러면 "/diary" 는 params를 필수적으로 받는다는 선언이어서
    //   "/diary" URL에 대한 처리가 필요하다 
    
    <Routes>
      <Route path="/diary/:id" element={<Diary />}></Route>
      <Route path="/diary" element={<Diary />}></Route>
    </Routes>
    ```

    ```react
    // useParams import
    import { useParams } from "react-router-dom";
    
    const Diary = () => {
      // URL의 Params 로 전달되는 값을 객체로 가져옴
      // 위에 "/diary/:id" 에서 params의 이름이 id이기 때문에 id로 받는다
      const { id } = useParams();
    
      return (
        <div>
          <h2>Diary</h2>
          <p>이곳은 일기 목록 페이지 입니다.</p>
        </div>
      );
    };
    
    export default Diary;
    ```

    

- Query String

  - "/edit?id=10&mode=dark" 처럼 URL에 정보를 담아 보낸 것을 사용

  - 처리 방법

    ```react
    // URL이 "/edit?id=10&mode=dark" 로 왔을 때
    // // 쿼리 스트링은 위에 ":id" 와 다르게 매핑되는 페이지가 없어도 그냥 화면을 보여줌
    
    // useSearchParams import
    import { useSearchParams } from "react-router-dom";
    
    const Edit = () => {
    	
      // searchParams	: 전달 받은 params가 저장되는 곳
      // setsearchParams : 쿼리를 새롭게 수정하는 곳, 새로운 화면으로 이동
      const [searchParams, setsearchParams] = useSearchParams();
    
      // 전달 받은 params를 searchParams에서 get을 통해 꺼내어 사용한다
      const id = searchParams.get("id");
      const mode = searchParams.get("mode");
    
      return (
        <div>
          <h2>Edit</h2>
          <p>이곳은 일기 수정 페이지 입니다.</p>
    
          {/*이 버튼을 클릭하면 "/edit?id=10&mode=dark" 에서 "/edit?who=ABC" 로 변경됨 */}
          <button onClick={() => setsearchParams({ who: "ABC" })} />
        </div>
      );
    };
    
    export default Edit;
    ```

    

- Page Moving

  - 강제로 페이지 이동시키기

  - 사용 방법

    ```react
    // useNavigate import
    import { useNavigate, useSearchParams } from "react-router-dom";
    
    const Edit = () => {
      
      const navigate = useNavigate();
    	
      const [searchParams, setsearchParams] = useSearchParams();
      const id = searchParams.get("id");
      const mode = searchParams.get("mode");
    
      return (
        <div>
          <h2>Edit</h2>
          <p>이곳은 일기 수정 페이지 입니다.</p>
          <button onClick={() => setsearchParams({ who: "ABC" })} />
        	
          {/* "/AAA" URL로 보내버리려면 navigate("AAA")로 사용 */}
    			<button
            onClick={() => {
              navigate("/home");
            }}
          >
            홈으로 가기
          </button>
          
          {/* 뒤로 가기 기능은 navigate(-1)로 처리 */}
          <button
            onClick={() => {
              navigate(-1);
            }}
          >
            뒤로 가기
          </button>
        
        </div>
      );
    };
    
    export default Edit;
    ```

    
