from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from .models import Person


from django.contrib.auth.forms import UserChangeForm
from .forms import CustonUserChangeForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            birth = form.cleaned_data.get('birth')
            email = form.cleaned_data.get('email')  # 아이디, 이메일, 학번, 생일, 이름, 성별
            school = form.cleaned_data.get('studentid')
            name = form.cleaned_data.get('name')
            gender = form.cleaned_data.get('gender')

            member = Person(username=username, name=name, school=school, gender=gender, birth=birth, email=email)
            member.save()
            # print(username, email, school, birth, name, gender)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def memberpage(request):
    return render(request, 'common/member.html')

# @login_required
def update(request):
    #user_change_form = UserChangeForm(instance = request.user)
    return render(request, 'common/update.html')


