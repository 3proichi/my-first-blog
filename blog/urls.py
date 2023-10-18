from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/zyugyounew/', views.zyugyou_post_new, name='zyugyou_post_new'),
    path('post/baitonew/', views.baito_post_new, name='baito_post_new'),    
    path('post/souzikinew/', views.souziki_post_new, name='souziki_post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('',views.post_start, name='post_start'),
]
