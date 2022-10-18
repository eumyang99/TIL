22.10.18 08lect

REST API

1. 대표 HTTP Request Methods
   1. GET
      1.  리소스 표현을 요청, 데이터 **검색**
   2. POST
      1. 데이터를 지정된 리소스에 **제출**(Submit), 서버의 상태를 **변경**
   3. PUT
      1. 리소스를 **수정**
   4. DELETE
      1. 리소스를 **삭제**



2. URI(Uniform Resource Identifier) 통합 자원 식별자
   1. 원하는 자원을 특정하는 식별자
   2. URN = 특정 이름공간에서 **이름**으로 리소스를 식별하는 URI
      1. ex) 국제 표준 도서번호, 국제 표준 시청각 자료번호
   3. URL = Uniform Resource Locator(통합 자원 위치)
      1. 자원의 **위치**로 자원을 식별
      2. URL 구조
         1. Scheme(or protocol)
            1. 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
            2. URL 첫 부분에 나타냄
            3. **https**://www.example.com:80/path/to/myfile.html/?key=value#quick-start
         2. Authotiry
            1. Scheme 다음 :// 으로 구분된 Authority(권한)이 작성됨
            2. domain과 port를 포함하고 :(콜론)으로 구분됨
               1. Domain name
                  1. 요청중인 웹 서버를 나타냄
                  2. 구글은 142.251.42.142 인데 외우기 어려우니까 Domain name으로 사용
                  3. https://**www.example.com**:80/path/to/myfile.html/?key=value#quick-start
               2. Port
                  1. 웹 서버 리소스에 접근하는 데에 사용되는 기술적인 문(Gate)
                  2. http 프로토콜 표준 포트는 HTTP -> 80 / HTTPS -> 443이고 이 둘은 생략 가능
                  3. https://www.example.com**:80**/path/to/myfile.html/?key=value#quick-start
                  4. 장고에서는 별도로 쓸 일은 없음
            3. Path
               1. 웹 서버의 리소스 상세 경로
               2. 예전에는 물리적인 경로를 나타냈는데 요새는 추상화된 형태의 구조를 표현
               3. 예를 들어 /articles/create/가 실제 articles 폴더 안의 create 폴더 안을 나타내는 것은 아니니까
               4. https://www.example.com:80/**path/to/myfile.html**/?key=value#quick-start
            4. Parameters
               1. 웹 서버에 제공하는 추가적인 데이터
               2. '&' 기호로 구분되는 key-value 쌍 목록
               3. https://www.example.com:80/path/to/myfile.html/**?key=value**#quick-start
            5. Anchor
               1. 리소스의 다른 부분에 대한 앵커
               2. 리소스 내부 일종의 '북마크', 해당 북마크 지점에 있는 컨텐츠를 표시
               3. '#' 이후 부분은 서버에 전송되지 않고(불필요) 브라우저에게 해당 지점으로 이동하도록 함
               4. https://www.example.com:80/path/to/myfile.html/?key=value**#quick-start**



3. API(Application Programming Interface)
   1. 애플리케이션과 프로그래밍으로 소통하는 방법
      1. 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공하는 구성
   2. 가전 제품의 플러그를 꽂으면 제품이 작동하는 것처럼 우리가 직접 배선을 하지 않음, 매우 비효율적
   3. API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)



4. Web API
   1. 웹 서버 or 웹 브라우저를 위한 API
   2. 현재 웹 개발은 AtoZ 개발보다 여러 open API를 활용하는 추세
      1. open API
         1. 개발자라면 누구나 사용할 수 있도록 공개된 API
         2. 개발자에게 권한을 제공해줌
   3. ex) youtube API, Naver Papago API, Kakao Map API 등
   4. API는 다양한 타입의 데이터를 보내주는데 우리는 JSON을 주목



