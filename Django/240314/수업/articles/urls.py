"""
URL configuration for my_thirld_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'articles'
# 특정 app의 기능을 사용하기 위한 요청 경로는
# 그 app이 직접 관리 할 수 있도록 구분해준다.
urlpatterns = [
    # 각 경로를 사용자가 브라우저의 주소창에 직접 입력하는 것 이외에도
    # 서비스를 구성할 때, 다른 view함수를 사용해야 하는 경우가 많다.
    # ex) nav bar에서, 각 페이지로 이동하는 링크를 만들 때
    # <a href="{% url "articles:" %}"></a>
    # 경로가 변경되더라도 해당 경로를 사용중인 모든 코드를 수정할 필요 없다.
    path('', views.index, name='index')
]
