# 20201005 REST API

### API Server 

- 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

**결과적으로 프로그래밍을 통해 요청에 json을 응답하는 서버를 만들자**



### RESTful API

> 상태에 대한 정보들을 정의하는 약속
>
> 구조화를 시켜서 이해 

- REST : REpresentational State Transfer -> 자원과 주소의 지정 방법 
  - 웹 상에 존재하는 자료를 HTTP 위에서 전송하기 위한 인터페이스
  - 네트워크 아키텍처

- **REST 중심 규칙**

  - URI 는 정보의 자원을 표현해야 한다
  - 자원에 대한 어떠한 행위는 HTTP Method로 표현한다

- REST 구성(아키텍처: 디자인패턴)

  - **자원**(URI) : Uniform Resource Identifier (통합 자원 식별자)
    - URI 는 정보를 표현하는데 집중 (간략하고, 계층적으로 )

  - **행위**(HTTP Method) : 컨텐츠를 전송하기 위한 프로토콜 (규약)
    - HTTP 기본 속성
      - stateless : 상태 정보가 저장되지 않음
      - connectless : 서버 요청을 하고 응답을 한 이후에 연결은 끊어짐 
    - HTTP Method
      - GET : 데이터를 조회
      - POST : 데이터를 생성
        - *#API 서버에서는 POST 요청이 오면 값을 저장. 저장된 값을 다시 보내준다.*
      - PUT/PATCH : 서버로 보낸 데이터 저장/ 지정 리소스의 부분만을 수정
      - DELETE 
  - **표현**(Representations) 
    - JSON (JavaScript Object Notation) : javascript 객체 표기법 
      - 데이터 덩어리!!! (언어 독 립 적 : 변환이 쉽다)

- HTTP Method + 자원 (URL)  표현
  - ex) GET/articles/1/ 

**프로그래밍을 통해  요청에 RESTful 한 방식으로 JSON을 응답하는 서버를 만들자**



### Django REST Framework

- #### Serialization (직렬화)

  > translating (QuerySet, model, instance --> JSON) 번역을 해주는 과정 

  - 데이터 구조나 오브젝트 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성 할 수 있는 포맷으로 변화하는 과정
  - Django에서 Form 을 작성하는 것과 굉장히 유사(유효성 검사, DB 저장 등등..)

  
  
  



