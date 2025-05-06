from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # API
    path('api/posts/', api_views.PostListCreateAPIView.as_view(), name='api_post_list_create'),
    path('api/posts/<int:pk>/', api_views.PostRetrieveUpdateDestroyAPIView.as_view(), name='api_post_detail'),
]

