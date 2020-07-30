# 0729 모듈 Module

> 파일 단위의 코드 재사용
>
> 모듈(module)은 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)입니다.

![image-20200729094113977](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20200729094113977.png)



- 모듈 생성 후 실행 

  ```
  import check
  check.odd(n)
  
  ```

  ```python
  import module
  from module import var, function, Class
  from module import *
  ```



# Package

>패키지(pakcage)는 **점(`.`)으로 구분된 모듈 이름(`package.module`)** 을 써서 모듈을 구조화하는 방법입니다.



```python
from package import module
모듈. 변수
모듈.함수
모듈.클래스

from package.module import var, function, Class

from my_package.math.tools(패키지.모듈/ 모듈) import * #해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져옵니다.
변수 
함수
클래스
from my_package.statistics.tools import standard_deviation as sd #함수를 sd 지칭
```



**모듈 찾는 위치**

1. 실행하는 파일을 기준으로 찾고
2. 파이썬에서 제공하는 것들 중에서 찾고
3. 외부 라이브러리 설치된 모듈을 찾는다. (pip에서 관리하는 path)

pip에서 패키지가 설치 되었는지 확인하는 방법 pip list



----

## 정리

- 모듈: 특정 기능을 하는 변수, 함수 , 클래스 코드를 .py나 스크립트 단위로 작성
- 패키지: 특정 기능과 관련된 여러 모듈의 집합. 패키지는 또 다른 서브 패키지를 가질 수 있음.
- 라이브러리: 모듈과 패키지들의 집합(파이썬 표준 라이브러리 PSL)
- 패키지관리자: 외부 패키지를 설치 할 수 있게 도와주는 패키지(pip)

### 모듈의 활용

- import를 통해서 모듈을 이름 공간으로 가져와야 한다.

- import 모듈명

- from 모듈명 import 변수 함수 클래스

- from 모듈명 import *

  

### 패키지의 활용

- 점(.)으로 구분된 모듈 이름(패키지명,모듈명)을 써서 모듈을 구조화하는 방법
- from 패키지명 import 모듈명
  - 모듈명.변수명, 모듈명.함수명, 모듈명.클래스명
- from 패키지명 import 모듈명 as 별명
  - 별명.변수명, 별명.함수명, 별명. 클래스명
- from 패키지명.모둘명 import 변수명, 함수명, 클래스명
  - 변수명 함수명 클래스명
- from 패키지명.모듈명 import *

```python
import datatime
print(datetime.datetime.now()) #datetime 모듈안의 datetime클래스 안 now라는 메서드사용

from datetime import datetime
print(datetime.now()) 
```



