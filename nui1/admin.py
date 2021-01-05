from django.contrib import admin
import nui
from .models import Test1


# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


nui.site.register(Test1, TestAdmin)
