# Django

학습한 내용을 토대로 간단한 project의 준비 순서 및 작성법을 정리해 보았다.

- 첫 세팅

  - ```python
    # 가상환경
    python -m venv venv
    
    # 가상환경 실행
    source venv/Scripts/activate
    
    # 장고 설치
    pip install django==3.2.13
    
    # pip freeze
    pip freeze > requirements.txt
    
    # 프로젝트 생성
    django-admin startproject project_name .
    
    # 서버 확인
    python manage.py runserver
    
    # app 생성
    python manage.py startapp app_name
    
    # settings.py > INSTALLED_APPS에 app 추가
    INSTALLED_APPS = [
        'app_name',
        	...
    ]
    ```

  - ```python
    # 가장 바깥에 templates / base.html 생성 후
    {% block content %}
    {% endblock content %}
    # block 공간 마련
    
    # 이후 settings.py > TEMPALTES에서 BASE_DIR 설정
    TEMPLATES = ...
            'DIRS': [BASE_DIR / 'templates'],
            		...
    ```





- URL / VIEW / HTML 연결

  - URL

    - ```python
      # apps / urls.py 생성
      # 차후 url 호출 시 app_name에 할당한 'apps'와
      # name에 할당한 'index'를 토대로
      # apps:index 로 urls 호출
      from django.urls import path
      from . import views
      
      app_name = 'apps'
      urlpatterns = [
          path('', views.index, name='index'),
      ]
      
      
      
      # project / urls.py 에서 app에 따른 urls 분리
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('apps/', include('apps.urls')),
      ]
      ```

  

  - VIEW

    - ```python
      # apps / views.py 에서 사용할 view 함수 생성
      ### 예시
      def index(request):
          return render(request, 'apps/index.html')
      ```

  

  - HTML

    - ```python
      # apps / templates / apps 폴더 생성 후
      # 여기에 view함수가 호출 할 html파일 생성
      
      # base.html 기본 바탕으로
      {% extends 'base.html' %}
      
      # block을 활용한다
      {% block content %}
        <h1>INDEX</h1>
      {% endblock content %}
      ```





- DB 모델

  - ```python
    # apps / models.py 에서
    # from django.db import models > import된 models를 사용
    ### 예시
    class App(models.Model):
        title = models.CharField(max_length=20)
        audience = models.IntegerField()
        release_date = models.DateField()
        genre = models.CharField(max_length=30)
        score = models.FloatField()
        poster_url = models.TextField()
        description = models.TextField()
        
    # 이후 apps / migrations에 설계도를 만들기 위해
    python manage.py makemigrations
    
    # 이후 DB에 동기화를 하기 위해
    python manage.py migrate
    ```





- DB모델을 참조한 Form 만들기

  - ```py
    # apps / forms.py 를 만들고
    from django import forms
    from .models import App 	# App은 만들어 놓은 모델
    
    ### 예시
    class MovieForm(forms.ModelForm):
    	### MovieForm은 Meta의 내용을 참조한다.
        class Meta:
            model = Movie
            fields = '__all__'
    ```





- 메인 페이지 index

  - views

    - ```python
      def index(request):
          movies = Movie.objects.all() # Movie라는 모델의 모든 데이터를 할당
          context = {					 # context에 movies를 dict로 할당
              'movies' : movies
          }
          return render(request, 'movies/index.html', context)
      ```

  - html

    - ```python
      {% block content %}
      
        <h1>INDEX</h1>
        <a href="{% url 'movies:create' %}">[CREATE]</a>	# 생성 하이퍼링크
        <hr>
      
        {% for movie in movies %}		# for문 사용
      	# 제목을 누르면 해당 데이터의 detail을 보는 곳으로 이동
          <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
          # 영화의 제목
          <p>{{ movie.score }}</p>
          <hr>
        {% endfor %}
      
      {% endblock content %}
      ```



