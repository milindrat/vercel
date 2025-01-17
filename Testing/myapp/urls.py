
from django.urls import path
from myapp import views


urlpatterns = [
    path('ver/', views.home_view, name='home_view'),
]