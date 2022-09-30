from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name='signup'),
    path('member/', views.memberpage, name='member'),
    path('update/', views.update, name='update'),
    path('mypage/',views.mypage,name = 'mypage'),
    path('d_day/',views.d_day,name = 'd_day'),
    path('report_after/', views.report_after, name='report_after'),
    path('report_before/', views.report_before, name='report_before'),
    path('Enroll/', views.Enroll, name='Enroll'),
    path('notice_before/', views.notice_before, name='notice_before'),
    path('cote_submit/', views.cote_submit, name='cote_submit'),
    path('cote_main/', views.cote_main, name='cote_main'),
    path('notice_list/', views.notice_list, name='notice_list'),
    path('report_list/', views.report_list, name='report_list'),
    path('cote_list/', views.cote_list, name='cote_list'),
    path('calender/', views.calender, name='calender'),
    path('notice_main/', views.notice_main, name='notice_main'),
    path('board_list/', views.board_list, name='board_list'),
    path('QnA_list/', views.QnA_list, name='QnA_list'),
    path('board_before/', views.board_before, name='board_before'),
    path('board_after/', views.board_after, name='board_after'),
    path('QnA_question/', views.QnA_question, name='QnA_question'),
    path('QnA_answer/', views.QnA_answer, name='QnA_answer')

]