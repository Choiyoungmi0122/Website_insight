from django.contrib import admin
from .models import Item

from ast import Mod
from email import message
from operator import mod
from django.db import models

class ItemAdmin(admin.ModelAdmin):
    pass


class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
