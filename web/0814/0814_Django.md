# Django

> python web framework

- 장고 시작하기

  ```PYTHON
  django-admin startproject first web_bex
  ```

  - `first_webex`라는 이름으로 폴더가 생성.

    - 여기 안에는 `first_webex`라는 이름으로 폴더가 생성.
      - first-webex : 프로젝트 설정 파일들이 들어 있음.
      - manage.py : 장고 명렁어를 실행하기 위한 파일.

    

- 장고 프로젝트는 application의 집합체로 동작

  - 실제로 어떠한 역할을 해주는 친구가 바로 app.
  - 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음.
    - 어플리케이션 : 하나의 역할 및 기능 단위로 쪼개진 형태.
      - 회원 관리 / 글 작성, 수정, 글 삭제 / 데이터를 수집 분석 /.....
      - 어플리케이션을 이렇게 나니어야 한다 같은 기준은 없음.
      - 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.

- 어플리케이션 생성

  ```python
  python manage.py startapp 앱이름(복수형)
  ```

  - 해당 앱 이름으로 폴더가 생성됨. (앱 폴더)

  

- MTV(MVC 패턴)

  - Model : 장고에서는 model
  - View: 장고에서는 Template
  - Controller : 장고에서는 view

- 3 대장 : 우리가 가장 밀접하게 수정하여야 하는 파일 

  - urls.py
  - views.py
  - templates(html 을)

- urls.py 에서 해야할 일

  - path('url 패턴 /' , 실행 되어야 하는 views에 있는 함수, 해당 path의 별명)
    - 많이 놓치는 부분: url 패턴 뒤에 슬러쉬

- views.py에서 해야할 일

  - 함수를 정의 (첫번 째 인자로 request 필수 꼭 ! )
  - return 은 꼭 필요.
    - render: 주로 template와 함께 response 할 때 사용되는 함수.
  
- template 에서 해야할 일

  - 폴더 명은 반드시 `templates`인 것을 확인



![image-20200814094913078](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200814094913078.png)

* 데이터 흐름
  1. urls.py
  2. views.py
  3. templates

- Template Variable

  - render() 세번째 인자로 `{key : value}`와 같이 딕셔너리 형태로 넘겨 주면 Template 에서 key를 이용하여 value를 가져올 수 있다.

  ```
  context={'key' : value}
  return render(request,'index.html',context)
  ```

  ```
  {{key}} 이렇게 value를 보여줄 수 있다.
  ```

- Variable Routing (동적 라우팅)

  - url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

    주소요청 : `http:// ~~~/hello/문자열`

    urls.py

    ```
    path('hello/<str(타입): name(저장되는 변수명)>/')
    ```

    views.py

    ```
    def hello(request, name(저장되는 변수명)):
    	print(name)
    	context={
    	'name': name,
    	}
    	return render(request,'hello.html',context)
    ```

    template(hello.html)

    ```
    <body>
    이름은 : {{name}} # context의 key 값을 사용하면 value를 출력
    ```





## Django Template Language(DTL)

> django template system 에서 사용하는 built-in template system이다. 
>
> 조건 반복 치환 필터 변수 등의 기능을 제공.

- 로직을 표현 할 때는 : `{%  for %}`
- 

template 에서 사용하는 데이터는 view에서 보내주는 것이다. **주의**!!!





** intro- lotto 진행 **