#coding:utf-8

from django.urls import path, include
from . import views





app_name = 'blog_app'


urlpatterns = [
	path('',views.HomeView.as_view(), name='home'),
	path('post-detail/<title>/<int:id>/', views.PostDetailView.as_view(), name='post-detail'),
	path('add-post/', views.PostCreateView.as_view(), name='add'),
	path('post-update/<str:title>/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
	path('post-delete/<str:title>/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
			  
];