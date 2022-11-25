# Vue

1.  Vue  CDN

   1.  Vue를 사용하기 위한 CDN

   2. ```html
        <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
      ```

2.  Vue 생성자 함수

   1.  new obj()

   2. ```html
        <script>
          const app = new Vue({
            el: '#app',
            data:{
              message: ''
            }
          })
        </script>
      ```

   3.  el: 

      1. View와 Model을 연결하는 역할

      2. HTML id 혹은 class와 연결(마운트)

      3. ```html
           <script>
            	el: '#id'
           </script>
         ```

   4. data:

      1. Vue instance에 data 객체 추가

      2. ```html
           <script>
             data:{
               message: 'bla bla'
             }
           </script>
         ```

      3. 추가된 객체는 {{}} interpolation을 통해 view에 렌더링 가능

      4. 추가된 객체의 각 값들은 this.message 처럼 접근 가능

   5. method:

      1. Vue instance의 method들을 정의하는 곳

      2. ```html
           <script>
             methods:{
               print: function () {
                 console.log(this.message)
               },
               bye: function () {
                 this.message = 'Bye, Vue!'
               }
             }
           </script>
         ```

      3.  vue instance 이름이 app이라면 app.print(), app.bye() 로 실행

3. 기본 문법

   1.  v-html

      1. HTML의 기본 속정이 아닌 Vue가 제공하는 특수 송성의 값으로 data를 작성

      2. ```html
         <div id="app">
           <div v-html="rawHTML"></div>
           <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
         </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data:{
                 rawHTML: '<span style="color:red">빨간 글씨 </span>'
               }
             })
           </script>
         ```

      3.  v-html 이 rawHTML 인 경우 적용됨

      4.  사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지

   2.  v-text

      1. {{ }} 와 동일한 역할

   3.  v-show & v-if

      1. boolean 값이 변경 될 때 마다 반응

      2. 작성된 값에 따라 element를 보여줄 것인지 결정

      3. ```html
           <div id="app3">
             <p v-show="isActive">보이니? 안보이니?</p>
             <p v-if="isActive">안보이니? 보이니?</p>
           </div>
         .
         .
         .
           <script>
             const app3 = new Vue({
               el: '#app3',
               data: {
                 isActive: false
               }
             })
           </script>
         ```

      4.  v-if 는 v-else-if / v-else 형태로 사용 가능

   4.  v-for

      1.  str

         1. ```html
              <div id="app">
                <h2>String</h2>
                <div v-for="(char, index) in myStr" :key="index">
                  <p>{{ index }}번째 문자열 {{ char }}</p>
                </div>
              </div>
            .
            .
            .
              <script>
                const app = new Vue({
                  el: '#app',
                  data: {
                    // 1. String
                    myStr: 'Hello, World!',
                  }
                })
              </script>
            ```

         2. ```html
            <div v-for="(char, index) in myStr" :key="index">
            ```

         3. 위와 같은 형식으로 사용

      2. array

         1. ```html
              <div id="app">
                <h2>Array</h2>
                <div v-for="(item, index) in myArr" :key="index">
                  <p>{{ index }}번째 아이템 {{ item }}</p>
                </div>
               
                <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
                  <p>{{ index.id }}번째 아이템</p>
               		  <p>{{ item.name }}</p>
                </div>
              </div>
            .
            .
            .
              <script>
                const app = new Vue({
                  el: '#app',
                  data: {
                    //2-1. Array
                    myArr: ['python', 'django', 'vue.js'],
            
                    //2-2. Array with Object
                    myArr2: [
                      { id: 1, name: 'python', completed: true},
                      { id: 2, name: 'django', completed: true},
                      { id: 3, name: 'vue.js', completed: false},
            	 	],
                  }
                })
              </script>
            ```

      3. object

         1. ```html
              <div id="app">
                <div v-for="(value, key) in myObj"  :key="key">
                  <p>{{ key }} : {{ value }}</p>
                </div>
              </div>
               
            <script>
                const app = new Vue({
                  el: '#app',
                  data: {
                    // 3. Object
                    myObj: {
                   	  name: 'harry',
                      age: 27
                    },
                  }
                })
              </script>
            ```

      4. key 값은 고유한 녀석으로 설정해서 입력해줘야 함

   5.  v-on

      1. ```html
           <div id="app">
             <button v-on:click="number++">increase Number</button>
             <p>{{ number }}</p>
           </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data: {
                 number: 0,
               },
             })
           </script>
         ```

      2.  addEventListener 와 같은 역할

      3.  위 예시는 클릭을 하면 숫자가 1씩 커지는 코드

      4. '@' shortcut

         1. @click 은 v-on:click 과 같음, shortcut을 제공

   6. v-bind

      1. HTML 기본 속성에 Vue data를 연결

      2. class의 경우 다양한 형태로 연결 가능

         1. 조건부 바인딩

            1. {'class name' : '조건 표현식'}

            2. ```html
               <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
               ```

         2. 다중 바인딩

            1. ['JS 표현식', 'JS표현식', ...]

            2. ```html
               <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>
               ```

      3. ':' shortcut

         1. :class 는 v-bind:class 와 같음, shortcut을 제공

   7. v-model

      1. Vue instance와 DOM의 양방향 바인딩

      2. Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

      3. ```html
           <div id="app">
             <h2>1. Input -> Data</h2>
             <h3>{{ myMessage }}</h3>
             <input @input="onInputChange" type="text">
             <hr>
           </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data: {
                 myMessage: '',
               },
               methods: {
                 onInputChange: function (event) {
                   this.myMessage = event.target.value
                 },
               }
             })
           </script>
         ```

      4. ```html
           <div id="app">
             <h2>2. Input <-> Data</h2>
             <h3>{{ myMessage2 }}</h3>
             <input v-model="myMessage2" type="text">
             <hr>
           </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data: {
                 myMessage2: '',
               },
             })
           </script>
         ```

      5. 위의 코드는 이벤트를 듣고 그것을 method를 통해 반영

      6. 아래의 코드는 양방향 바인딩으로 method 없이 가능

      7. 다만 아래의 코드는 한글 반영이 늦고 위의 코드는 한글 반영이 바로 됨

      8. 따라서 한글의 경우 우리는 위의 코드를 쓰는 것이 좋음

