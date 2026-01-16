from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('medical-info/', views.medical_info, name='medical_info'),
    path('help/', views.help_page, name='help_page'),

]
