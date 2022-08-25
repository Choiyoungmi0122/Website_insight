"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))cd
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from insight import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insight/', include('insight.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index')     #로그인성공시 이동하는 /에 해당하는 path
]