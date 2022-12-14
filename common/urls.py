from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.login, name = 'login'),
    path('singup/', views.signup, name='signup'),
    path('member/', views.memberpage, name='member'),
    path('mypage/', views.mypage, name='mypage'),
]



