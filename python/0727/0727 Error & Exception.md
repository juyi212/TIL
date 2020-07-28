# 0727 Error & Exception

## 에러(Error)

- 문법 에러 (syntax error)
  - 오타나 불안전한 코드 일때 
  - parser 에러가 감지된 가장 앞의 위치를 알려줌
  - EOL: End of Line  - 어딘가에서 string(''," ")을 닫아주지 않았구나
  - EOF: End of File - 괄호
- 예외(Exception)
  - ZeroDivisionError -0으로 나눌 수 없다
  - NameError- 선언되지 않음, 정의되지 않음
  - TypeError- 자료형에 대한 타입이 맞지않아 에러가 나올 경우
  - ValueError-존재하지 않는 값을 찾고자 할 경우..
  - IndexError-
  - ModuleNotFoundError
  - ImportError
  - KeyboardInterrupt



## 예외 처리(Exception Handing)

- try & except

  ```
  try :
  	에러가 날 거 같은 코드
  except:
  	처리하는 코드
  ```

  ```
  #
  try:
      num = input('값을 입력하시오 : ')
      print(int(num))
  except:
      print('숫자를 다시 입력해주세요')
  
  ```

- 에러 메세지 처리 as

  ```
  #indexerror 어떤 것들에서 어떤 에러가 나는지 과목평가에 나옴.
  try:
      empty_list = []
      print(empty_list[-1])
  except IndexError as error:
      print(error)   
  ```

- 복수의 예외 처리

  ```
  #
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      print(100/int(num))
  except (ValueError, ZeroDivisionError):
      print('무언가가 잘 못 되었습니다.')
      
  #
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      print(100/int(num))
  except ValueError:
      print('글자가 아닌 숫자를 입력해주세요.')
  except ZeroDivisionError:
      print('0으로는 나눗셈을 할 수 없습니다.')
  
  ```

  

- else

  ```
  #에러가 발생하지 않는 경우 실행 시킬 문장은 else를 활용한다.
  
  #
  try:
      numbers = [1, 2, 3]
      number = numbers[3]
  except IndexError:
      print('오류 발생')
  else:
      print(number)
  ```

  

- finally

  - 어떤 경우에든 반드시 실행해야하는 코드에는 `finally`를 활용한다.
  - 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
  - 예외의 발생 여부과 관계없이 항상 실행된다.

  ```
  try:
      languages = {'python': 'good'}
      languages['python']
  except KeyError as err:
      print(f'{err}는 딕셔너리에 없는 키입니다.')
  finally:
      print('감사합니다')
  ```

- raise

  - 예외를 강제로 발생시킬 수 있습니다.

    ```
    rais NameError('이름이 없습니다.')
    ```