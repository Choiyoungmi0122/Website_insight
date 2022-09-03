from django.contrib import admin
from .models import Person
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
# admin.site.register(Users, userAdmin)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'school', 'email', 'gender', 'birth']
    list_display_links = ['name', 'school']