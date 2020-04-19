from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    # 아래는 각 페이지마다 특정 pk값을 가진 놈들 넘겨주기 위함
    path('<int:pk>/detail/', views.detail,name='detail'),
    path('<int:pk>/update/', views.update,name='update'),
    path('<int:pk>/delete/', views.delete,name='delete'),
    ]