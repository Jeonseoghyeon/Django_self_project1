from django.contrib import admin
from django.urls import path
from . import views


app_name = 'accounts' # app_name 추가 잊지 말자! 이걸 해줘야 'accounts:index'처럼 연결해줄 수 있음

urlpatterns = [
    # 각각 urlnamespace 써줬다 -> 나중에 세부 주소가 바뀌어도 처리해주기 쉬워짐!!!! * 이해한 부분!
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    ]