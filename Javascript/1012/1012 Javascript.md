# 1012 Javascript

>브라우저 화면을 동적으로 만들기 위해서 쓴다! (브라우저 조작!)
>
>HTML + CSS (정적) + Javascript (동적)



### History of Browser & Javascript

- 1994년 네스케이프사의 브라우저가 표준 
- 정적인 html을 동적으로 표현하기 위한 언어 도입을 결정
- 1995년 브랜던 아이크 주도로 개발된 'Mocha'를 자체 브라우저에 도입
- 이후 livescript라는 이름을 거쳐 지금의 javascript로 변경 

- MS의 폭발적 성장, IE3에서 자체적인 JScirpt 를 지원, 호환성 문제로 크로스 브라우징 등의 이슈 발생
- 계속되는 파편화를 방지하고 모든 브라우저에서 동일하기 동작하기 위한 표준의 필요성 제기
- Chrome 등장 이후 여러 과정을 거쳐 자바스크립트의 고질적인 문제를 많이 해결한 ES6 등장!



1. 브라우저 전쟁
2. 파편화 & 표준화의 투쟁
   - 브라우저 전쟁의 여파로  Cross browsing lssue
   - 표준화 통합을 위한 노력 jQuery
   - Vanilla JavaScript ! 사용



## DOM 의 개념

> Document Object Model (문서 객체 모델)
>
> 웹 페이지 문서 구조를 표현함으로써 스크립트 및 프로그래밍 언어와 페이지를 연결한다. ( JS- HTML )
>
> DOM은 문서를 논리 트리로 표현 , 각 노드는 객체를 갖는다

- HTML, XML등과 같은  문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스

- 문서 구조 스타일 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현

  

## DOM 조작

- 화면으로 표시된 HTML을 조작어 가능

- **selector** 를 이용해서 조작을 한다 (단일 Node)

  - `querySelector(selector)`를 이용해서 id, class 태그를 선택해서 조작 가능 (id,class,복.선, tag 포함)
  - `getElementById(id)`는 수업시간에서는 사용하지 않을 예정.
    - live 속성때문
  - dir (선택된 엘리먼트를 가진 변수)
    - 사용할 수 있는 속성 정보를 볼 수 있다.
    - mdn 문서 (mdn  + 찾으려는 속성 정보)

- HTMLCollection (live)

  - document.getElementsByTagName(tagName)
  - document.getElementsByClassName(class)

- NodeList(non-live)

  - document.querySelectorAll(selector)

- **Manipulation**

  - innerText 

    - 텍스트

  - innerHTML

    - XSS 공격에 취약점이 있어서 사용시 주의

  - Node attribute

    - element.style.backgroundcolor
    - setAttribute(attributeName, value)
    - getAttribute(attributeName)

  - Document.createElement(tagName)

    - 특정 태그를 생성

  - ParentNode.appendChild(Node)

    - 마지막 자식 요소로 추가

  - ParentNode.removeChild(child Node)

    - 해당요소를 제거

    

- 정리

  1. 선택한다

  2. 변경한다

     



## EventListener

- ### Event

  > click, submit, keydown, mouseover...
  >
  > 브라우저에서 일어나는 일

  - **addEventListener**

    - 특정 이벤트가 벌어지면 특정 행동을 한다.
- ~하면 ~한다
    - `EventTarget. addEventListener( 이벤트type, listener(function) )`
- `preventDefault()` 
      - 기본 동작을 동작하지 않게 막을 수 있다.
    
    