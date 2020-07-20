# 7/20 python 첫수업

### - web application 배울 것임 

: python, html/css, django, database, javascript ---

프로그래밍 언어 - python

1. 저장 (변수/ 저장 )- 무엇을 어떻게 어디에
2. 제어 (조건 / 반복) 

codlab 을 이용해서 진행

**python doc - 파이썬 공식문서를 보는 것을 추천한다.**



# 1. 변수

dust = 60 (60이라는 숫자를 dust 안에 넣는다.)



### 1) 할당연산자

- 변수는 = 을 통해 할당된다.
- 해당 데이터 타입을 확인하기 위해서는 type()을 활용함.
- 해당 값의 메모리 주소를 확인하기 위해서는 id()를 활용함

**다른 값을 동시에 할당.**

```
a,b=2020,4

print(a)

print(b)
```

```
a, b =b,a    #값을 바꿀 수 있다.

print(a)

print(b)
```

### 2) 식별자

파이썬에서 식별자는 변수 함수 모듈 클래스 등을 식별하는데 사용되는 이름입니다.

- 아래의 예약어는 사용 못함.

\# 예약어들을 직접 확인해봅시다.

```
import keyword #외부에 있는 것 을 가져와서 쓸게.

print(keyword.kwlist) #예약어들 직접 확인.
```



# 2. 데이터 타입

### 1) 숫자타입

- int - 어떤 숫자든 호용이 가능하다. max * max 도 가능

- ```
  binary_number = 0b10 #2진수값으로 입력했지만 10진수 값으로 나옴 
  
  print(binary_number)
  
  octal_number =0o10 #8진수 
  
  print(octal_number)
  
  hexadecimal_number = 0x10 #16진수
  
  print(hexadecimal_number) 
  ```

  ```
  **실수의 연산 (중요하다..실수를 많이 할 수 있기 때문)**
  
  3.0 - 실수 연산
  
  round(3.5 - 3.2,2) # 소숫점 둘째자리에서 반올림.
  
  == 0.3 - true 나옴
  
  a = 3.5 -3.2
  
  b= 0.3
  a == b  false #주의 해야함.
  ```

  ```
  a= 3.5-3.12
  b=3.8
  
  abs(a-b)<= 1e-10 #작을때 같다라고 생각하고 true
   
  
  import sys
  
  print(sys.float_info.epsilon) #굉장히 작은 값.
  abs(a-b) <= sys.float_info.epsilon  ->true
  
  
  import math
  
  math.isclose(a,b) #값이 서로 가까이 있으면 TRUE
  ```

  ### 2) 문자타입

  ```
  number=input('숫자를 입력해주세요.') #문자로 인식
  
  print(int(number)* 2) #정수로 바꿔줌 
  ```

  ### 3) 이스케이프 시퀀스 

  ![image-20200720130551415](720 python 첫수업.assets/image-20200720130551415.png)

  

  ```
  > print('hello',end='\t') #\n 값은 기본으로 들어가있기때문에 end를 이용해서 조작해준다.
  
  > print('ssafy')
  ```

  

  ### 4 )string interpolation 중요하다

  - `%-formatting`
  - [`str.format()`](https://pyformat.info/)
  - **[`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원 !!!!!!!!**

  print('내 이름은 %s 입니다.' % name) #옛날 방법 

  print('내 이름은 {} 입니다.' .format(name))

  **print(f'내 이름은 {name} 입니다.') #이제 이것을 쓸 것임.  **

  - f string은 형식을 지정가능

    -f'올해는 {n:%Y}년 이번달은 {n:%m}월 오늘은{n:%d}일'

    ```
    import datetime
    
    n = datetime.datetime.now()
    print(n)
    
    
    
    pi=3.141592
    print(f'{pi:.3}') => 3.14 나옴
    
    r=10
    print(f'{pi:.3} 넓이는 : {pi*r*r :.3}')
    ```

    

  ### 5 ) 참/거짓 타입

  

