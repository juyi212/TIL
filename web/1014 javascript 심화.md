## AJAX 

> Asynchronous JavaScript And XML
>
> 서버와 통신하기 위해서 XMLHttpRequest 객체를 사용하는 것
>
> 페이지 전체를 리프레쉬(reload)하지 않고서도 수행되는 "비동기성"이다.
>
> 사용자의 Event 가 있으면 전체 페이지가 아닌 일부분만 업데이트 할 수 있음

- XHR (XML Http Request)

  - 서버와 상호작용하기 위해 사용
  - 전체 페이지의 새로고침 없이도 URL로 부터 데이터를 받아올 수 있다.
  - 사용자가 하고 있는 것을 방해하지 않으면서 페이지의 일부를 업데이트 가능
  - AJAX 프로그래밍에서 주로 사용한다

- Asynchronous (비동기)

  - 기다려주지 않는다!

- Single Thread

  - 혼자서 일하기 때문 

- Event Loop

  - event loop 매커니즘으로 일을 한다.

  - Call Stack : 함수 호출을 기록하는 곳
  - Web API  : 브라우저 영역에서 제공하는 API
  - Task Queue : 콜백 함수가 대기하는 queue 형태의 자료 구조
  - Event Loop : call stack에 실행 중인 task가 없는지 확인하고 task queue에 task가 있는지 확인

- Callback Function 
  - 비동기적인 것을 callback 함수를 통해 해결

### Promise(약속)

- sync (동기)
- async (비동기)
- callback function -> callback hell 을 방지하기 위해~ 벗 chaining 으로 또 복잡해질 수 있긴함.
- **promise 객체는 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타낸다**



### async & await (ES8 + )

- syntactic sugar  
- 체이닝의 복잡성을 해결해주고 + 동기적으로 보이게 하기 위함 !



## Axios 

> Promise based HTTP client for the browser and node.js
>
> 편하게 직관적으로 요청을 보내자 (promise를 기반으로 .then, .catch )





-------------------------

### 참고

- JSON placeholder : REST API 테스트를 위한 더미 데이터를 받을 수 있음