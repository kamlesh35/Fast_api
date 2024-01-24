from django.contrib import admin
from todayapp1.models import student


# Register your models here.


# @admin.site.register(student)
@admin.register(student)
class stud(admin.ModelAdmin):
    list_display = ['first_name','last_name','department','datetime','Active']
