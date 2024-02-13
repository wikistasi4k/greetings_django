from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('<str:name>/', views.greet_name, name='greet_name'),
]