- 데이터 생성 create

  - url

    - ```python
      path('create/', views.create, name='create'),
      ```

  - views

    - ```python
      def create(request):
          # request의 method가 POST이면 수정해서 데이터에 새로 저장하는 것
          if request.method == "POST":
              # form은 request에 POST로 전달된 내용을 MovieForm에 매핑하여 할당한 것
              form = MovieForm(request.POST)
              # 그 내용이 적절하면(유효성 검사)
              if form.is_valid():
                  # 데이터에 저장하면서 그것을 movie에 할당
                  movie = form.save()
                  # 이 데이터의 pk를 전달하면서 detail url로 넘어감
                  return redirect('movies:detail', movie.pk)
      
      	# POST가 아니면(GET이면) 데이터 생성하는 페이지로 이동
          else:
              # form은 MovieForm
              form = MovieForm()
      	
          context = {
              'form' : form,
          }
          # MovieForm을 토대로 create 페이지로 이동
          return render(request, 'movies/create.html', context)
      ```

  - html

    - ```python
      {% block content %}
      	# POST 방식으로 create url로 보냄
        <form action="{% url 'movies:create' %}", method="POST">
      	# csrf 보안처리 
          {% csrf_token %}
          # 간단하게 MovieForm을 토대로 입력 받을 코드를 줄임
          # .as_p는 p태그로 감싼다는 뜻
          {{ form.as_p }}
          <input type="submit" value="submit">
          
      {% endblock content %}
      ```



- 데이터의 detail

  - url

    - ```python
      path('<int:pk>/', views.detail, name='detail'),
      ```

  - views

    - ```python
      # detail은 하나의 데이터를 특정해야 하기 때문에 pk를 인자값으로 받음
      def detail(request, pk):
          # 특정된 하나의 movie는 Movie모델의 objects에서 pk가 입력받은 pk인 녀석으로 특정
          movie = Movie.objects.get(pk=pk)
          # 그 특정된 녀석이 가지고 있는 모든 field의 값을 movie에 할당
          context = {
              'movie' : movie,
          }
        	# context에 담아 detail 페이지를 렌더링
          return render(request, 'movies/detail.html', context)
      ```

  - html

    - ```python
      {% block content %}
      	# movie에 담긴 특정한 녀석의 title, score, genre 등등을 출력
        <p>{{ movie.title }}</p>
        <p>{{ movie.audience }}</p>
        <p>{{ movie.release_date }}</p>
        <p>{{ movie.genre }}</p>
        <p>{{ movie.score }}</p>
        <p>{{ movie.poster_url }}</p>
        <p>{{ movie.description }}</p>
      
      {% endblock content %}
      ```



- 데이터 수정 update

  - url

    - ```python
      path('<int:pk>/update/', views.update, name='update')
      ```

  - views

    - ```python
      # update는 하나의 데이터를 특정해서 수정해야 하기 때문에 pk를 인자값으로 받음
      def update(request, pk):
          # 데이터 하나를 특정하고
          movie = Movie.objects.get(pk=pk)
          # request의 method가 POST이면
          if request.method == 'POST':
              # instance=movie가 있으면 수정하는 것이라고 함
              # 새롭게 전달받은 내용을 form에 저장하고
              form = MovieForm(request.POST, instance=movie)
              # 그 내용이 적절하면(유효성 검사)
              if form.is_valid():
                  # DB에 저장하고
                  form.save()
                  # 해당 pk를 전달하며 detail url로 넘어감 
                  return redirect('movies:detail', movie.pk)
              
          # request의 method가 POST가 아니면
          else:
              # form은 MovieForm 형태를 갖추는데 그 안의 담긴 내용이
              # 이미 특정된 데이터 movie의 내용을 가지고 있음 (instance = movie)
              form = MovieForm(instance = movie)
          # 특정된 movie와 form을 context에 담아
          context = {
              'movie' : movie,
              'form' : form,
          }
          # update 페이지로 이동
          return render(request, 'movies/update.html', context)
      ```

  - html

    - ```python
      {% block content %}
      	# update url로 pk값을 전달
          # 방식은 POST
        <form action="{% url 'movies:update' movie.pk%}" method='POST'>
      	# 보안처리
          {% csrf_token %}
          # MovieForm으로 쉽게 입력 받음
          {{ form.as_p }}
          <input type="submit">
        </form>
      
      {% endblock content %}
      ```

    - 

- 데이터 삭제 delete

  - url

    - ```python
      path('<int:pk>/delete/', views.delete, name='delete'),
      ```

  - views

    - ```python
      # 데이터 하나를 특정하기 위해 pk값을 받음
      def delete(request, pk):
          # movie에 특정 데이터를 할당하고
          movie = Movie.objects.get(pk=pk)
          # 그 녀석을 삭제
          movie.delete()
          # index url로 넘어감
          return redirect('movies:index')
      ```

  - html

    - ```python
      # delete url로 pk값을 전달
      # 방식은 POST
      <form action="{% url 'movies:delete' movie.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
      </form>
      ```

