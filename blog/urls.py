from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/kadainew/', views.post_new, name='kadai_post_new'),
    #path('post/nyuuryoku/', views.post_nyuuryoku, name='post_nyuuryoku'),  
    path('post/yotei/', views.yotei_post_new, name='yotei_post_new'),
    path('post/zyugyounew/', views.zyugyou_post_new, name='zyugyou_post_new'),
    path('post/baitonew/', views.baito_post_new, name='baito_post_new'),    
    path('post/souzikinew/', views.souziki_post_new, name='souziki_post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('',views.post_start, name='post_start'),
]
