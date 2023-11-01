from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/kadainew/', views.post_new, name='kadai_post_new'),
    path('post/yoteinew/', views.yotei_post_new, name='yotei_post_new'),
    path('post/zyugyounew/', views.zyugyou_post_new, name='zyugyou_post_new'),
    path('post/baitonew/', views.baito_post_new, name='baito_post_new'),    
    path('post/souzikinew/', views.souziki_post_new, name='souziki_post_new'),
    path('post/kazinew/', views.kazi_post_new, name='kazi_post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/delete/', views.delete_post, name='post_delete'),
    path('',views.post_start, name='post_start'),
]
