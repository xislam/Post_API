from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.post_list, name="posts_list"),
    path('post_detail/<str:pk>/', views.post_detail, name="post_detail"),
    path('post_create/', views.post_create, name="post_create"),
    path('post_update/<str:pk>/', views.post_update, name="post_update"),
    path('post_delete/<str:pk>/', views.post_delete, name="port_delete"),
    path('comment_list/', views.comment_list, name="comment_list"),
    path('comment_detail/<str:pk>/', views.comment_detail, name="comment_detail"),
    path('comment_create/', views.comment_create, name="comment_create"),
    path('comment_update/<str:pk>/', views.comment_update, name="comment_update"),
    path('comment_delete/<str:pk>/', views.comment_delete, name="comment_delete"),
]