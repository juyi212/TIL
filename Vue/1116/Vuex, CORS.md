# Vuex

- Vuex는 Vue.js 애플리케이션에 대한 **상태 관리 패턴 + 라이브러리** 입니다. 
- 컴포넌트간의 데이터를 더 효율적으로 전달하고 관리하고자 데이터 통신을 한 곳에서 중앙집중식으로 관리함.



#### 상태관리 패턴

- state : 컴포넌트간 공유하는 data
- action : 사용자의 입력에 따라 실행하는 메소드(비동기적인 동작)
- mutation : state를 변경하는 메소드(동기적인 동작)





# DRF (Server) - Vue.js(Client)

- 서버
  - 서버는 클라이언트에게 네트워크를 통해 정보나 서비스를 제공하는 컴퓨터 시스템
  - 서버, 정보 제공
- 클라이언트
  - 그 서버가 맞는 서비스를 요청, 서버가 원하는 방식에 맞게 제공, 사용자에게 적절한 방식으로 표현
  - 정보 요청 & 표현 



# CORS

> Cross - Origin Resource Sharing 
>
> 교차 출처 자원 공유
>
> 다른 출처에서 온 리소스를 공유하는 행위 

- SOP (Same- Origin Policy) 동일 출처 정책
  - 같은 출처 에서만 자원을 공유 



### 11/16 수업 흐름

#### server

- 가상환경 만들기

  - ```
    python -m venv venv
    ```

  - ```
    가상환경 만들어졌는지 확인
    ```

- 장고 설치

  - ```
    pip install django
    ```

- 프로젝트 생성

  - ```
    django-admin startproject config .
    ```

- 앱 생성

  - ```
    python manage.py startapp todos
    ```

- 셋팅에서 기본 설정.

- urls.py 분리

- models.py

- makemigrations, migrate

- django - rest framework 설치

  - google에 검색 

- serailizers.py 만들기



### client

- vue create client

- vue add router

...



> 오늘 수업은 약간 빨라서 따라가기 힘들었지만, 이제 Front - back 을 연결할 수 있게 되어서 굉장히 뿌듯하였다. 더 복습하고 React 까지 공부할 수 있기를 !

