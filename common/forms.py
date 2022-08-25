from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    name = forms.CharField(label = "사용자이름")
    birth = forms.IntegerField(label = "생일")
    gender = forms.IntegerField(label = "성별")
    studentid = forms.IntegerField(label="학번")
    class Meta:
        model = User
        fields = ("name", "username", "password1", "password2", "birth", "email", "gender")
