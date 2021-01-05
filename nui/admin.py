from django.contrib import admin
import nui
from django.contrib.auth.models import User, Group


# import nui

# Register your models here.
class myadmin(admin.ModelAdmin):
    pass


class NuiUser(nui.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active',)
    icon = 'nav-icon far nlyfont nly-icon-user-fill'


class NuiGroup(nui.ModelAdmin):
    list_display = ('id', 'name')
    icon = 'nav-icon far nlyfont nly-icon-security-fill'


nui.site.register(User, NuiUser)
nui.site.register(Group, NuiGroup)
