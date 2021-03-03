# React 

> 라이브러리 

### react 구조

- public 디렉토리

  - 기본적으로 정적 파일을 담는다. 웹 브라우저 상에 보이는 html 파일이나 img 등

- src 디렉토리

  - root 안에 들어가는 컴포넌트들은 어떤 파일을 열어야지 확인 할 수 있는지 알아보자

  - ### index. js

  ```javascript
  <script>
  import React from 'react';
  import ReactDOM from 'react-dom';
  import './index.css';
  import App from './App';
  import * as serviceWorker from './serviceWorker';
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
  serviceWorker.unregister();
  </script>
  ```

  1) 돔 선택자를 기반으로해서 컴포넌트들을 index.html 에 붙이겠다

  ```
  document.getElementById('root')
  ```

  2) React에서 만든 컴포넌트들 ===

  ```
  <React.StrictMode>
      <App />
  </React.StrictMode>,
  ```

  3) 컴포넌트 모음 가져오기

  ```
  import App from './App';
  ```
  - ### App.js

    - 이 모든 컴포넌트를 가져오는 App.js 는?

  ```javascript
  import logo from './logo.svg';
  import './App.css';
  
  function App() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {/* Edit <code>src/App.js</code> and save to reload. */}
            hello
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
  
  export default App;
  
  ```

  - 이 코드에서 index.js 에 있는 <App /> 사용자 정의태그 안에 들어가는 내용은 바로 App 클래스의 return 된 값들이다.