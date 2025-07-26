from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Add this line
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
