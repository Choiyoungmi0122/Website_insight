from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Users(models.Model):
    username=models.CharField(max_length=64, verbose_name="사용자명")
    #useremail=models.EmailField(max_length=128, verbose_name="사용자 이메일")
    password=models.CharField(max_length=64, verbose_name="비밀번호")
    registered_dttm=models.DateField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.username

    #DB테이블 이름 설정
    class Meta:
        db_table="users"
        verbose_name="사용자"
        verbose_name_plural="사용자"
