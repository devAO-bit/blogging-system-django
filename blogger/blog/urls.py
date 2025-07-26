from django.urls import path
from .views import blog_list, blog_detail, blog_create

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
]