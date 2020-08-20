# 0819 Django Model

### Model

- 데이터에 대한 단 하나의 정보 소스

- 저장된 데이터베이스의 구조를 의미

- django는 model을 통해 데이터를 접속하고 관리한다

- 일반적으로 각각의 모델은 하나의 데이터 베이스 테이블에 매핑

  

#### datadase 

- 체계화된 데이터의 모임
  - database의 기본 구조
    - 스키마 Schema
      - 데이터 베이스의 구조와 제약 조건에 관련한 전반적인 명세를 기술한 것.
      - 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조 
    - 테이블 table 
      - 열(필드)과 행(레코드)의 모델을 사용해 조작된 데이터 요소들의 집합 
      - SQL 데이터베이스에서는 테이블을 관계라고도 한다.
    - 기본키 PK
      - 반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.

#### 쿼리 query

- 데이터를 조회하기 위한 명령어
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어

#### ORM

- 객체지향 프로그래밍 
- 장점 : SQL 을 잘 알지 못해도 DB 조작이 가능, SQL의 절차적 접근이 아닌 객체지향적 접근으로 인한 높은 생산성
- 단점 : ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있다. 
- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것이다. **생산성!!!!**



- 우리는 DB를 객체(Object)로 조작하기 위해 ORM을 사용한다.



### Model 안의 Class 속성

-------------------

`models.py`에 모델 클래스를 정의를 해서 사용 할 수 있음.

- class 테이블명(models.Model):

  title=models.CharField(max_length=100)

### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max length가 필 수 인자
- 필드의 최대 길이, 데이터베이스와 django의 유효성 검사(이 데이터가 올바른 데이터인지, 이 문자의 길이가 10자를 넘는지 안넘는지 )

### TextField()

- 글자의 수가 많을 때 사용 

### DateTimeField()

- 최초 생성 일자 :auto_now_add = True

  - auto-now는 생성될때마다 일자 변경

  - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
  - 테이블에 어떤 데이터를 최초로 넣을 때

- 최초 수정 일자 : auto_now=True

  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



## Migrations

- django가 model에 생긴 변화(필드를 추가했다던가 모델을 삭제했다던가 등 )을 반영하는 방법
- 마이그레이션 실행 및 DB스키마를 다루기 위한 몇가지 명령어
  - **makemigrations**
    - python manage.py makemigrations [app 이름]
    
    - model을 변경한 것에 기반한 새로운 마이그레이션(설계도라고 생각하자)을 만들 때 사용 
    - 모델을 활성화 하기 전에 DB 설계도를 작성
    - 생성된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전 관리 시스템이라고 생각.
    
  - **migrate**
    - python manage.py migrate [app 이름]
    
    - 작성된 마이그레이션 파일을 기반으로 실제 DB에 반영하기 위해 사용 (이 명령을 해야 테이블을 생성함.)
    - db.sqlite3 라는 데이터베이스 파일에 테이블을 생성 
    - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
    
  - sqlmigrate
    - 해당 마이그레이션 파일이  SQL 문으로 어떻게 해석되어서 동작할지 미리 확인하기 위해 사용
    - ex) python manage.py sqlmigrate articles 0001
    
  - showmigrations
    
    - 마이그레이션 파일들의 migrate 여부를 확인하기 위한 명령어



## Model의 중요 3단계

1. models.py : 변경사항(작성,수정,삭제...) 발생
2. makemigrations : 마이그레이션 (설계도) 만들기 
3. migrate : DB에 적용 



## Database API

- django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도와줌(Create, Read, Update, Delete - 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인)
- 모델을 만들면 django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API

![image-20200819112455789](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200819112455789.png)

- Manager
  - django 모델에 데이터베이스 query작업이 제공되는 인터페이스
  - 기본적으로 모든 django 모델 클래스에 objects라는 manager를 추가
- QuerySet
  - 데이터베이스로부터 전달받은 객체 목록
  - queryset 안의 객체는 0개,1개 혹은 여러 개 일 수 있음
  - 데이터베이스로부터 조회,필터,정렬 등을 수행 할 수 있음.



#### CREATE

데이터를 작성하는 3가지 방법

1.

