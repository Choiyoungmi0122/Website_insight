from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import views
#correction user
from django.contrib.auth import get_user_model
from .models import Person


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    name = forms.CharField(label = "사용자이름")
    birth = forms.IntegerField(label = "생일")
    gender = forms.IntegerField(label = "성별")
    studentid = forms.IntegerField(label = "학번")
    username = forms.CharField(label="사용자아이디")


    class Meta:
        model = User
        fields = ("name", "username", "password1", "password2", "birth", "email", "gender")  #form의 피릴래

class CustonUserChangeForm(UserChangeForm):
    class Meta:
        model = Person()
        fields = ['name', 'email', 'birth', 'gender']