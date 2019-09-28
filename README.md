# Hello Django


## 1. PART 01

### - 프로젝트 만들기 

```
...\> django-admin startproject mysite
```

코드를 저장할 디렉토리로 이동하여 위와 같은 명령을 수행하면 아래와 같은 mysite 디렉토리가 생성된다.

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

### - 개발 서버

```
...\> py manage.py runserver
```

위 명령으로 django 서버를 시작할 수 있다.

기본적으로, runserver 명령은 내부 IP 의 8000 번 포트로 개발 서버를 띄운다.

### - 설문조사 앱 만들기

cf) 프로젝트와 앱의 차이점
앱 : 특정한 기능(블로그나 공공 기록물을 위한 데이터베이스나, 간단한 설문조사 앱)을 수행하는 웹 어플리케이션. 
프로젝트: 이런 특정 웹 사이트를 위한 앱들과 각 설정들을 한데 묶어놓은 것. 프로젝트는 다수의 앱을 포함 가능. 앱은 다수의 프로젝트에 포함될 수 있음.

```
...\> py manage.py startapp polls
```

위와 같은 명령으로 앱을 만든다.

### - 뷰 호출하기

뷰를 호출하려면 이와 연결된 URL 이 있어야 하는데, 이를 위해 URLconf가 사용된다.
polls 디렉토리에서 URLconf를 생성하려면, urls.py라는 파일을 생성해야 한다.

최상위 URLconf 에서 polls.urls 모듈을 바라보게 설정하기 위해서는 mysite/urls.py 파일을 열고, django.urls.include를 import 하고, urlpatterns 리스트에 include() 함수를 추가한다.

include() 함수는 다른 URLconf(여기서는 polls.urls)들을 참조할 수 있도록 도와준다.


## 2. PART 02

### - 데이터베이스 설치

 SQLite는 Python에서 기본으로 제공되기 때문에 별도로 설치할 필요가 없다.
 
 **데이터베이스를 변경해보고 싶어서 데이터베이스 문서를 참고하고 공부해 보았는데 이해가 잘 안됐고 cmd창에서 에러 메시지가 떠서 일단은 접고 뒤의 내용을 공부했다.
 
 **mysite/settings.py를 편집할 때, 당신의 시간대에 맞춰 TIME_ZONE 값을 설정하세요. <<<설정했는데 나중에 오류가 나서 다시 UTC로 바꿨다.
 
 **데이터베이스 클라이언트에 접속해 장고가 생성한 테이블 확인에 실패했다.
 
 
 ### - 모델 만들기
 
 모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말한다.
 각 모델은 몇개의 클래스 변수를 가지고 있으며, 각각의 클래스 변수들은 모델의 데이터베이스 필드를 나타낸다.
 
 ### - 모델 활성화
 
 앱을 현재의 프로젝트에 포함시키기 위해서는, 앱의 구성 클래스에 대한 참조를 INSTALLED_APPS 설정에 추가해야 한다. 
 makemigrations 을 실행시킴으로서, 당신이 모델을 변경시킨 사실과(이 경우에는 새로운 모델을 만들었습니다) 이 변경사항을 migration으로 저장시키고 싶다는 것을 Django에게 알려줍니다.

migration은 Django가 모델(즉, 데이터베이스 스키마를 포함한)의 변경사항을 저장하는 방법으로써, 디스크상의 파일로 존재한다. 
migrate 명령은 아직 적용되지 않은 마이그레이션을 모두 수집해 이를 실행하며(Django는 django_migrations 테이블을 두어 마이그레이션 적용 여부를 추적) 이 과정을 통해 모델에서의 변경 사항들과 데이터베이스의 스키마의 동기화가 이루어진다.

<모델 변경하는법>
1. (models.py 에서) 모델을 변경.
2. python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만들기.
3. python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용.
(2번 3번 명령이 분리되어 있음)


### - Django 관리자 

```
...\> py manage.py createsuperuser
```
위 명령으로  관리 사이트에 로그인할 수 있는 관리자를 생성한다.

관리 사이트에서 poll app 을 변경가능하도록 하려면 polls/admin.py 파일을 열어 다음과 같이 편집하면 된다..

```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## 03. PART 03

### - 템플릿 만들기

우선, polls 디렉토리에 templates라는 디렉토리를 만든다. 그 안에 polls라는 디렉토리를 생성하고, index.html을 만든다.
views.py에서 템플릿을 호출하여 사용한다.

### - 404 에러 일으키기

파이썬의 예외 처리 코드를 사용해서 일으킨다.
get_object_or_404() 메소드를 import 해서 사용해도 된다.

