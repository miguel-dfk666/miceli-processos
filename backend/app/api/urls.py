from django.urls import path
from rest_framework.routers import DefaultRouter
from app.api.views import PostViewSet, CustomUserViewSet, CustomUserLoginViewSet

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
post_router.register(r'custom-users', CustomUserViewSet, basename='customuser')
post_router.register(r'login', CustomUserLoginViewSet, basename='login')