```html
article = Article() # 1. 인스턴스 생성
article # 2. 인스턴스로 클래스 변수 접근
<Article: Article object (None)>

article.title = 'first' #인스턴스 변수를 변경
article.content='django!'
article.save() #3. 반드시 저장해줘야함.
    
```

2. 클래스로 인스턴스 생성 시 keyword 인자를 함께 작성
   - article = Article(title='second',content='django!')
   - article.save()

3. create() 메서드를 사용하면 쿼리셋 객체를 생성하고 save하는 로직이 한 번에 가능
   - Article.objects.create(title='third',content='django!')



#### READ

`all()`

- `QuerySet` return
- 리스트는 아니지만 리스트와 거의 비슷하게 동작 (조작할 수 있음)

```
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
get()
```

`get()`

- 객체가 없으면 `DoesNotExist`에러가 발생

- 객체가 여러개일 경우는 `MultipleObjectReturned`에러가 발생

- 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있으면 사용할 수 있다.

- pk를 조회할때 사용한다.

  ```
  article=Article.objects.get(pk=1)
  ```

`filter()`

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 QuerySet을 return 
- 복수의 값도 리턴해줌

```
>>> Article.objects.filter(content='django!')
<QuerySet [<Article: first>, <Article: fourth>]>

>>> Article.objects.filter(title='first')
<QuerySet [<Article: first>]>
```



#### UPDATE

1. 몇번 글 수정? -> .get() 으로 조회
2. 인스턴스 변수 값을 바꾸고
3.  save까지 해줘야함 갱신! (updated_at 도 바뀌게 됨.)

```python
# UPDATE articles SET title='byebye' WHERE id=1;
>>> article = Article.objects.get(pk=1)
>>> article.title
'first'

# 값을 변경하고 저장
>>> article.title = 'byebye'
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'byebye'
```

#### DELETE

- article 인스턴스 생성후 `.delete()` 메서드 호출



--------------------------

# Field lookups

- 구글링 키워드 : django queryset

- 필드명_필드룩업

- exact : 대소문자 전부 일치해야 함.

- iexact :  대소문자는 상관없이 일치하면 됨.

- contains : 해당 글자가 어느 위치 던지 포함되어 있으면 됨.

- startwith : 해당 글자로 시작하는 것만 

- endwith :  해당 글자로 끝나는 것만 

- gt / gte / lt / lte (비교 연산자)

  ```
  https://docs.djangoproject.com/en/3.1/ref/models/querysets/#id4
  ```

  

### 실습

- 제목이 first이고 한개만 가져와라. (여러개의 데이터가 있는데 하나만 가져오고 싶을 때)

```python
Article.objects.filter(title='second').first()
```

해당 모델 클래스로 값이 리턴



- 정렬을 하고 싶을 때 (오름, 내림)

  ```
  # 오름차순 
  Article.objects.order_by('title')
  
  # 내림차순
  Article.objects.order_by('-title')
  ```

- Queryset으로 리턴을 받았을 때

  - Queryset 은  list와 유사함
  - indexing & slicing 

  ```python
  Article.objects.all()[2]
  <Article: third>
      
  # -1 은 지원하지 않음.
  
  Article.objects.all()[:2]
  <QuerySet [<Article: first_number>, <Article: second>]>
  ```

  

------------------------

# Template 확장 사용하기

1. base.html 을 생성하고 원하는 위치에 templates폴더 안에 위치 시킨다.
   - base.html 에는 기본 html DOM트리를 구성
   - bootstrap CDN을 복붙해준다. (JS,..)
   - block을 body 안에 적절한 곳에 위치시킨다.
2. setting.py 에 base.html의 경로를 등록한다.
   - TEMPLATES 라는 곳에 있는 DIRS에 그 경로를 추가한다.
   - base.html 이 있는 경로를 BASE_DIR로 부터 설정해 주면 됨.
   - `'DIRS': [BASE_DIR/'workshop_sol'/'templates'],`
3. 확장하고 사용한다.
   - 가장 첫번째 줄에 {% extends `base.html`%}
   - 그 다음 block 을 위치 시키고 block 안에 적절히 꾸며주면 됨.



---------------

**0819_ws check list**

- 링크 태그

  ```python
  <a class="nav-link" href="{% url 'pages:community'%}">community</a>
  
  # url 분리 후 url namespace로 만들어줌.
  ```

  

