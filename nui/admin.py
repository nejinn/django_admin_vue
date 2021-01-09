import nui
from django.contrib.auth.models import User, Group


# import nui


class NuiUser(nui.NuiModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active',)
    icon = 'nav-icon far nlyfont nly-icon-user-fill'


class NuiGroup(nui.NuiModelAdmin):
    list_display = ('id', 'name')
    icon = 'nav-icon far nlyfont nly-icon-security-fill'


nui.site.register(User, NuiUser)
nui.site.register(Group, NuiGroup)
