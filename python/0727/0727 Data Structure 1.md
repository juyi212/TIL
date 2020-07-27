# 0727 Data Structure 1

> 데이터 구조란 **데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법**
>
> program= data structure + algorithm

- 알고리즘에 빈번히 활용되는 순서가 있는 데이터 구조
  - str, list

### 문자열(string)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

- 조희/탐색 - .find()

  ```
  'apple'.find('p') 
  >> 1
  
  'apple'.find('f')
  >> -1 #없는 경우에는 
  ```

- .index() 

  ```
  'apple'.index('k')
  >> error
  없으면, 오류가 발생합니다. # find 와 찾는것이 없을때 return 값이 다름.
  ```

- 값 변경- .replace(old,new[,count])

  ```
  'yay!'.replace('a', '_')
  >>'y_y!'
  ```

- .strip([chars]) 

  - 알고리즘 문제때 유용하게 쓰인다. 확인하자

  - 특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip).

    지정하지 않으면 공백을 제거합니다.

  ```
  '    oh!\n'.strip()
  >> 'oh!'
  '    oh!\n   '.lstrip()
  'hehehihihihihi'.rstrip('hi')
  ```

- .split()

  - 문자열을 특정한 단위로 나누어 리스트로 반환

  ```
  'a_b_c'.split('_')
  >> ['a', 'b', 'c']
  
  inputs = input().split()
  print(inputs)
  >>a b c d s 
  ['a', 'b', 'c', 'd', 's']
  
  ```

- 'separator',.join(iterable)

  - 반복가능한(iterable) 컨테이너의 요소들을 separator를 구분자로 합쳐(`join()`) 문자열로 반환합니다.

  ```
  word = '배고파'
  words = ['안녕', 'hello']
  
  # 아래에 코드를 작성하세요.
  '~'.join(word)
  >> 배~고~파'
  ' '.join(words)
  >>'안녕 hello'
  ```

- 문자변형 
  - 풀어보기



## 리스트(list)

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

원본 변경-> None

원본변경x-> 변경된 값을 return 

- .append

  ```
  new_cafe=cafe.append('banapresso')
  print(new_cafe)
  
  >> none # 원본을 조작하는 친구이기때문에 새로운 변수가 아니고 cafe변수를 넣어주면 됨.
  ```

- .extend

  - 리스트에 iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있습니다.

  ```
  cafe.extend(['wcafe', '빽다방'])
  print(cafe)
  >>['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso', 'wcafe', '빽다방']
  ```

  list와 list를 extend 해야함 !

  append 는 리스트로 안하고 넣음 x.append('s')

- insert(i,x)

  - ```
    cafe.insert(len(cafe)+100, '!')
    print(cafe)
    ```

  **원본변경이면 return 값이 없다!!!**

- pop

- clear 

  꼭 하기(원본변경인지 아닌지 return 값 나오는지 안나오는지)



- 리스트 복사

- 데이터의 분류 

  - mutable vs immutable 보기

- slice 연산자 사용

  ```
  a = [1, 2, 3]
  b = a[:] #b=a 와 다름 
  
  b[0] = 5
  print(a)
  >> [1, 2, 3]
  ```

- list()활용

  ```
  # 2차원 배열은 조금 다름
  a = [1, 2, [1, 2]] #[1,2]의 리스트 주소를 가리키는 것임.
  b = a[:]
  
  b[2][0] = 3
  print(a)
  >> [1, 2, [3, 2]]
  ```

  

### list comprehension

> 표현식과 제어문을 통해 리스트를 생성합니다.
>
> 여러 줄의 코드를 한 줄로 줄일 수 있습니다.
>
> 반복문을 짜보고 바꿔보자! 실습, 응용문제 풀기

```
numbers = range(1, 11)
cubic_list = []
for number in numbers:
    cubic_list.append(number ** 3)
print(cubic_list) 
 >>[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
 
 이걸 바꿔야함
 
 cubic_list = [number**3 for number in numbers]
 
```



```
even_list = []
for number in range(1,11):
    if number%2 ==0:
        even_list.append(number)
print(even_list)

바꿈

even_list = [number for number in range(1,11) if number%2 ==0]
```

- map(공통적으로 적용 할 함수, 순회가능한 자료)

  ```
  new=map(str,numbers)
  print(list(new))
  >>['1', '2', '3']
  ```



