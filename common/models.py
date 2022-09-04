from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=10)
    username=models.CharField(max_length=41)
    school=models.IntegerField()
    email=models.EmailField()
    gender=models.IntegerField()
    birth=models.IntegerField()

    def __str__(self):
        return self.name


    @property
    def is_staff(self):
        return self.is_staff




