# 0820 

> 0819 복습 및 새로운 내용 추가

lab.ssafy.com/dy/crud - clone 해놓기

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

--------------

# CRUD

### READ

- DB에 전체 글 목록을 가져와서 page에 보여주자
- Article.objects.all() 의 queryset을 그대로 context에 담아서 template파일에 전달
- template 은 for문으로 하나씩 db 값을 접근가능하고 연산자를 이용해서 값에 접근가능.

```python
#view.py
def index(request):
    articles = Article.objects.all()
    #queryset 형태는 list와 비슷
    context={
        'articles':articles
    }

    return render(request,'articles/index.html',context)
```

```python
{% extends 'base.html' %}
{% block content %}
<h1>index page</h1>
<!-- read의 전체 목록 불러오기, 쿼리셋에 있는 내용들을 불러냄 -->
{% for article in articles %} 
    <br>    
    <p>글 제목 :{{article.title}}</p>
    <p>내용 :{{article.content}}</p>
    <p>생성일 :{{article.created_at}}</p>
    <p>수정일 :{{article.updated_at}}</p>
    <br>
{% endfor %}
{% endblock %}
```

### CREATE

- form 태그에서 데이터를 전달하고 
- 그 데이터를 3가지 저장 방법 중 1개의 방법으로 DB에 저장하면 끝
- GET / POST
  - GET :  주소줄에 쿼리 스트링 형식으로 데이터가 전달. 전달하는 길이가 한계가 있음(255자)
    - 주로 데이터 정보를 가져 올 때 사용 (즉, 데이터를 조회할 때 이용 )
  - POST : 패킷 바디 안에 데이터가 전달. 좀 더 많은 양의 데이터를 전달 할 수 있음.
    - 주로 데이터의 정보를 생성, 수정, 삭제 할 때 사용.
  - GET / article / : article의 정보를 조회
  - POST/article/ : article 을 생성
  - POST/article/1 : article을 수정
  - REST API : 나중에 수업할 예정인 내용.
- method를 POST로 변경 할 때 해야할 일
  - CSRF : (Cross-site request forgery) 사이트 간 요청 위조 
  - CSRF를 Form tag  사이에 {% csrf_token %} 넣어줘야함
  - request.GET을 request.POST로 변경
-  return redirect('articles:index')  # 바로 index 페이지로 넘어가도록 함.

```python

def create(request):
    return render(request,'articles/create.html')


def new(request):
    # print(request.GET.get('title'))
    # print(request.GET.get('content')) #딕셔너리 형태라서 get 이용

    #1번 방법
    # article = Article()
    # article.title = request.GET.get('title') #주소줄에 나타난 값을 request로 받아서 변수에 담아줌.
    # article.content = request.GET.get('content')
    # article.save() #데이터 베이스에 저장

    #2번 방법
    # title= request.GET.get('title')
    # content=request.GET.get('content')
    # article=Article(title=title,content=content)
    # article.save()

    #3번 방법
    title=request.GET.get('title')
    content=request.GET.get('content')

    Article.objects.create(title=title,content=content)
    return render(request,'articles/new.html')
```



```python
#create.html
{% extends 'base.html' %}
{% block content %}
<form action="{% url 'articles:new' %}" method="GET">
    Title: <input type="text" name='title'>
    <br>
    Content : <Textarea name='content'></Textarea>
    <br>
    <button>제출</button>
</form>
{% endblock%}
```



### UPDATE

- 글 제목을 클릭 했을 때 해당 글만 보이는 페이지 만들기
- detail 페이지를 먼저 만들자!
  - 어떠한 글의 detail 페이지인지 해당 글의 정보 pk가 필요함
  - 글의 정보를 동적 라우팅 방법으로 주소로 전달
  - 주소로 전달 받은 글의 pk 값을 가지고 DB에서 데이터를 가져옴
  - 가져온 데이터를 template 파일에서 보여주면 그것이 detail page !
- detail 페이지 하단에 수정하기 링크를 만들어 준다.
  - 수정하기 링크는 edit하는 페이지를 보여준다.
  - create 방법과 유사하게 form을 보여주는데 
  - 차이점은 해당 글의 data를 같이 넘겨주고 그 데이터를 같이 보여주는게 차이점.
  - 수정하기 최종 버튼을 눌렀으면 post 방식으로 DB에 적용을 시켜주면 끝
  - 이 때 필요한 정보pk도 주소 줄을 이용해서 전달한다.
- DB에 적용시키는 방법
  - 해당 pk를 가지는 데이터를 불러오고 값을 수정하고 save 해준다
- 끝나면 detail page로 redirect 시키면 끝.



### DELETE

