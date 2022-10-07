from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('app/logout', views.logout, name="logout"),
]