5. REST(Representational State Transfer)
   1. '소프트웨어 아키텍처 디자인 제약 모음'
   2. REST의 기본 아이디어는 리소스
      1. 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 설계 방법론
      2. 자원을 식별 - URI
      3. 자원에 대한 행위 - HTTP Methods
      4. 자원을 표현 - JSON
   3. REST에서 자원을 정의하고 주소를 지정하는 방법
      1. 자원의 식별
         1. URI
      2. 자원의 행위
         1. HTTP Method
            1. GET
            2. POST
            3. PUT
            4. DELETE
      3. 자원의 표현
         1. 자원과 행위를 통해 궁극적으로 표현되는 결과물
         2. JSON으로 표현된 데이터를 제공



6. JSON
   1. JavaScript의 표기법을 따른 단순 문자열
   2. 파이썬의 dict, 자바스크립트의 object처럼 c 계열 언어가 갖고 있는 자료구조로 쉽게 변환 가능한 key-value형태의 구조를 갖고 있음
   3. 현재 API에서 가장 많이 사용하는 데이터 타입



7. Response

   1. 다양한 방법으로 JSON 데이터 응답해보기

      1. HTML 응답
      2. JsonResponse()를 사용한 JSON 응답
      3. Django Serializer를 사용한 JSON 응답
      4. **DJango REST framework를 사용한 JSON 응답**
         1. ModelSerializer
            1. ModelSerializer 클래스는 모델 필들에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
            2. Model 정보에 맞춰 자동으로 필드를 생성
            3. serializer에 대한 유효성 검사기 자동 생성(is_valid())
            4. .create() 및 .update()의 간단한 기본 구현이 포함됨

   2. DJango REST framework를 사용한 JSON 응답

      1. Postman 설치

      2. 데이터 migrate

      3. python manage.py loaddata articles.json

      4. pip install djangorestframework

      5. settings.py 의 installed_apps 에 rest_framework 추가

      6. pip freeze > requirements.txt 로 갱신

      7. articles에 serializers.py 파일 생성

      8. ```python
         # articles/serializers.py 
         from rest_framework import serializers	# drf에서 제공하는 모델 시리얼라이즈 사용
         from .models import Article				# 모델 import
         
         class ArticleListserializer(serializers.ModelSerializer):
             
             class Meta:
                 model = Article
                 fields = ('id', 'title', 'content') # 전체를 받고 싶으면 all하면 됨
         ```

      9. python manage.py shell_plus 에서 연습
   
         1. 단일 데이터
   
            1. from articles.serializers import ArticleListSerializer
            2. serializer = ArticleListSerializer()
            3. serializer 출력 후 확인
            4. article = Article.objects.get(pk=1)
            5. serializer = ArticleListSerializer(article)
            6. serializer 출력 후 확인
            7. serializer.data 출력 후 확인
   
         2. 쿼리셋 시리얼라이저 데이터
   
            1. articles = Article.objects.all()
   
            2. serializer = ArticleListSerializer(articles, many=True)
   
               1. 단일이 아니고 쿼리셋일 경우 many=True를 해야 함
   
            3. serializer.data 출력 후 확인
   
               
   
   3. Buile RESTful API - Article
   
      1. GET - List
   
         1. 게시글 데이터 목록 조회하기
   
         2. DRF에서 api_view 데코레이터 작성 필수
   
         3. ```python
            # articles/urls.py
            from django.urls import path
            from . import views
            
            # app_name 필요없음
            urlpatterns = [
                path('articles/', views.article_list),
            ]
            
            # articles/views.py
            from rest_framework.response import Response
            
            from .serializers import ArticleListSerializer
            from .models import Article
            
            @api_view(['GET'])
            def article_list(request):
                articles = Article.objects.all()
                serializer = ArticleListSerializer(articles, many=True)
                return Response(serializer.data)
                
            ```
   
      2. GET - Detail
   
         1. 단일 게시글 데이터 조회하기
   
         2. 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의
   
         3. ```python
            # articles/serializers.py
            class ArticleSerializer(serializers.ModelSerializer):
                
                class Meta:
                    model = Article
                    fields = '__all__'
            
            # articles/urls.py
            urlpatterns = [
                path('articles/', views.article_list),
                path('articles/<int:article_pk>', views.article_detail),
            ]
            
            # articles/views.py
            from .serializers import ArticleListSerializer, Articleserializer#추가
            
            @api_view(['GET'])
            def article_detail(request, article_pk):
                articles = Article.objects.get(pk=article_pk)
                serializer = ArticleListSerializer(articles)
                return Response(serializer.data)
            ```
   
      3. POST
   
         1. 게시글 데이터 생성하기
   
         2. 데이터 생성이 성공했으면 201 Created 상태 코드를, 실패했을 때는  400 Bad request를 응답
   
         3. 지금 pk를 받지 않는 article_list 함수와 받아야 하는 article_detail 함수가 있는데 데이터 생성은 pk값이 필요 없으니 article_list 함수에서 기능을 추가
   
         4. ```python
            # articles/views.py
            from rest_framework import status
            
            @api_view(['GET', 'POST'])
            def article_list(request):
                # 전체 조회 기능은 GET 방식일 때
                if request.method == 'GET':
                    articles = Article.objects.all()
                    serializer = ArticleListSerializer(articles, many=True)
                    return Response(serializer.data)
                
                # 데이터 생성은 POST 방식일 때
            	elif request.method == 'POST':
                    serializer = ArticleSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
            ```
   
      4. DELETE
   
         1. 게시글 데이터 삭제하기
   
         2. 데이터 삭제가 성공했으면 204 No Content 상태 코드를 응답
   
         3. pk를 받아야 특정 게시글을 삭제하니  article_detail 함수에 기능을 추가
   
         4. ```python
            # articles/views.py
            
            @api_view(['GET', 'DELETE'])
            def article_detail(request, article_pk):
                articles = Article.objects.get(pk=article_pk)
                
                # 단일 데이터 조회는 GET 방식일 때
                if request.method == 'GET':
                    serializer = ArticleListSerializer(article)
                    return Response(serializer.data)
                
                # 특정 데이터 삭제는 DELETE 방식일 때
            	elif request.method == 'DELETE':
                    article.delete()
                    return Response(status=status=status.HTTP_204_NO_CONTENT)
            ```
   
      5. PUT
   
         1. 게시글 데이터 수정하기
   
         2. 데이터 수정이 성공했을 경우 200 OK 상태 코드 응답
   
         3. 마찬가지로 pk를 받아야 특정 게시글을 수정하니  article_detail 함수에 기능을 추가
   
         4. ```python
            # articles/views.py
            
            @api_view(['GET', 'DELETE'])
            def article_detail(request, article_pk):
                article = Article.objects.get(pk=article_pk)
                
                # 단일 데이터 조회는 GET 방식일 때
                if request.method == 'GET':
                    serializer = ArticleListSerializer(article)
                    return Response(serializer.data)
                
                # 특정 데이터 삭제는 DELETE 방식일 때
            	elif request.method == 'DELETE':
                    article.delete()
                    return Response(status=status=status.HTTP_204_NO_CONTENT)
                
                # 특정 데이터 수정은 PUT 방식일 때
                elif request.method == 'PUT':
                    serializer = ArticleSerializer(article, data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response(serializer.data)
            ```



