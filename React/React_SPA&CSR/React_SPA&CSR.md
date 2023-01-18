# SPA & CSR

- Routing
  - 어떤 네트워크 내에서 통신 데이터를 보낼 경로를 선택하는 일련의 과정
  - Router : 데이터의 경로를 실시간으로 지정해주는 역할을 하는 장치
  - Routing : 경로를 정해주는 행위 자체와 일련의 과정들을 모두 포함하는 말



- Page Routing
  - 브라우저가 /home 요청을 보내면 웹 서버는 Home.html 웹 문서를 제공한다.
  - MPA : multiple page application
    - MPA에서는 여러 HTML 페이지가 나뉘어져 있고 브라우저가 /home, /horse 처럼 다른 요청을 보내면 해당 요청에 대한 HTML 페이지로 응답한다. 
    - 이것이 해당 페이지로 라우팅하는 Page Routing
    - 다른 HTML를 요청하고 서버에서 새로운 HTML을 받아야 하기 때문에 새로고침 로딩이 걸린다.
    - SSR(server side rendering) : 서버에서 렌더링을 시행한다.
  - SPA : single page application
    - SPA는 단 한개의 HTML 페이지만으로 여러 요청에 대한 응답을 한다.
    - CSR(client side rendering) : 클라이언트 측에서 렌더링을 시행한다.
    - 데이터의 변화에 반응해야 하기 때문에 요청을 보내면 json파일로 응답하지만 CSR이기 때문에 라우팅을 다르게 해도 페이지 변환에 시간이 걸리지 않는다.
      - 서버와의 데이터 요청, 응답이 줄어들기 때문



- React : SPA & CSR