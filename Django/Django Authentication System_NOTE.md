# Django Authentication System

---

- 사전작업

  - ```python
    # accounts 앱 생성
    python manage.py startapp accounts
    
    # settings.py > INSTALLED_APPS 에 accounts 등록
    ```

  - ```python
    # accounts url 분리 및 매핑
    
    # accounts 앱에 urls.py 생성하고
    from . import views
    app_name = 'accounts'
    urlpatterns = [
    ]
    
    # main project / urls.py 에서 url 분리
    path('accounts/', include('accounts.urls')),
    ```

  - ```python
    # 기존 User model을 Custom user model로 대체하기
    
    # accounts / models.py 에서
    from django.contrib.auth.models import AbstractUser
    
    class User(AbstractUser):
        pass
    
    # settings.py 에서 기존 auth.User를
    # 방금 위에서 만든 accounts.User 로 바꿈
    AUTH_USER_MODEL = "accounts.User" 
    
    # accounts / admin.py 
    from django.contrib.auth.admin import UserAdmin
    from .models import User
    
    admin.site.register(User, UserAdmin)
    ```



- login

  - ```python
    # urs 생성
    urlpatterns = [
        path('login/', views.login, name='login')
    ]
    ```

  - ```python
    # view 함수 생성
    from django.contrib.auth.forms import AuthenticationForm
    
    # login 페이지로 렌더링 하는 부분 먼저 작성
    def login(request):
        if request.method == 'POST':
            pass
        else:
            form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'accounts/login.html', context)
    ```

  - ```python
    # accounts/templates/accounts에 html 생성
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>LOGIN</h1>
        
      <form action="{% url 'accounts:login' %}" method='POST'>
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    
    ```

  - ```python
    # login 기능을 하는 view 함수 마저 완성
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import login as auth_login # 뒤에 정의하는 def login과 이름이 같아 auth_login으로 사용
    
    def login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST) # AuthenticationForm은 첫번째 인자로 request를 받고 뒤에 내용을 받음
            if form.is_valid():
                auth_login(request, form.get_user()) # user정보는 form에 들어 있음, .get_user()를 사용해서 유저정보를 추출
                return redirect('articles:index')
    ```

  - ```python
    # 로그인이 되어 있는지 확인하기 위해 base.html 에 작성
    # user는 settings.py 에서 이미 참조하는 녀석이라 그냥 써도 됨
    <h3>{{ user }}</h3>
    
    # base.html에 login 하이퍼링크 생성
    <a href="{% url 'accounts:login' %}">LOGIN</a>
    ```
  
  - 

