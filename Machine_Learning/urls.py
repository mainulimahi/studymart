from django.urls import path
from . import views

urlpatterns = [
    path('', views.Machine_Learning),
    path('decision/', views.Decison),
]