4. Buile REST framework - N:1 Relation

   1. 강의 흐름 상 사전 준비

      1. Comment 모델 주석 해제 및 데이터베이스 초기화
      2. python manage.py makemigrations / python manage.py migrate 진행
      3. python manage.py loaddata articles.json comments.json 데이터 로드

   2. GET - List

      1. 댓글 데이터 목록 조회하기

      2. Article List와 비교하며 작성해보기

      3. ```python
         # articles/serializers.py 
         class CommentSerializer(serializers.ModelSerializer):
             
             class Meta:
                 model = Comment
                 fields = '__all__'
                 
         # articles/urls.py
         urlpatterns = [
             path('articles/', views.article_list),
             path('articles/<int:article_pk>', views.article_detail),
             path('comments/', views.comment_list), # url 추가
         ]
         
         # articles/views.py
         from .models import Article, Comment# 추가
         from .serializers import ArticleListSerializer, Articleserializer, CommentSerializer#추가
         
         @api_view(['GET'])
         def comment_list(request):
             if request.method == 'GET':
                 comments = Comment.objects.all()
                 serializer = CommentSerializer(comments, many=True)
                 return Response(serializer.data)
         ```

   3. GET - Detail

      1. 단일 댓글 데이터 조회

      2. Article과 달리 같은 serializer 사용하기

      3. ```python
         # articles/urls.py
         urlpatterns = [
             path('articles/', views.article_list),
             path('articles/<int:article_pk>', views.article_detail),
             path('comments/', views.comment_list),
             path('comments/<int:comment_pk>/', views.comment.detail), # url추가
         ]
         
         # articles/views.py
         @api_view(['GET'])
         def comment_detail(request, comment_pk):
             comment = Comment.objects.get(pk=comment_pk)
             
             # 단일 데이터 조회는 GET 방식일 때
             if request.method == 'GET':
                 serializer = CommentSerializer(comment)
                 return Response(serializer.data)
         ```

   4. POST

      1. 단일 댓글 데이터 생성하기

         1. article의 pk가 필요해서 새로운 url을 만들어야 함

      2. ```python
         # articles/urls.py
         urlpatterns = [
             path('articles/', views.article_list),
             path('articles/<int:article_pk>', views.article_detail),
             path('comments/', views.comment_list),
             path('comments/<int:comment_pk>/', views.comment.detail),
             path('articles/<int:article_pk>/comments/', views.comment_create)
         ]
         
         # articles/views.py
         @api_view(['POST'])
         def comment_create(request, article_pk):
             article = Article.objects.get(pk=article_pk)
             serializer = CommentSerializer(data=request.data)
             if serializer.is_valid(raise_exception=True):
                 # 댓글을 외래키가 필요함
                 # 그래서 .save(commit=False)를 하면서 인스턴스를 생성해서 저장을 했었었는데
                 # 여기서는 .save(article=article)로 해결
                 # 그러나 is_valid 검사를 할 때 article가 충족되지 않아서 불가능
                 # 따라서 article은 검사대상에서 제외하고 읽기 전용 필드로만 사용
                 # 맨 밑에 처럼 CommentSerializer를 조정
                 serializer.save(article=article)
                 return Response(serializer.data, status=status.HTTP_201_CREATED)
             
             
             
         # articles/serializers.py 
         class CommentSerializer(serializers.ModelSerializer):
             
             class Meta:
                 model = Comment
                 fields = '__all__'
                 read_only_fields = ('article',) # 읽기 전용 필드로 설정
         ```

   5. DELETE & PUT

      1. 댓글 데이터 삭제 및 수정

      2. 위의 article과 동일

      3. ```python
         # articles/views.py
         @api_view(['GET', 'DELETE', 'PUT'])
         def comment_detail(request, comment_pk):
             comment = Comment.objects.get(pk=comment_pk)
             if request.method == 'GET':
                 serializer = CommentSerializer(comment)
                 return Response(serializer.data)
         
             elif request.method == 'DELETE':
                 comment.delete()
                 return Response(status=status.HTTP_204_NO_CONTENT)
         
             elif request.method == 'PUT':
                 serializer = CommentSerializer(comment, data=request.data)
                 if serializer.is_valid(raise_exception=True):
                     serializer.save()
                     return Response(serializer.data)
         ```



5. N:1 - 역참조 데이터 조회
   1. 특정 게시글에 작성된 댓글 목록 출력하기
      1. 기존 필드 override
   2. 특정 게시글에 작성된 댓글 개수 출력하기
      1. 새로운 필드 추가