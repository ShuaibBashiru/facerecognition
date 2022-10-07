from django.urls import path
from . import views


urlpatterns = [
    path('signin', views.signin, name="user-signin"),
    path('dashboard/<str:name>/', views.dashboard, name="user-dashboard"),
]

