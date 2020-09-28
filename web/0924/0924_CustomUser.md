## 0924

## Custom User

- 준비 (클래스 정의/ settings.py 에 등록)

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class User(AbstractUser):
	pass
```

- AbstractUser

```
# settings.py 
# 다른 앱에서 끌어쓸 수 있도록 만들어 놓음.(articles/models.py 에서 끌어다가 씀)

AUTH_USER_MODEL = 'accounts.User'
```

- 기존 DB 삭제
- makemigrations
- migrate

## Custom User 를 했을 시 수정되어야하는 Form

- user을 모델로 하는 모델폼들을 수정해야 함.
- 제공되는 user관련 모델폼은 auth.User(django에서 제공해주는 User 클래스)를 model 정보로 가지고 있기때문.
- UserCreationForm / UserChangeForm 

```python
# accounts/forms.py
from django.contrib.auth.forms import UserChangForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model=get_user_model()
		fields=UserCreationForm.Meta.fields + ('email,')
```

- get_user_model()

  - return 유저 클래스
  - models.py 제외한 모든 곳

- settings AUTH_USER_MODEL

  - return 유저 클래스 문자열 (str)

  - models.py 에서만 사용 

-----------------

User- Article(1:N)

User- Comment(1:N)

```
# articles/models.py

class Article / class Comment
	....
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)(N에 해당하는 부분에 외래키 정의)
```

