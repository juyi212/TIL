## 처음부터 eithers 작성



1. 가상환경 설정 
   - django 설치
2. 장고 프로젝트 만들기
   - 프로젝트 
   - 앱 (프로젝트 안 manage.py 위치한 곳에)
3. urls.py 분리/ 기본 template(base.html)
   - urls 분리
   - base.html( 부트스트랩 CDN 포함)
     - settings.py 등록



유저와 관련된 내용이 있다면,

Custom User 적용 까지 해줘야 함!

------------------------------

## 모델 정의

- 투표모델
  - 주제
  - 항목 2개
- 댓글 모델
  - 댓글 입력창
  - 외래키 



## 폼 정의

- 투표 모델을 기반으로 폼 정의
- 댓글 모델을 기반으로 폼 정의
  - 만든 후에 makemigrations, migrate



## 기능 정의

- 투표 모델은 생성과 조회 C, R
  - CREATE
  - READ