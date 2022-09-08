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
    # url 생성
    path('update/', views.update, name='update'),
    ```
    
  - ```python
    # views에서 update 함수 생성
    def update(request):
        if request.method == 'POST':
            pass
        else:
            # 위에 만들었던 커스텀change폼
            # instance 는 수정할 때 쓰는 인자 =  request의 user정보
            form = CustomUserChangeForm(instance=request.user)
       	context = {
            'form' = form,
        }
        return render(request, 'accounts/update.html', context)
    ```
  
  - ```python
    # 커스텀chaneform의 field를 조작하지 않으면
    # 정보수정화면에서 회원 등급까지 스스로 바꿀 수 있게 됨
    # 따라서 수정할 정보만 나타나도록 field를 제한해야 함
    class CustomUserChangeForm(UserChangeForm):
    
        class Meta(UserChangeForm.Meta):
            model = get_user_model()
            fields = ('email', 'first_name', 'last_name',)
    ```
  
  - ```python
    # update.html 생성
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>회원정보수정</h1>
      # 역시 유사한 html 모습
      <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    
    {% endblock content %}
    ```
  
  - ```python
    # views에서 update 함수 완성
    def update(request):
        if request.method == 'POST':
            # form에 커스텀change폼 내용을 instance와 함께 담고
            form = CustomUserChangeForm(request.POST, instance=request.user)
            # form = CustomUserChangeForm(data=request.POST, instance=request.user)
            # 유효성 검사 후
            if form.is_valid():
                # DB에 저장
                form.save()
                return redirect('articles:index')
        else:
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    ```
  
  - ```python
    # base.html에 버튼 생성
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
    ```



- 비밀번호 변경

  - ```python
    # url 생성
    # 변수명이 겹칠 수 있으니 view함수 이름을 change_passoword로 설정
    path('password/', views.change_password, name='change_password'),
    ```

  - ```python
    # view 함수 생성
    # PasswordChangeForm import 받고
    from django.contrib.auth.forms import PasswordChangeForm
    
    def change_password(request):
        if request.method == 'POST':	
            pass
        else:
            # PasswordChangeForm에 request.user로 user 정보 입력
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```

  - ```python
    # html 생성
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>비밀번호변경</h1>
        
      <form action="{% url 'accounts:change_password' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
        
      </form>
    {% endblock content %}
    ```

  - ```python
    # view 함수 완성
    # 비밀번호 변경 후 로그인이 풀리지 않도록 세션을 업데이트해주는 함수
    from django.contrib.auth import update_session_auth_hash
    
    def change_password(request):
        if request.method == 'POST':
            # PasswordChangeForm 는 첫번재 인자로 유저정보를 받음
            form = PasswordChangeForm(request.user, request.POST)
            # 유효성 검사
            if form.is_valid():
                # DB에 저장
                form.save()
                # 이걸 하지 않으면 기존 세션과 회원인증정보가 불일치, 로그인이 풀림
                update_session_auth_hash(request, form.user)
                return redirect('articles:index')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```



- 로그인 유저와 비로그인 유저에게 다른 화면을 출력 제공하기

  1. 표면적 접근 : is_authenticated attribute
     - 권한과 관련 없고, 유저가 활성화 상태인지 유효한 세션을 가졌는지도 확인하지 않음
     - 단지 로그인 유저인지 비로그인 유저인지 True/False로 나누어주기만 할 뿐
  2. 내부적 접근 : login_required 데코레이터

  - ```python
    # base.html에서
    
    	# 만약 request.user 가 is_authenticated이면
        {% if request.user.is_authenticated %}
        	# 유저명 표시
          <h3>{{ user }}</h3>
        	# 로그아웃 form 표시
          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
          </form>
        	# 회원탈퇴 form 표시
          <form action="{% url 'accounts:delete' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="회원탈퇴">
          </form>
        	# 회원정보수정 하이퍼링크 표시
          <a href="{% url 'accounts:update' %}">회원정보수정</a>
          
        {% else %}
        	# 로그인 하이퍼링크 표시
          <a href="{% url 'accounts:login' %}">Login</a>
        	# 회원가입 하이퍼링크 표시
          <a href="{% url 'accounts:signup' %}">Signup</a>
        {% endif %}
        <hr>
        {% block content %}
        {% endblock content %}
    
        
    # articles/templates/articles/index.html (메인페이지)에서
    # 로그인 유저만 create 버튼이 보이도록
    {% extends 'base.html' %}
    
    {% block content %}
      <h1>Articles</h1>
      	###################### 이 부분!!!!
      {% if request.user.is_authenticated %}
        <a href="{% url 'articles:create' %}">CREATE</a>
      {% endif %}
    	######################
      <hr>
      {% for article in articles %}
        <p>글 번호 : {{ article.pk }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
        <hr>
      {% endfor %}
    {% endblock content %}
    
    
    #######################################################################
    # 그런데 이렇게만 view함수에서 차단한 것이 아니기 때문에 로그인 상태에서 url만 입력하면 login 화면으로 넘어감...
    # 비로그인 상태에서 url만 입력하면 create 화면으로 넘어감...
    ```

  - ```python
    # 그래서 view함수에서 로그인 유저가 
    # 로그인 url에 접근하면 메인페이지로 보내버리는 조건문
    def login(request):
        if request.user.is_authenticated:
            return redirect('articles:index')
        ...
    ```

  - ```python
    # articles/views 에서
    # 유저가 로그인을 했는지 확인하는 login_required 데코레이터 import
    from django.contrib.auth.decorators import login_required
    
    @login_required
    def create(request):
        ...
        
    @login_required
    def update(request, pk):
        ...
    ```

  - ```python
    # is_authenticated 에서 가시적으로 가리기는 했음
    # 그러나 url로 타고 들어가면 해당 html을 rendering 해서 보여주었음
    # 그래서 login_required 데코레이터로 비로그인일 경우 함수에 접근을 막음
    # 비로그인 상태에서 함수에 접근하면 login_required는 로그인하라고 요청함
    # 요청된 로그인 이후 'next' 파라미터에 해당하는 url로 이동하라고 쿼리가 생김
    # 그곳으로 이동하려면 로그인 이후 메인페이지로 이동하는 것이 아니라 해당 url로 가야함
    {% extends 'base.html' %}
    {% block content %}
      <h1>LOGIN</h1>
        ##################################### 이 부분 action=""
      <form action="" method="POST">	# action을 비워두면 해당 url 전체를
    	##################################### 입력 받음(자기자신에게 보냄)
        
        # accounts/login/?next='parameter' 일 경우
        # accounts/login/ 이곳으로 내용을 보내고
        # ?next='parameter' 이 정보도 보내는 것
        # 따라서 next 파라미터 정보를 보내기 위해서 action="비워둠"
        
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
      </form>
    {% endblock content %}
    
    # next 파라미터가 있을 경우에 next의 value로 보내야 하기 때문에 분기처리 함
    # def login(request)에서 method가 'POST'일 때
    if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            # form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                # 로그인
                auth_login(request, form.get_user())
                # next 파라미터가 있다면 next키에 해당하는 value로 redirect함
                return redirect(request.GET.get('next') or 'articles:index')###################### 이 부분
    
    
    
    ```

  - ```python
    # def delete는 create와 update와는 다름
    @login_required
    @require_POST
    def delete(request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    
    # 이 경우 @login_required로 로그인하면 next파라미터인 delete가 실행되지 않음
    # next파라미터가 GET방식으로 보내는 것이기 때문에
    # @require_POST 에 막힘
    
    # 따라서 @login_required 를 붙일 수 없음
    # 대신 is_authenticated 를 이용해서 로그인 여부를 판단함
    @require_POST
    def delete(request, pk):
        # 로그인 한 유저이면 뒤를 진행
        if request.user.is_authenticated:
            article = Article.objects.get(pk=pk)
            article.delete()
        return redirect('articles:index')
    
    ```



- 마지막 마무리

  - ```python
    # accounts/views와 articles/views에 적절한 데코레이터 작성 
    
    from django.contrib.auth.decorators import login_required
    from django.views.decorators.http import require_POST, require_http_methods
    
    # login_required
    # require_POST
    # require_http_methods
    # 사용
    
    @require_http_methods(['GET', 'POST'])
    def login(request):
        
    @require_POST
    def logout(request):
        
    @require_http_methods(['GET', 'POST'])
    def signup(request):
    
    @require_POST
    def delete(request):    
        
    @login_required
    @require_http_methods
    def update(request):
        
    @login_required
    @require_http_methods
    def change_password(request):
    ```

    

