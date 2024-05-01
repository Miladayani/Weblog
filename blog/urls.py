from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add', views. PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
