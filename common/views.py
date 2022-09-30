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


@login_required
def update(request):
    if request.method=='POST':
        user_change_form = CustonUserChangeForm(instance = request.user)
    return render(request, 'common/update.html', {'user_change_form':user_change_form})

def mypage(request):
    return render(request,'common/mypage.html')

def d_day(request):
    return render(request,'common/d_day.html')

def report_after(request):
    return render(request,'common/report_after.html')

def report_before(request):
    return render(request,'common/report_before.html')

def Enroll(request):
    return render(request,'common/Enroll.html')

def notice_before(request):
    return render(request,'common/notice_before.html')

def cote_submit(request):
    return render(request,'common/cote_submit.html')

def cote_main(request):
    return render(request,'common/cote_main.html')

def notice_list(request):
    return render(request,'common/notice_list.html')

def report_list(request):
    return render(request,'common/report_list.html')

def cote_list(request):
    return render(request,'common/cote_list.html')

def calender(request):
    return render(request,'common/calender.html')

def notice_main(request):
    return render(request,'common/notice_main.html')

def board_list(request):
    return render(request,'common/board_list.html')

def QnA_list(request):
    return render(request,'common/QnA_list.html')

def board_before(request):
    return render(request,'common/board_before.html')

def board_after(request):
    return render(request,'common/board_after.html')

def QnA_question(request):
    return render(request,'common/QnA_question.html')

def QnA_answer(request):
    return render(request,'common/QnA_answer.html')