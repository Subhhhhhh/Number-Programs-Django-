"""
URL configuration for Number_Programs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', number_programs, name='number_programs'), 
    path('is_prime/<int:n>/', is_prime, name='is_prime'),
    path('is_armstrong/<int:n>/', is_armstrong, name='is_armstrong'),
    path('is_perfect/<int:n>/', is_perfect, name='is_perfect'),
    path('is_disarium/<int:n>/', is_disarium, name='is_disarium'),
    path('is_niven/<int:n>/', is_niven, name='is_niven'),
    path('is_spy/<int:n>/', is_spy, name='is_spy'),
    path('is_palindrome_num/<int:n>/', is_palindrome_num, name='is_palindrome_num'),
    path('is_evil/<int:n>/', is_evil, name='is_evil'),
    path('is_strong/<int:n>/', is_strong, name='is_strong'),

]