4.  Vue advance

   1. computed & method

      1. ```html
           <div id="app">
             <h1>data_01 : {{ number1 }}</h1>
             <h1>data_02 : {{ number2 }}</h1>
             <hr>
             <h1>add_method : {{ add_method() }}</h1>
             <h1>add_method : {{ add_method() }}</h1>
             <h1>add_method : {{ add_method() }}</h1>
             <hr>
             <h1>add_computed : {{ add_computed }}</h1>
             <h1>add_computed : {{ add_computed }}</h1>
             <h1>add_computed : {{ add_computed }}</h1>
             <hr>
             <button v-on:click="dataChange">Change Data</button>
           </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data: {
                 number1: 100,
                 number2: 100
               },
               computed: {
                 add_computed: function () {
                   console.log('computed 실행됨!')
                   return this.number1 + this.number2
                 }
               },
               methods: {
                 add_method: function () {
                   console.log('method 실행됨!')
                   return this.number1 + this.number2
                 },
                 dataChange: function () {
                   this.number1 = 200
                   this.number2 = 300
                 }
               }
             })
           </script>
         ```

      2.  위의 코드를 console에서 확인해보면

      3.  method

         1. 호출될 때마다 함수를 실행
         2. 같은 결과여도 매번 계산

      4. computed

         1. 함수의 종속 대상의 변화가 있을 때만 계산

         2. 변화가 없으면 저장된 값을 반환

         3. ```html
            <h1>add_method : {{ add_method() }}</h1>
            <h1>add_computed : {{ add_computed }}</h1>
            ```

         4. 그래서 method는 method() 이고 computed는 괄호가 없는 computed

   2. filters

      1. {{}} 이나 v-bind 를 이용할 때 사용 가능

      2. 자바스크립트 표현식 마지막에 '|'(파이프) 와 함께 추가, 이어서 사용 가능 

      3. ```html
           <div id="app">
             <p>{{ numbers }}</p>
           </div>
         .
         .
         .
           <script>
             const app = new Vue({
               el: '#app',
               data: {
                 numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
               },
               filters: {
                 getOddNums: function (nums) {
                   const oddNums = nums.filter((num) => {
                     return num % 2
                   })
                   return oddNums
                 },
               }
             })
           </script>
         ```

      4. 위 예시는 numbers의 홀수만 출력하는 예시