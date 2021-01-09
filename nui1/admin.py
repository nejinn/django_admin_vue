# from django.contrib import admin
import nui
from .models import Test1


# Register your models here.

class TestAdmin(nui.NuiModelAdmin):
    list_display = ("id", "name")
    list_filter = ('id', 'name')
    search_fields = ("name", "id")


nui.site.register(Test1, TestAdmin)
