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



- LOGIN

  - ```python
    # url 생성
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



- LOGOUT

  - ```python
    # url 생성
    path('logout/', views.logout, name='logout'),
    ```

  - ```python
    # view 함수 생성
    from django.contrib.auth import logout as auth_logout
    
    def logout(request):
        auth_logout(request)
        # logout 하고 메인 페이지로
        return redirect('articles:index')
    ```

  - ```python
    # base.html에 logout 버튼 생성
    <form action="{% url 'accounts:logout' %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    ```



- 회원가입(user create)

  - ```python
    # url 생성
    path('signup/', views.signup, name='signup'),
    ```

  - ```python
    # CustomUserCreationForm 만들기
    
    # accounts / forms.py 생성 후 작성
    # UserCreationForm 은 model이 user로 되어 있음
    # 우리는 우리가 만든 models.py 의 User를 사용할 예정
    from django.contrib.auth.forms import UserCreationForm
    # .models의 User클래스를 import할 수 있지만 장고는 이것을 사용하라고 함!
    # get_user_model() 은 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
    from django.contrib.auth import get_user_model
    
    # Custom~ 은 기존 UserCreationForm을 상속 받아
    class CustomUserCreationForm(UserCreationForm):
    	# 그 안의 Meta 클래스 속 model을 우리의 User로 변경해야 함
        # 따라서 Meta 도 UserCreationForm 속 Meta를 상속 받고
        # get_user_model() 을 사용해서 model을 변경!
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            
    # 회원정보수정하는 UserChangeForm 도 마찬가지로 model이 user라서 같이 바꿔줌
    
    ```

  - ```python
    # views에서 signup 함수 생성
    
    # 위에서 만든 Custom~ 을 가져옴
    from .forms import CustomUserCreationForm
    
    def signup(request):
        if request.method == 'POST':
    		pass
        
        # 회원가입 페이지로!
        else:
            form = CustomUserCreationForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/signup.html', context)
    ```

  - ```python
    # signup.html 생성
    {% extends 'base.html' %}
    
    # 사실 form을 다 제공해줘서 바뀌는게 거의 없음!
    {% block content %}
      <h1>SIGNUP</h1>
      <form action="{% url 'accounts:signup' %}" method='POST'>
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    
    # base.html 에 signup 하이퍼링크 생성
    <a href="{% url 'accounts:signup' %}">Signup</a>
    ```

  - ```python
    # views에서 signup 함수 마저 완성
    def signup(request):
        if request.method == 'POST':
            
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                # 회원가입 후 바로 로그인 하도록 하려면
                user = form.save() # form.save()는 user를 반환, user에 내용을 담고
                auth_login(request, user) # 로그인 함
                return redirect('articles:index')
            
            
        else:
            form = CustomUserCreationForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/signup.html', context)
    ```

  - ```python
    # 회원가입할 때 받고 싶은 정보(accounts model의 field)를 커스텀하려면
    class CustomUserCreationForm(UserCreationForm):
    
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            # fields를 조작하면 됨
            # 얘는 튜플로 이루어져 있음
            fields = UserCreationForm.Meta.fields + ('email', )
            
    ```

  

- 회원탈퇴

  - ```python
    # url 생성
    path('delete/', views.delete, name='delete'),
    ```

  - ```python
    # views에서 delete 함수 생성
    def delete(request):
        # DB에서 지우는 것
        request.user.delete()
        # 세션에서도 지우고 싶다면
        auth_logout(request)
        return redirect('articles:index')
    ```

  - ```python
    # base.html 에서 회원탈퇴 버튼 생성
    <form action="{% url 'accounts:delete' %}" method='POST'>
      {% csrf_token %}
      <input type="submit" value='회원탈퇴'>
    </form>
    ```



- 회원정보수정

  - ```python
    ```

  - 
