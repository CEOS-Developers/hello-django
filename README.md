# Hello Django

## Polls 앱 만들기

1. 프로젝트 만들기


    `django-admin startproject mysite`<br>=> mysite 대신에 내가 원하는 디렉토리명 사용가능<br>
    `python3 manage.py runserver`<br> =>기본 포트 8000으로 서버 생성?
2. 설문조사 앱 만들기


    `python3 manage.py startapp polls`
3. 데이터 베이스 설정
   
    기본으로 SQlite 설정되어 있음<br>
    `python3 manage.py migrate ` => settings.py에서 Installed_APPS의 설정을 탐색하여 필요한 데이터 베이스 테이블을 생성
4. 모델 만들기


    모델 => 부가적인 메타 데이터를 가진 데이터 베이스의 구조(layout)<br><br>
    Question, Choice => django.db.models.Model 클래스의 서브 클래스로 표현<br><br>
    `Installed_APPS`에 `Polls.app.PollsConfig`를 추가해야함<br> => Django가 Polls앱이 포함된것을 알아 차리기위해<br>
    `python3 manage.py makemigrations polls` => 모델을 변경시킨 사실과 변경사항을 migration으로 저장<br>
    `python3 manage.py migrate` => 아직 적용되지 않은 migration을 모두 수집해 실행, 모델에서의 변경사항들과 데이터 스키마의 동기화
5. API 사용해보기


    `python3 manage.py shell` <br>
    => 대화식 python 쉘에 들어가 Django API를 자유롭게 다룰수 있음
6. 관리자 생성하기

    `python3 manage.py createsuperuser`
    => name,email,password를 설정하면 관리자 생성 끝
    `django.contrib.auth`모듈에서 제공되고 Question을 관리자 사이트에서 편집하고 싶으면 `polls/admin.py`에서 `django.contrib.auth`로 register를 해주어야한다.
7. 뷰 추가하기
   
   polls디렉토리에 templates디렉토리를 만들고 그 안에 polls 디렉토리를 생성한다. Django는 여기서 템플릿을 찾게 된다.<br>
    `render()`를 사용하면 `loader`와 `HttpResponse`를 임포트하지 않아도 된다.<br>
    `render(request, "polls/index.html", context)` =>`request `객체를 첫번째 인수로 받고, `템플릿 이름`을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적 인수로 받는다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환된다.

8. 템플릿 시스템 사용하기
    
    {{ 변수 }} 중괄호 안에 context를 통해 넘겨진 변수를 이용하여 views에서의 값을 템플릿 안에서 사용할 수 있다.
9. 템플릿에서 하드 코딩된  url제거하기

    `polls.urls` 모듈의 `path()` 함수에서 인수의 이름을 정의했으므로, `{% url %}` template 태그를 사용하여 url 설정에 정의된 특정한 URL 경로들의 의존성을 제거할 수 있다.
