# useRef

- **HTML DOM 요소를 선택하여 접근할 수 있는 기능**

- ```javascript
  // React에서 import 해서 사용
  import {useRef} form "React"
  ```

- **예시**

  - 주석의 순서대로 사용

  - ```javascript
    const DiaryEditor = ({ onCreate }) => {
      // 1. useRef함수의 반환값을 상수에 담음
      const authorInput = useRef();
      const contentInput = useRef();
    
      const handleSubmit = () => {
        if (state.author.length < 1) {
          // 3. useRef의 currunt메소드를 사용하여 불러와서 사용
          // authorInput.current 는 연결된 태그를 의미
          authorInput.current.focus();
          return;
        }
    
        if (state.content.length < 5) {
          contentInput.current.focus();
          return;
        }
        onCreate(state.author, state.content, state.emotion);
        alert("저장 성공!");
        setState({
          author: "",
          content: "",
          emotion: 1,
        });
      };
    
      return (
        <div className="DiaryEditor">
          <h2>오늘의 일기</h2>
          <div>
            <input
              // 2. authorInput을 해당 태그에 달아서 태그와 상수를 연결
              ref={authorInput}
              name="author"
              value={state.author}
              onChange={handleChangeState}
            />
    
            <div>
              <button onClick={handleSubmit}>일기 저장하기</button>
            </div>
          </div>
        </div>
      );
    };
    
    export default React.memo(DiaryEditor);
    ```

    

