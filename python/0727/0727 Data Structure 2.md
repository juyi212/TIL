# 0727 Data Structure 2

> 알고리즘에 빈번히 활용되는 순서가 없는 데이터 구조 - set, dictionary

## set

> 변경 가능하고(mutable),순서가 없고, 순회 가능한(iterable), 중복 x

```
#집합 자체는 수정/추가 될 수 있지만 **포함된 요소는 immutable 해야 한다.**

set3={1.'a',(1,3)} -> list 들어가면 error 남

#index 넘버가 없다 . 순서가 없기때문, but 함수로 값을 추가할 수 있다.
```

- add -하나의 값만 추가
- update - (*others) 여러가지 값 추가 가능 ,iterable 데이터 구조만 가능

- remove -세트에서 삭제하고, 없으면 KeyError가 발생합니다.
- discard-세트에서 삭제하고 없어도 에러가 발생하지 않습니다.
- pop- 임의의 원소를 제거해 반환함,순서가 없기때문에 임의의 값임.



### dictionary

>변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
>
>`Key: Value` 페어(pair)의 자료구조

```
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

#value 만
for dic in my_dict.values():
    print(dic)

#key,value 동시에
for dic,value in my_dict.items():
    print(dic)
    print(value)

```

- **.get(key[,default])- key 값이 없으면 default 값인 none이 반환됨.**

  ```
  my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
  print(my_dict.get('pineapple'))
  print(my_dict.get('apple'))
  print(my_dict.get('pineapple', 0)) #default 값을 0로 설정한것임
  
  >>None
  사과
  0
  ```

- **.pop(key[,default])**

  - key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.
  - default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.
  - get과는 다르게 기본 default 값이 설정이 x,설정해주면 가능 

  ```
  my_dict = {'apple': '사과', 'banana': '바나나'}
  my_dict.pop('apple')
  print(my_dict)
  {'banana': '바나나'}
  ```

- .update (apple='애플') 이런거

  - 값 추가, 기존에 있는 값 수정 가능.
  - key 값이 int 일때는 my_dict[1]='one' 이런식으로 함. 근데 key에 숫자가 잘 안들어감.

- dictionary comprehension

  - ```python
    dict({키: 값 for 요소 in iterable})
    ```

  ```
  numbers=[1,2,3,4,5]
  cubic = {}
  for i in numbers:
      cubic[i]=i**2
  print(cubic)
  
  >>{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  
  ## 표현식
  
  dict({i:i**2 for i in numbers}) 
  
  num={i:i**2 for i in numbers}
  print(num)
  
  
  blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
  negative_blood_types = {'-'+i:blood_types[i] for i in blood_types}
  print(negative_blood_types)
  >>{'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
  
  ##조건식
  result = {dust:dusts[dust] for dust in dusts if dusts[dust]>80}
  print(result)
  >>{'대전': 82, '중국': 200}
  
  result = {dust:'나쁨' if dusts[dust]>80 else '보통' for dust in dusts}
  >> {'서울': '보통', '대전': '나쁨', '구미': '보통', '광주': '보통', '중국': '나쁨'}
  ```

  