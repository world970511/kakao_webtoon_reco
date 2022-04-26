*윈도우 os 기준. 리눅스 혹은 다른 운영체제일 경우 체크 필요


```
0. 원하는 위치에 프로젝트 폴더 생성 (생성)

1. vs코드에서(혹은 다른 개발환경에서) 프로젝트 폴더로 이동. 이후 소스코드 다운로드(저장소 클론): git clone https://github.com/world970511/kakao_webtoon_reco.git 를 터미널에 입력.

2. 파이썬 가상환경 생성 python -m venv venvAi (아무데나 상관없지만 프로젝트 루트면 좋음... 프로젝트 폴더/venvAi 이 구조면 편하다는 이야기) 이후 가상환경 실행
cd venvAi/Scripts
activate
(구조가 틀릴 수 있음-- source ./venvAi/bin/activate 로도 테스트해보기)
    -- pip 업그레이드가 필요할 경우 -> *pip 최신 버전 업그레이드: python -m pip install --upgrade pip

3.필요 파이썬 패키지 설치
pip3 install -r require.txt     

4.서버 구동 확인: 
  cd back
  python manage.py runserver
  http://localhost:8000 로 접속 확인 후 서버 종료 : Ctrl + C
    *404 페이지 뜨는 거 당연하니까 놀라지 말기

5. 신규 브랜치 생성(서로 같은 파일 작업 시 문제 발생을 줄여줌)
 git checkout -b "프로젝트명" (ex: git checkout -b nauen 이런 식으로 입력)

6. git add .

7. git commit -m "feat: first commit" 입력

8. git push origin "프로젝트명" (ex: git push origin nauen 이런 식으로 입력)

추가 참고 

* model 수정시 :
  python manage.py makemigrations
  python manage.py migrate --run-syncdb
  python manage.py createsuperuser
  이후 db_uploaders.py 디버깅해서 초기 데이터 업로드
  
* 초기 db 생성: python manage.py (db.sqlite3 파일 생성 - 장고 기본 초기 DB)
* 초기 관리자 생성: python manage.py createsuperuser
 - id / pw : admin / 1q..

* python manage.py runserver 명령으로 서버 구동후 localhost:8000/admin 으로 접속하여 Django admin 페이지에서 User, Product에 +(더하기버튼)눌러 아무 적당한 값들을 입력하여 데이터들 디비에 입력.

* 서버에서 전달하는 데이터 확인 방법: 웹 브라우저나 포스트맨에서 아래 api 주소로 확인하면됨.
 localhost:8000/api/product/ 또는 localhost:8000/api/user 에 접속하여 추가한 데이터들이 JSON 형식으로 잘 리턴되는지 확인

* 혹시 안된다면 아래 DB 모델 관련 마이그레이션 명령어들 실행 후 python manage.py runserver 명령으로 서버 구동해 볼 것.

* DB/모델 추가/변경시 새 마이그레션을 생성:
  python manage.py makemigrations
  python manage.py migrate

커밋컨벤션: https://overcome-the-limits.tistory.com/entry/%ED%98%91%EC%97%85-%ED%98%91%EC%97%85%EC%9D%84-%EC%9C%84%ED%95%9C-%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9D%B8-git-%EC%BB%A4%EB%B0%8B%EC%BB%A8%EB%B2%A4%EC%85%98-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0
이거 참고해서 깃 관리할거라 참고해주십셔
```

++
머지 후 브랜치 삭제한 이후

1) git pull <저장소 명 (보통 origin)> main
을 사용해서 로컬도 최신으로 유지

2) git checkout -b <신규 브랜치명>

그 이후는 위와 동일