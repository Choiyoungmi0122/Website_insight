from django.contrib import admin
from .models import Users

class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
admin.site.register(Users, userAdmin)