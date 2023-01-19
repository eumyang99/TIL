# Router_1

- 설치

  ```react
  // 프로젝트 폴더에서 설치
  // @6는 react router의 6버전을 설치해달라는 명령어
  
  npm install react-router-dom@6
  
  // 이후 package.json dependency에서 설치 및 버전 확인
  ```

- 컴포넌트 제작

  - src 폴더에 pages 폴더를 생성 후 그 안에 생성

    - Home, New, Edit, Diary 컴포넌트

    ```react
    // src/pages/Home.js
    const Home = () => {
      return (
        <div>
          <h2>Home</h2>
          <p>이곳은 홈 입니다.</p>
        </div>
      );
    };
    
    export default Home;
    
    ```

    ```react
    // src/pages/New.js
    const New = () => {
      return (
        <div>
          <h2>New</h2>
          <p>이곳은 일기 작성 페이지 입니다.</p>
        </div>
      );
    };
    
    export default New;
    ```

    ```react
    // src/pages/Edit.js
    const Edit = () => {
      return (
        <div>
          <h2>Edit</h2>
          <p>이곳은 일기 수정 페이지 입니다.</p>
        </div>
      );
    };
    
    export default Edit;
    ```

    ```react
    // src/pages/Diary.js
    const Diary = () => {
      return (
        <div>
          <h2>Diary</h2>
          <p>이곳은 일기 목록 페이지 입니다.</p>
        </div>
      );
    };
    
    export default Diary; 
    ```

- React-router-dom을 이용해서 위 네 페이지를 특정 주소에 연결해서 페이지 라우팅하기

  - browserRouter :Browser URL 과 React APP을 연결하는 컴포넌트

  - Routes : Browser URL 이 변경되면 어떤 컴포넌트를 렌더링해서 그 컴포넌트가 페이지 역할을 하게 하는지 결정하는 컴포넌트

  - Route : Browser URL 경로와 각 컴포넌트를 매핑 시켜주는 컴포넌트

    ```react
    import "./App.css";
    
    // 1. BrowserRouter import
    // 4. Routes import
    // 6. Route import
    import { BrowserRouter, Routes, Route } from "react-router-dom";
    
    // 10. RouteTest import;
    import RouteTest from "./components/RouteTest";
    
    
    // 3. pages 컴포넌트들 import 
    import Home from "./pages/Home";
    import New from "./pages/New";
    import Edit from "./pages/Edit";
    import Diary from "./pages/Diary";
    
    function App() {
      function App() {
        return (
          // 2. BrowserRouter 컴포넌트로 return 부분을 감싼다
          // 감싸져 있는 부분은 Browser URL 과 매핑될 수 있다
          <BrowserRouter>
            <div className="App">
              <h2>App.js</h2>
              {/* 5. 화면에서 바뀔 부분을 Routes로 감싼다 */}
              <Routes>
                {/* 7. url 경로에 해당하는 컴포넌트를 작성   */}
                <Route path="/" element={<Home />} />
                <Route path="/new" element={<New />} />
                <Route path="/edit" element={<Edit />} />
                <Route path="/diary" element={<Diary />} />
              </Routes>
              
              {/* 11. RouteTest 작성 : 링크 이동 버튼 */}
              </RouteTest>
            </div>
          </BrowserRouter>
        );
      }
      
      export default App;
    ```

  - CSR 방식으로 각 컴포넌트로 이동하는 버튼 만들기

    - src 폴더에 components 폴더를 생성 후 그 안에 생성

    - ```react
      // Link 구조
      <Link to={"/경로"}>HOME</Link>
      ```

    ```react
    // src/pages/RouteTest.js
    
    // 8. Link import
    import { Link } from "react-router-dom";
    
    // 9. RouteTest 컴포넌트 안의 자식 컴포넌트로 Link 컴포넌트들 작성
    const RouteTest = () => {
      return (
        <>
          <Link to={"/"}>HOME</Link>
          <br />
          <Link to={"/diary"}>DIARY</Link>
          <br />
          <Link to={"/new"}>NEW</Link>
          <br />
          <Link to={"/edit"}>EDIT</Link>
          <br />
        </>
      );
    };
    
    export default RouteTest;
    
    ```

    